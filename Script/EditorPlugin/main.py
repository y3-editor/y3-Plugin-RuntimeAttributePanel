# -*- coding: utf-8 -*-
import G
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTreeWidgetItem, QListWidgetItem
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QCheckBox, QGroupBox, QGridLayout, QScrollArea, QStackedLayout
from PyQt5.QtGui import QPixmap, QIcon
from ui_runtime_debug_tool import Ui_RuntimeDebugToolDialog
from ui_runtime_debug_tool_select import Ui_RuntimeDebugToolSelectDialog
import os
import json
import copy

class MyMainWindow(QWidget):
    def __init__(self, contain_widget):
        super(MyMainWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.main_window = (contain_widget == Ui_RuntimeDebugToolDialog)
        self.widget = contain_widget()
        self.widget.setupUi(self)

    def is_mouse_on_title_bar(self, pos):
        """判断鼠标是否在标题栏内"""
        title_geometry = self.widget.titleWidget.geometry()
        return title_geometry.contains(pos)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.is_mouse_on_title_bar(event.pos()):
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    
    def mouseMoveEvent(self, event):
        if hasattr(self, 'drag_position') and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()
    
    def mouseReleaseEvent(self, event):
        if hasattr(self, 'drag_position') and event.button() == Qt.LeftButton:
            del self.drag_position
            event.accept()

    def closeEvent(self, event):
        if self.main_window:
            QApplication.quit()
        else:
            super(MyMainWindow, self).closeEvent(event)

class Plugin(object):

    def on_start(self):
        G.logger.info('on start')
        self.regist_event()
        self.unit = None
        self.unit_kvs = {}
        self.game_paused = False
        self.default_show_conf_type = 'creature'
        self.page_idx = None
        self.recore_alter = {}
        self.kv_record_alter = {}
        self.init_original_attr_conf()
        self.scroll_value = 0
        self.attr_scroll_value = 0
        self.conf_expand_state = {}
        self.attr_expand_state = {}
        self.view_map = {}
        self.attrs_cache = {}
        self.attr_lineedit_map = {}
        self.kv_lineedit_map = {}
        self.load_attr_conf()
    
    def regist_event(self):
        G.EventSystem.regist_event(G.EventType.StartSoftPause, lambda: self.on_pause_game_change(True))
        G.EventSystem.regist_event(G.EventType.EndSoftPause, lambda: self.on_pause_game_change(False))
        G.EventSystem.regist_event(G.EventType.SwitchMode, self.on_editor_mode_switch)
        G.EventSystem.regist_event(G.EventType.ON_SELECT_UNIT_EVENT, self.on_select_unit)

    def on_pause_game_change(self, pause_state):
        self.set_pause_btn_text(pause_state)

    def on_editor_mode_switch(self, mode):
        if self.unit:
            self.unit.unregist_event(self.unit.OnAttrChange, self.on_unit_attr_change)
            self.unit.unregist_event(self.unit.OnKvChange, self.on_unit_kv_change)
            self.unit = None
        self.game_paused = False
        if mode == G.EditorRunMode.EditorMode:
            self.switch_page(0)
        elif mode == G.EditorRunMode.GameMode:
            self.switch_page(2)

    def init_original_attr_conf(self):
        self.original_attr_conf = {}
        datas = {
            'creature': G.UnitType.Creature,
            'item': G.UnitType.Item,
            'destructible': G.UnitType.Destructible,
        }
        for key, type in datas.items():
            self.original_attr_conf[key] = G.Helper.query_type_attrs(type)
            self.original_attr_conf[key]['show_kv'] = 'kv属性'

    def load_attr_conf(self):
        self.attr_conf = {
            'creature': set(),
            'item': set(),
            'destructible': set()
        }
        conf_path = G.Helper.get_plugin_root_path()
        path = os.path.join(conf_path, 'attr_conf.json')
        if os.path.exists(path):
            with open (path, 'r') as f:
                self.attr_conf = json.load(f)
                self.attr_conf['creature'] = set(self.attr_conf['creature'])
                self.attr_conf['item'] = set(self.attr_conf['item'])
                self.attr_conf['destructible'] = set(self.attr_conf['destructible'])
        else:
            self.attr_conf['creature'] = set(self.original_attr_conf['creature']['base'].keys() + self.original_attr_conf['creature']['custom'].keys() + ['show_kv',])
            self.attr_conf['item'] = set(self.original_attr_conf['item']['base'].keys() + self.original_attr_conf['item']['custom'].keys() + ['show_kv',])
            self.attr_conf['destructible'] = set(self.original_attr_conf['destructible']['base'].keys() + self.original_attr_conf['destructible']['custom'].keys() + ['show_kv',])
        self.temp_attr_conf = copy.deepcopy(self.attr_conf)

    def save_attr_conf(self):
        conf_path = G.Helper.get_plugin_root_path()
        path = os.path.join(conf_path, 'attr_conf.json')
        with open(path, 'w+') as f:
            dumy = dict(self.attr_conf)
            dumy['creature'] = list(dumy['creature'])
            dumy['item'] = list(dumy['item'])
            dumy['destructible'] = list(dumy['destructible'])
            json.dump(dumy, f)

    def on_select_unit(self, unit):
        if unit != self.unit:
            if self.unit:
                self.unit.unregist_event(self.unit.OnAttrChange, self.on_unit_attr_change)
                self.unit.unregist_event(self.unit.OnKvChange, self.on_unit_kv_change)
            self.unit = unit
            self.unit_name = self.unit.get_name() + '(%i)' % self.unit.unit_id
            self.unit_kvs = self.unit.get_kvs()
            self.unit.regist_event(self.unit.OnKvChange, self.on_unit_kv_change)
            self.unit.regist_event(self.unit.OnAttrChange, self.on_unit_attr_change)
        self.refresh_attr_widget(True)
        self.switch_page(1)
    
    def on_unit_attr_change(self, attr_key, val):
        self.attrs_cache[attr_key] = val
        textbox = self.attr_lineedit_map[attr_key]
        if textbox.isWidgetType():
            textbox.blockSignals(True)
            textbox.setText(str(val))
            textbox.blockSignals(False)
    
    def on_unit_kv_change(self, key, val):
        #说明kv被删掉了
        if val == None and key in self.unit_kvs:
            self.unit_kvs.pop(key)
            self.refresh_attr_widget()
            return
        self.unit_kvs[key] = val
        box = self.kv_lineedit_map.get(key)
        if box and box.isWidgetType():
            if isinstance(box, QCheckBox):
                box.blockSignals(True)
                box.setCheckState(Qt.Checked if val else Qt.Unchecked)
                box.blockSignals(False)
            else:
                box.blockSignals(True)
                box.setText(str(val))
                box.blockSignals(False)
        else:
            self.refresh_attr_widget()

    def get_unit_type(self):
        map = {
            G.UnitType.Creature: 'creature',
            G.UnitType.Item: 'item',
            G.UnitType.Destructible: 'destructible',
        }
        if self.unit:
            return map[self.unit.unit_type]
        return 'creature'

    def get_current_attrs(self):
        if self.unit:
            return self.unit.get_attributes()
        return {}

    def set_unit_attr(self, key, val):
        if self.unit:
            self.unit.set_attr_val(key, val)

    def set_unit_kv(self, key, val):
        if self.unit:
            self.unit.set_kv(key, val)

    def create_widgets(self):
        self.main_panel = MyMainWindow(Ui_RuntimeDebugToolDialog)
        self.config_panel = MyMainWindow(Ui_RuntimeDebugToolSelectDialog)
        self.main_widget = self.main_panel.widget
        self.config_widget = self.config_panel.widget
        self.main_panel.show()
        self.setup_main_widget()
        self.setup_config_widget()
        self.on_editor_mode_switch(G.EditorRunMode.get_current_mode())
        return [self.main_panel, ]

    def switch_page(self, page_idx):
        if page_idx == self.page_idx:
            return
        self.page_idx = page_idx
        self.main_widget.stackedWidget.setCurrentIndex(self.page_idx)
        if self.page_idx == 0:
            #主界面
            self.main_widget.pushButtonListPlay.setEnabled(True)
            self.main_widget.pushButtonListPlay.disconnect()
            self.main_widget.pushButtonListPlay.clicked.connect(lambda _:G.Helper.switch_game_or_editor_inside() or self.main_widget.pushButtonListPlay.setEnabled(False))
            self.main_widget.pushButtonListPlay.setVisible(True)
            self.main_widget.pushButtonListAdd_3.setVisible(False)
            self.main_widget.pushButtonListStop.setVisible(False)
            self.main_widget.label.setVisible(False)
            self.main_widget.label_entity.setVisible(False)
            self.main_widget.pushButtonSetting.setVisible(False)
        elif self.page_idx == 1:
            #属性修改界面
            self.main_widget.pushButtonListAdd_3.setVisible(not self.game_paused)
            self.main_widget.pushButtonListStop.setEnabled(True)
            self.main_widget.pushButtonListStop.setVisible(True)
            self.main_widget.label.setVisible(True)
            self.main_widget.label_entity.setVisible(True)
            self.main_widget.pushButtonSetting.setVisible(True)
            self.main_widget.treeWidget.setColumnCount(2)
            self.main_widget.treeWidget.setHeaderLabels(['属性名', '值'])
            self.main_widget.treeWidget.header().resizeSection(0, 300)
        else:
            #属性修改空白界面
            self.main_widget.pushButtonListPlay.setEnabled(True)
            self.main_widget.pushButtonListPlay.disconnect()
            self.main_widget.pushButtonListPlay.clicked.connect(self.change_pause_state)
            self.main_widget.pushButtonListPlay.setVisible(self.game_paused)
            self.main_widget.pushButtonListAdd_3.setVisible(not self.game_paused)
            self.main_widget.pushButtonListStop.setEnabled(True)
            self.main_widget.pushButtonListStop.setVisible(True)
            self.main_widget.label.setVisible(True)
            self.main_widget.label_entity.setVisible(True)
            self.main_widget.pushButtonSetting.setVisible(True)

    def refresh_attr_widget(self, refresh_all=False):
        can_edit = self.game_paused
        if not self.unit: return
        self.attrs_cache = self.get_current_attrs() if refresh_all or not self.attrs_cache else self.attrs_cache
        conf_type = self.get_unit_type()
        treeWidget = self.main_widget.treeWidget
        scrollbar = treeWidget.verticalScrollBar()
        last_scroll_value = self.attr_scroll_value
        self.main_widget.label_entity.setText(self.unit_name)
        treeWidget.curr_conf_type = conf_type
        treeWidget.clear()
        unit_type = self.unit.unit_type
        root = QTreeWidgetItem(self.main_widget.treeWidget)
        root.group_name = 'all'
        root.setExpanded(not self.attr_expand_state.get(conf_type, {}).get('all', True))
        name_map = {
            G.UnitType.Creature: '单位属性',
            G.UnitType.Item: '物品属性',
            G.UnitType.Destructible: '可破坏物属性'
        }
        label = QLabel(name_map[unit_type])
        label.setStyleSheet("font-size:12px;color:#D0D0D0;")
        treeWidget.setItemWidget(root, 0, label)
        base_attr_node = QTreeWidgetItem(root)
        base_attr_node.group_name = 'base'
        label = QLabel('基础属性')
        label.setStyleSheet("font-size:12px;color:#D0D0D0;")
        treeWidget.setItemWidget(base_attr_node, 0, label)
        base_attr_node.setExpanded(not self.attr_expand_state.get(conf_type, {}).get('base', True))
        custom_attr_node = QTreeWidgetItem(root)
        custom_attr_node.group_name = 'custom'
        label = QLabel('自定义属性')
        label.setStyleSheet("font-size:12px;color:#D0D0D0;")
        treeWidget.setItemWidget(custom_attr_node, 0, label)
        custom_attr_node.setExpanded(not self.attr_expand_state.get(conf_type, {}).get('custom', True))

        idx = 0
        for attr_key in self.attr_conf[conf_type]:
            parent_node = None
            atype = ''
            if attr_key in self.original_attr_conf[conf_type]['base']:
                parent_node = base_attr_node
                atype = 'base'
            elif attr_key in self.original_attr_conf[conf_type]['custom']:
                parent_node = custom_attr_node
                atype = 'custom'
            if parent_node != None:
                val = self.attrs_cache.get(attr_key)
                if val is None and self.attrs_cache:
                    continue
                attr_widget = QTreeWidgetItem(parent_node)
                desc = self.original_attr_conf[conf_type][atype][attr_key]
                label = QLabel(desc)
                label.setStyleSheet("font-size:12px;color:#D0D0D0;")
                attr_type = type(val)
                if attr_type == bool:
                    box = QCheckBox('')
                    box.setStyleSheet(self.checkbox_style_sheet)
                    box.setCheckState(Qt.Checked if val else Qt.Unchecked)
                    box.stateChanged.connect(lambda state,key=attr_key, at=attr_type:self.on_text_changed(state, key, at) or self.apply_attr())
                    box.setEnabled(can_edit)
                    self.attr_lineedit_map[attr_key] = box
                else:
                    box = QLineEdit()
                    box.setReadOnly(not can_edit)
                    box.setStyleSheet(self.lineedit_style_sheet)
                    box.setText(str(val))
                    self.attr_lineedit_map[attr_key] = box
                    box.textChanged.connect(lambda text, key=attr_key, at=attr_type:self.on_text_changed(text, key, at))
                    box.editingFinished.connect(lambda: self.apply_attr())
                self.main_widget.treeWidget.setItemWidget(attr_widget, 0, label)
                self.main_widget.treeWidget.setItemWidget(attr_widget, 1, box)
                idx += 1
        if 'show_kv' in self.attr_conf[conf_type]:
            kv_attr_node = QTreeWidgetItem(root)
            label = QLabel('KV属性')
            label.setStyleSheet("font-size:12px;color:#D0D0D0;")
            treeWidget.setItemWidget(kv_attr_node, 0, label)
            kv_attr_node.group_name = 'show_kv'
            kv_attr_node.setExpanded(not self.attr_expand_state.get(conf_type, {}).get('show_kv', True))
            for key, val in self.unit_kvs.items():
                attr_widget = QTreeWidgetItem(kv_attr_node)
                label = QLabel()
                label.setStyleSheet("font-size:12px;color:#D0D0D0;")
                label.setText(key)
                attr_type = type(val)
                if attr_type == bool:
                    box = QCheckBox('')
                    box.setStyleSheet(self.checkbox_style_sheet)
                    box.setCheckState(Qt.Checked if val else Qt.Unchecked)
                    box.stateChanged.connect(lambda state,key=key, at=attr_type:self.on_text_changed(state, key, at, True))
                    box.setEnabled(can_edit)
                    self.kv_lineedit_map[key] = box
                else:
                    box = QLineEdit()
                    self.kv_lineedit_map[key] = box
                    box.setReadOnly(not can_edit)
                    box.setStyleSheet(self.lineedit_style_sheet)
                    box.setText(str(val))
                    box.textChanged.connect(lambda text, key=key, at=attr_type:self.on_text_changed(text, key, at, True))
                    box.editingFinished.connect(lambda: self.apply_attr())
                self.main_widget.treeWidget.setItemWidget(attr_widget, 0, label)
                self.main_widget.treeWidget.setItemWidget(attr_widget, 1, box)
                idx += 1

        scrollbar.setValue(last_scroll_value)
        self.main_widget.treeWidget.addTopLevelItem(root)
    
    def on_conf_collapsed(self, collapsed, item):
        conf_type = self.config_widget.treeWidget.curr_conf_type
        if conf_type not in self.conf_expand_state:
            self.conf_expand_state[conf_type] = {}
        self.conf_expand_state[conf_type][item.group_name] = collapsed
    
    def on_attr_collapsed(self, collapsed, item):
        conf_type = self.main_widget.treeWidget.curr_conf_type
        if conf_type not in self.attr_expand_state:
            self.attr_expand_state[conf_type] = {}
        self.attr_expand_state[conf_type][item.group_name] = collapsed

    def refresh_config_widget(self, conf_type, view_node_key=None, state=None):
        scrollbar = self.config_widget.treeWidget.verticalScrollBar()
        last_scroll_value = self.scroll_value
        treeWidget = self.config_widget.treeWidget
        treeWidget.curr_conf_type = conf_type
        treeWidget.clear()
        self.view_map = self.calc_view_data(conf_type, view_node_key, state)
        name_map = {
            'creature': '单位属性',
            'item': '物品属性',
            'destructible': '可破坏物属性'
        }
        root = QTreeWidgetItem(self.config_widget.treeWidget)
        root.group_name = 'all'
        root.setExpanded(not self.conf_expand_state.get(conf_type, {}).get('all', True))

        base_attr_node = QTreeWidgetItem(root)
        base_attr_node.group_name = 'base'
        base_attr_node.setExpanded(not self.conf_expand_state.get(conf_type, {}).get('base', True))
        
        custom_attr_node = QTreeWidgetItem(root)
        custom_attr_node.group_name = 'custom'
        custom_attr_node.setExpanded(not self.conf_expand_state.get(conf_type, {}).get('custom', True))
        
        kv_node = QTreeWidgetItem(root)
        label = QLabel('kv属性')
        label.setStyleSheet("font-size:12px;color:#D0D0D0;")
        checkbox_kv = QCheckBox('')
        checkbox_kv.setStyleSheet(self.checkbox_style_sheet)
        checkbox_kv.setCheckState(self.view_map['show_kv'])
        treeWidget.setItemWidget(kv_node, 0, label)
        treeWidget.setItemWidget(kv_node, 1, checkbox_kv)
        for view_node_key, state in self.view_map.items():
            if view_node_key == 'all':
                label = QLabel(name_map[conf_type])
                label.setStyleSheet("font-size:12px;color:#D0D0D0;")
                self.checkbox_root = QCheckBox('')
                self.checkbox_root.setStyleSheet(self.checkbox_style_sheet)
                self.checkbox_root.setCheckState(self.view_map[view_node_key])
                treeWidget.setItemWidget(root, 0, label)
                treeWidget.setItemWidget(root, 1, self.checkbox_root)
            elif view_node_key == 'base':
                label = QLabel('基础属性')
                label.setStyleSheet("font-size:12px;color:#D0D0D0;")
                self.checkbox_base = QCheckBox('')
                self.checkbox_base.setStyleSheet(self.checkbox_style_sheet)
                self.checkbox_base.setCheckState(self.view_map[view_node_key])
                treeWidget.setItemWidget(base_attr_node, 0, label)
                treeWidget.setItemWidget(base_attr_node, 1, self.checkbox_base)
            elif view_node_key == 'custom':
                label = QLabel('自定义属性')
                label.setStyleSheet("font-size:12px;color:#D0D0D0;")
                self.checkbox_custom = QCheckBox('')
                self.checkbox_custom.setStyleSheet(self.checkbox_style_sheet)
                self.checkbox_custom.setCheckState(self.view_map[view_node_key])
                treeWidget.setItemWidget(custom_attr_node, 0, label)
                treeWidget.setItemWidget(custom_attr_node, 1, self.checkbox_custom)
            elif view_node_key == 'show_kv':
                continue
            else:
                parent_node = None
                attrs = None
                if view_node_key in self.original_attr_conf[conf_type]['base']:
                    parent_node = base_attr_node
                    attrs = self.original_attr_conf[conf_type]['base']
                else:
                    parent_node = custom_attr_node
                    attrs = self.original_attr_conf[conf_type]['custom']
                attr_desc = attrs[view_node_key]
                conf_widget = QTreeWidgetItem(parent_node)
                label = QLabel(attr_desc)
                label.setStyleSheet("font-size:12px;color:#D0D0D0;")
                checkbox = QCheckBox('')
                checkbox.setCheckState(self.view_map[view_node_key])
                checkbox.setStyleSheet(self.checkbox_style_sheet)
                checkbox.stateChanged.connect(lambda state, cf=conf_type, ak=view_node_key: self.on_cb_state_change(state, cf, ak))
                treeWidget.setItemWidget(conf_widget, 0, label)
                treeWidget.setItemWidget(conf_widget, 1, checkbox)
        self.checkbox_root.stateChanged.connect(lambda state, cf=conf_type:self.set_config_group('all', cf, state))
        self.checkbox_base.stateChanged.connect(lambda state, cf=conf_type:self.set_config_group('base', cf, state))
        self.checkbox_custom.stateChanged.connect(lambda state, cf=conf_type:self.set_config_group('custom', cf, state))
        checkbox_kv.stateChanged.connect(lambda state, cf=conf_type, ak='show_kv': self.set_kv_show(state, cf, ak))
        
        treeWidget.addTopLevelItem(root)
        scrollbar.setValue(last_scroll_value)
        self.config_widget.treeWidget.header().resizeSection(0, 280)
        self.config_widget.treeWidget.header().resizeSection(1, 30)
    
    def calc_view_data(self, conf_type, view_node_key=None, state=None):
        view_map = {}
        original_conf = self.original_attr_conf[conf_type]
        conf = self.temp_attr_conf[conf_type]
        if not original_conf['custom']:
            view_map['custom'] = Qt.Checked
        view_map['show_kv'] = Qt.Checked if 'show_kv' in conf else Qt.Unchecked
        idx = 0
        for attr_type, attr in original_conf.items():
            if attr_type == 'show_kv':continue
            parent_node = attr_type
            if not attr: continue
            all_unchecked = True
            all_checked = True
            for attr_key, attr_desc in attr.items():
                if attr_key in conf:
                    all_unchecked = False
                    view_map[attr_key] = Qt.Checked
                else:
                    all_checked = False
                    view_map[attr_key] = Qt.Unchecked
                idx += 1
            if all_unchecked:
                view_map[parent_node] = Qt.Unchecked
            elif all_checked:
                view_map[parent_node] = Qt.Checked
            else:
                view_map[parent_node] = Qt.PartiallyChecked
        if view_node_key:
            view_map[view_node_key] = state
            if view_node_key == 'all':
                view_map['base'] = view_map['custom'] = view_map['show_kv'] = state
        
        s = set([view_map.get('base', 3), view_map.get('custom', 3), view_map.get('show_kv', 3)]) - set([3])
        if len(s) == 1:
            view_map['all'] = s.pop()
            for key in ('base', 'custom', 'show_kv'):
                if key not in view_map:
                    view_map[key] = self.view_map.get(key, view_map['all'])
        elif len(s) == 0:
            view_map['all'] = Qt.Unchecked
            view_map['base'] = view_map['custom'] = view_map['show_kv'] = Qt.Unchecked
        else:
            view_map['all'] = Qt.PartiallyChecked
            for key in ('base', 'custom', 'show_kv'):
                if key not in view_map:
                    view_map[key] = self.view_map.get(key, view_map['all'])
        return view_map

    def show_config_panel(self):
        self.view_map = {}
        self.init_original_attr_conf()
        self.config_widget.listWidget.setCurrentRow(0)
        self.temp_attr_conf = copy.deepcopy(self.attr_conf)
        self.refresh_config_widget('creature')
        self.config_panel.show()

    def setup_main_widget(self):
        self.main_widget.pushButtonSetting_2.clicked.connect(self.show_config_panel)
        self.main_widget.pushButtonSetting.clicked.connect(self.show_config_panel)
        self.main_widget.pushButtonListAdd_3.clicked.connect(self.change_pause_state)
        self.main_widget.pushButtonClose.clicked.connect(QApplication.instance().quit)
        self.main_widget.pushButtonListStop.setEnabled(True)
        self.main_widget.pushButtonListStop.clicked.connect(lambda _:G.Helper.switch_game_or_editor_inside() or self.main_widget.pushButtonListStop.setEnabled(False))
        scrollbar = self.main_widget.treeWidget.verticalScrollBar()
        scrollbar.valueChanged.connect(self.on_attr_scrollbar_value_change)
        self.main_widget.treeWidget.itemExpanded.connect(lambda item:self.on_attr_collapsed(False, item))
        self.main_widget.treeWidget.itemCollapsed.connect(lambda item:self.on_attr_collapsed(True, item))
        self.switch_page(0)
    
    def setup_config_widget(self):
        self.config_widget.listWidget.clear()
        name_map = ('单位', '可破坏物', '物品')
        for i in xrange(3):
            self.config_widget.listWidget.addItem(name_map[i])
        for i in range(self.config_widget.listWidget.count()):
            item = QListWidgetItem(self.config_widget.listWidget.item(i))
            item.setFlags(item.flags() | Qt.ItemIsSelectable | Qt.ItemIsEditable)
            # item.clicked.connect(lambda type=name_map[i][0]:self.refresh_config_widget(type))
        self.config_widget.listWidget.itemClicked.connect(self.on_conf_list_item_click)
        self.config_widget.treeWidget.setColumnCount(2)
        self.config_widget.treeWidget.setHeaderLabels(['属性名', '是否显示'])
        
        self.config_widget.pushButtonConfirm.clicked.connect(self.save_and_refresh_conf)
        self.config_widget.pushButtonClose.clicked.connect(self.config_panel.close)
        self.config_widget.pushButtonCancel.clicked.connect(self.cancel_config)
        scrollbar = self.config_widget.treeWidget.verticalScrollBar()
        scrollbar.valueChanged.connect(self.on_scrollbar_value_change)
        self.config_widget.treeWidget.itemExpanded.connect(lambda item:self.on_conf_collapsed(False, item))
        self.config_widget.treeWidget.itemCollapsed.connect(lambda item:self.on_conf_collapsed(True, item))
        self.config_widget.treeWidget.itemClicked.connect(lambda item, col: self.on_conf_click(item, col))
        self.checkbox_style_sheet = "QCheckBox{font-size:12px;color:#D0D0D0;;background:transparent;border:none;}QCheckBox::indicator {background:transparent;border:none;border-radius:2px;image:url(:/resource/v3.0/yxsg/yxsg_zysc_checkbox_nml.png);}QCheckBox::indicator::unchecked {image:url(:/resource/v3.0/yxsg/yxsg_zysc_checkbox_nml.png);}QCheckBox::indicator:checked {image:url(:/resource/v3.0/yxsg/yxsg_common_checkbox_slc_v2.png);}QCheckBox::indicator:unchecked:disabled { image:url(:/resource/v3.0/yxsg/yxsg_zysc_checkbox_nml2.png);}QCheckBox::indicator:checked:disabled { image:url(:/resource/v3.0/yxsg/yxsg_common_checkbox_dis_dark.png);}QCheckBox::indicator:indeterminate{ image:url(:/resource/v3.0/yxsg/yxsg_common_partially_selected.png);}"
        self.lineedit_style_sheet = "QLineEdit {    background:        /*UiThemeStart[InputBG]*/        #0D0D0D;        /*UiThemeEnd*/;    border: 1px solid        /*UiThemeStart[InputBorderNml]*/        #0D0D0D;        /*UiThemeEnd*/;    color:        /*UiThemeStart[InputTxtNml]*/        #D0DADD;        /*UiThemeEnd*/;    font-size: 12px;    padding-left: 7px;    border-radius: 2px;    height:28px;}QLineEdit:hover {    border: 1px solid        /*UiThemeStart[InputBorderHover]*/        #474747;        /*UiThemeEnd*/;}QLineEdit:focus {    border:        1px solid        /*UiThemeStart[InputBorderFocus]*/        #6e54de;        /*UiThemeEnd*/;}QLineEdit:read-only,QLineEdit:read-only:hover,QLineEdit:read-only:focus {    background: transparent;    border: 1px solid        /*UiThemeStart[InputBorderDis]*/        #3E3E3E;        /*UiThemeEnd*/;}QLineEdit:disabled,QLineEdit:disabled:hover,QLineEdit:disabled:focus {    color:        /*UiThemeStart[InputTxtDis]*/        #999999;        /*UiThemeEnd*/;    background: transparent;    border: 1px solid        /*UiThemeStart[InputBorderDis]*/        #3E3E3E;        /*UiThemeEnd*/;}QLineEdit[warning=true] {    color:#FC4F4F;    border:1px solid #FC4F4F;}"

    def on_conf_click(self, item, col):
        checkbox = self.config_widget.treeWidget.itemWidget(item, 1)
        checkbox.setCheckState(Qt.Unchecked if checkbox.isChecked() else Qt.Checked)

    def save_and_refresh_conf(self):
        self.attr_conf = copy.deepcopy(self.temp_attr_conf)
        self.save_attr_conf()
        self.refresh_attr_widget(True)
        self.config_panel.close()

    def on_scrollbar_value_change(self, value):
        self.scroll_value = value

    def on_attr_scrollbar_value_change(self, value):
        self.attr_scroll_value = value
    
    def cancel_config(self):
        self.config_panel.close()
    
    def set_config_group(self, group_name, conf_type, state):
        if group_name == 'all':
            self.temp_attr_conf[conf_type].clear()
            if state == Qt.Checked:
                for attr_type, attrs in self.original_attr_conf[conf_type].items():
                    if attr_type == 'show_kv':continue
                    self.temp_attr_conf[conf_type] = self.temp_attr_conf[conf_type] | set(attrs.keys())
                self.temp_attr_conf[conf_type].add('show_kv')
        else:
            for attr_key, _ in self.original_attr_conf[conf_type][group_name].items():
                if state == Qt.Checked:
                    self.temp_attr_conf[conf_type].add(attr_key)
                else:
                    self.temp_attr_conf[conf_type].discard(attr_key)
        self.refresh_config_widget(conf_type, group_name, state)
    
    def on_conf_list_item_click(self, item):
        name_map = {
            u'单位': 'creature',
            u'可破坏物': 'destructible',
            u'物品': "item"
        }
        self.refresh_config_widget(name_map[item.text()])

    def on_text_changed(self, text, attr_key, attr_type, is_kv=False):
        if attr_type == bool:
            val = text
        else:
            val = attr_type(text)
        if is_kv:
            self.kv_record_alter[attr_key] = val
        else:
            self.recore_alter[attr_key] = val

    def apply_attr(self):
        for key, val in self.recore_alter.items():
            self.set_unit_attr(key, val)
        self.recore_alter.clear()
        for key, val in self.kv_record_alter.items():
            self.set_unit_kv(key, val)
        self.kv_record_alter.clear()

    def on_cb_state_change(self, state, conf_type, attr_key):
        if state:
            self.temp_attr_conf[conf_type].add(attr_key)
        else:
            self.temp_attr_conf[conf_type].discard(attr_key)
        self.refresh_config_widget(conf_type)
    
    def set_kv_show(self, state, conf_type, attr_key):
        if state:
            self.temp_attr_conf[conf_type].add(attr_key)
        else:
            self.temp_attr_conf[conf_type].discard(attr_key)
        self.refresh_config_widget(conf_type, 'show_kv', state)

    def change_pause_state(self):
        self.game_paused = not self.game_paused
        G.Helper.soft_pause_game(self.game_paused)
        self.main_widget.pushButtonListAdd_3.setVisible(not self.game_paused)
        self.main_widget.pushButtonListPlay.setVisible(self.game_paused)
        self.refresh_attr_widget()

    def set_pause_btn_text(self, pause_state):
        self.game_paused = pause_state
        self.main_widget.pushButtonListAdd_3.setVisible(not self.game_paused)
        self.main_widget.pushButtonListPlay.setVisible(self.game_paused)
        self.refresh_attr_widget()