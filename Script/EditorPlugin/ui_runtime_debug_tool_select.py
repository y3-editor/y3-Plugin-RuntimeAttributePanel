# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\Version2.0\05_extra\runtime_debug_tool_select.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RuntimeDebugToolSelectDialog(object):
    def setupUi(self, RuntimeDebugToolSelectDialog):
        RuntimeDebugToolSelectDialog.setObjectName("RuntimeDebugToolSelectDialog")
        RuntimeDebugToolSelectDialog.resize(521, 635)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RuntimeDebugToolSelectDialog.sizePolicy().hasHeightForWidth())
        RuntimeDebugToolSelectDialog.setSizePolicy(sizePolicy)
        RuntimeDebugToolSelectDialog.setMinimumSize(QtCore.QSize(521, 635))
        RuntimeDebugToolSelectDialog.setMaximumSize(QtCore.QSize(521, 635))
        RuntimeDebugToolSelectDialog.setStyleSheet("#RuntimeDebugToolSelectDialog{\n"
"background:transparent;\n"
"border-top-left-radius:6px;\n"
"border-top-right-radius:6px;\n"
"border-bottom-left-radius:6px;\n"
"border-bottom-right-radius:6px;\n"
"}")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(RuntimeDebugToolSelectDialog)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.centralWidget = QtWidgets.QWidget(RuntimeDebugToolSelectDialog)
        self.centralWidget.setMouseTracking(True)
        self.centralWidget.setStyleSheet("#centralWidget{\n"
"border:1px solid #4d4d4d;\n"
"border-top-left-radius:6px;\n"
"border-top-right-radius:6px;\n"
"border-bottom-left-radius:6px;\n"
"border-bottom-right-radius:6px;\n"
"background:#080808;\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical{border:none;width:16px;background-color:transparent;padding-top:16px;padding-bottom:16px;border-radius:2px;margin:0 4px;}\n"
"QScrollBar:vertical:hover{border-radius:2px;}\n"
"QScrollBar::handle:vertical{\n"
"background: #ededed;\n"
"width:4px;\n"
"border-radius:2px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{background:#e6e6e6;}\n"
"QScrollBar::add-line:vertical,QScrollBar::sub-line:vertical{height:0px;width:0px;background-color:rgba(0,0,0,0);}\n"
"QScrollBar:horizontal{border:none;height:16px;background-color:transparent;padding-left:16px;padding-right:16px;border-radius:2px;margin:4 0px;}\n"
"QScrollBar:horizontal:hover{border-radius:2px;}\n"
"QScrollBar::handle:horizontal{background:#ededed;height:4px;border-radius:2px;}\n"
"QScrollBar::handle:horizontal:hover{background:#e6e6e6;}\n"
"QScrollBar::add-line:horizontal,QScrollBar::sub-line:horizontal{height:0px;width:0px;background-color:rgba(0,0,0,0);}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"\n"
"")
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleWidget = QtWidgets.QWidget(self.centralWidget)
        self.titleWidget.setMinimumSize(QtCore.QSize(0, 32))
        self.titleWidget.setMaximumSize(QtCore.QSize(16777215, 32))
        self.titleWidget.setStyleSheet("#titleWidget{\n"
"background: #232323;\n"
"\n"
"border:none;\n"
"border-top-left-radius:6px;\n"
"border-top-right-radius:6px;\n"
"}")
        self.titleWidget.setObjectName("titleWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.titleWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.titleWidget)
        self.label.setStyleSheet("font-size: 14px;\n"
"font-weight: bold;\n"
"color:#E1E1E1;")
        self.label.setIndent(20)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonClose = QtWidgets.QPushButton(self.titleWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonClose.sizePolicy().hasHeightForWidth())
        self.pushButtonClose.setSizePolicy(sizePolicy)
        self.pushButtonClose.setMinimumSize(QtCore.QSize(56, 32))
        self.pushButtonClose.setMaximumSize(QtCore.QSize(56, 32))
        self.pushButtonClose.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonClose.setStyleSheet("QPushButton{\n"
"border:none;\n"
"image:url(:/resource/v3.0/dark/common/dark_popup_close_nml.png);\n"
"min-width:56px;\n"
"min-height:32px;\n"
"max-width:56px;\n"
"max-height:32px;\n"
"border-top-right-radius:6px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"image:url(:/resource/v3.0/dark/common/dark_popup_close_hover.png);\n"
"background-color:#FF3D3D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"image:url(:/resource/v3.0/dark/common/dark_popup_close_dwn.png);\n"
"}")
        self.pushButtonClose.setText("")
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.horizontalLayout.addWidget(self.pushButtonClose)
        self.verticalLayout.addWidget(self.titleWidget)
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_left = QtWidgets.QWidget(self.widget)
        self.widget_left.setMinimumSize(QtCore.QSize(150, 0))
        self.widget_left.setMaximumSize(QtCore.QSize(150, 16777215))
        self.widget_left.setStyleSheet("#widget_left{\n"
"background: #232323;\n"
"}\n"
"\n"
"/*以下是滑块设置*/\n"
"QScrollBar:vertical{\n"
"background:#1F1F1F;\n"
"border:none;width:8px;padding-top:0px;padding-bottom:0px;border-radius:2px;margin:0px 0px 0px 0px;}\n"
"QScrollBar:vertical:hover{\n"
"background:#1F1F1F;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"background:#404040;\n"
"width:8px;border-radius:2px;}\n"
"QScrollBar::handle:vertical:hover{\n"
"background:#6b6b6b;\n"
"}\n"
"QScrollBar::add-line:vertical,QScrollBar::sub-line:vertical{height:0px;width:0px;background-color:#e0e0e0;}\n"
"QScrollBar:horizontal{background:#31383D;border:none;height:8px;padding-left:0px;padding-right:0px;border-radius:2px;margin:0px 0px 0px 0px;}\n"
"QScrollBar:horizontal:hover{background:#31383D;}\n"
"QScrollBar::handle:horizontal{background:#495257;height:8px;border-radius:2px;}\n"
"QScrollBar::handle:horizontal:hover{background:#5C666C;}\n"
"QScrollBar::add-line:horizontal,QScrollBar::sub-line:horizontal{height:0px;width:0px;background-color:rgba(0,0,0,0);}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background:none;}")
        self.widget_left.setObjectName("widget_left")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_left)
        self.verticalLayout_3.setContentsMargins(12, 2, 12, 12)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.widget_left)
        self.listWidget.setStyleSheet("QListWidget{\n"
"background: transparent;\n"
"border:none;\n"
"outline:none;\n"
"padding-top:10px;\n"
"border-bottom-left-radius:6px;\n"
"}\n"
"QListWidget::item{\n"
"height:32px;\n"
"color: #D0D0D0;\n"
"font-size:12px;\n"
"margin-left:0px;\n"
"margin-right:0px;\n"
"padding-left:10px;\n"
"border-radius: 2px;\n"
"}\n"
"QListWidget::item:hover{\n"
"background: #333333;\n"
"}\n"
"QListWidget::item:selected{\n"
"background: #6e54de;\n"
"color:#ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"/*以下是滑块设置*/\n"
"QScrollBar:vertical{\n"
"background:#1F1F1F;\n"
"border:none;width:8px;padding-top:0px;padding-bottom:0px;border-radius:2px;margin:0px 0px 0px 0px;}\n"
"QScrollBar:vertical:hover{\n"
"background:#1F1F1F;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"background:#404040;\n"
"width:8px;border-radius:2px;}\n"
"QScrollBar::handle:vertical:hover{\n"
"background:#6b6b6b;\n"
"}\n"
"QScrollBar::add-line:vertical,QScrollBar::sub-line:vertical{height:0px;width:0px;background-color:#e0e0e0;}\n"
"QScrollBar:horizontal{background:#31383D;border:none;height:8px;padding-left:0px;padding-right:0px;border-radius:2px;margin:0px 0px 0px 0px;}\n"
"QScrollBar:horizontal:hover{background:#31383D;}\n"
"QScrollBar::handle:horizontal{background:#495257;height:8px;border-radius:2px;}\n"
"QScrollBar::handle:horizontal:hover{background:#5C666C;}\n"
"QScrollBar::add-line:horizontal,QScrollBar::sub-line:horizontal{height:0px;width:0px;background-color:rgba(0,0,0,0);}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background:none;}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout_3.addWidget(self.listWidget)
        self.horizontalLayout_4.addWidget(self.widget_left)
        self.widget_right = QtWidgets.QWidget(self.widget)
        self.widget_right.setStyleSheet("#widget_right{\n"
"background: #191919;\n"
"}\n"
"\n"
"\n"
"/*以下是滑块设置*/\n"
"QScrollBar:vertical{\n"
"background:#1F1F1F;\n"
"border:none;width:8px;padding-top:0px;padding-bottom:0px;border-radius:2px;margin:0px 0px 0px 0px;}\n"
"QScrollBar:vertical:hover{\n"
"background:#1F1F1F;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"background:#404040;\n"
"width:8px;border-radius:2px;}\n"
"QScrollBar::handle:vertical:hover{\n"
"background:#6b6b6b;\n"
"}\n"
"QScrollBar::add-line:vertical,QScrollBar::sub-line:vertical{height:0px;width:0px;background-color:#e0e0e0;}\n"
"QScrollBar:horizontal{background:#31383D;border:none;height:8px;padding-left:0px;padding-right:0px;border-radius:2px;margin:0px 0px 0px 0px;}\n"
"QScrollBar:horizontal:hover{background:#31383D;}\n"
"QScrollBar::handle:horizontal{background:#495257;height:8px;border-radius:2px;}\n"
"QScrollBar::handle:horizontal:hover{background:#5C666C;}\n"
"QScrollBar::add-line:horizontal,QScrollBar::sub-line:horizontal{height:0px;width:0px;background-color:rgba(0,0,0,0);}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background:none;}")
        self.widget_right.setObjectName("widget_right")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_right)
        self.verticalLayout_4.setContentsMargins(0, 0, 6, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.treeWidget = QtWidgets.QTreeWidget(self.widget_right)
        self.treeWidget.setStyleSheet("QTreeWidget{\n"
"background:transparent;\n"
"border:none;\n"
"outline:none;\n"
"}\n"
"QTreeWidget::item{\n"
"background: transparent;\n"
"height:36px;\n"
"font-size:12px;\n"
"color: #D0D0D0;\n"
"padding: 0 12px;\n"
"}\n"
"QTreeWidget::item:hover,QTreeWidget::item:selected{\n"
"background: #333333;\n"
"}\n"
"\n"
"\n"
"\n"
"QTreeWidget::indicator {\n"
"background-color: #dddddd;\n"
"border:none;\n"
"image: url(:/resource/v2.0_new/mainwindow/common/common_checkbox_nml.png);\n"
"}\n"
"\n"
"QTreeWidget::indicator:hover {\n"
"image:  url(:/resource/v2.0_new/mainwindow/common/common_checkbox_hover.png);\n"
"}\n"
"\n"
"QTreeWidget::indicator::unchecked {\n"
"image: url(:/resource/v2.0_new/mainwindow/common/common_checkbox_nml.png);\n"
"}\n"
"\n"
"QTreeWidget::indicator::checked { \n"
"image: url(:/resource/v2.0_new/mainwindow/common/common_checkbox_slc_v2.png);\n"
"}\n"
"\n"
"QTreeWidget::indicator::disabled { \n"
"image: url(:/resource/v2.0_new/mainwindow/common/common_checkbox_dis.png);\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:closed:has-children:!has-siblings,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    border-image: none;\n"
"    image: url(:/resource/v2.0_new/mainwindow/common/branch_close.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings {\n"
"    border-image: none;\n"
"    image: url(:/resource/v2.0_new/mainwindow/common/branch_open.png);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.treeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setIndentation(15)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setExpandsOnDoubleClick(True)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setCheckState(1, QtCore.Qt.Checked)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.verticalLayout_4.addWidget(self.treeWidget)
        self.horizontalLayout_4.addWidget(self.widget_right)
        self.verticalLayout.addWidget(self.widget)
        self.widgetToolContainer = QtWidgets.QWidget(self.centralWidget)
        self.widgetToolContainer.setMinimumSize(QtCore.QSize(0, 60))
        self.widgetToolContainer.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widgetToolContainer.setStyleSheet("#widgetToolContainer{\n"
"background: #232323;\n"
"}")
        self.widgetToolContainer.setObjectName("widgetToolContainer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widgetToolContainer)
        self.horizontalLayout_3.setContentsMargins(0, 10, 10, 10)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButtonConfirm = QtWidgets.QPushButton(self.widgetToolContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonConfirm.sizePolicy().hasHeightForWidth())
        self.pushButtonConfirm.setSizePolicy(sizePolicy)
        self.pushButtonConfirm.setMinimumSize(QtCore.QSize(100, 32))
        self.pushButtonConfirm.setMaximumSize(QtCore.QSize(100, 32))
        self.pushButtonConfirm.setStyleSheet("QPushButton{\n"
"background: #6e54de;\n"
"border:transparent;\n"
"font-size:12px;\n"
"color:#ffffff;\n"
"border-radius:2px;\n"
"}\n"
"QPushButton:hover{\n"
"background: #7e63f1;\n"
"color:#ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"background: #5844b3;\n"
"color:#ffffff;\n"
"}")
        self.pushButtonConfirm.setObjectName("pushButtonConfirm")
        self.horizontalLayout_3.addWidget(self.pushButtonConfirm)
        self.pushButtonCancel = QtWidgets.QPushButton(self.widgetToolContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCancel.sizePolicy().hasHeightForWidth())
        self.pushButtonCancel.setSizePolicy(sizePolicy)
        self.pushButtonCancel.setMinimumSize(QtCore.QSize(100, 32))
        self.pushButtonCancel.setMaximumSize(QtCore.QSize(100, 32))
        self.pushButtonCancel.setStyleSheet("QPushButton{\n"
"background: #4d418c;\n"
"border:transparent;\n"
"font-size:12px;\n"
"color:#ffffff;\n"
"border-radius:2px;\n"
"}\n"
"QPushButton:hover{\n"
"background: #6958bf;\n"
"color:#ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"background: #3f3573;\n"
"color:#ffffff;\n"
"}")
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_3.addWidget(self.pushButtonCancel)
        self.verticalLayout.addWidget(self.widgetToolContainer)
        self.horizontalLayout_2.addWidget(self.centralWidget)

        self.retranslateUi(RuntimeDebugToolSelectDialog)
        QtCore.QMetaObject.connectSlotsByName(RuntimeDebugToolSelectDialog)

    def retranslateUi(self, RuntimeDebugToolSelectDialog):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("RuntimeDebugToolSelectDialog", "字段配置"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("RuntimeDebugToolSelectDialog", "New Item"))
        item = self.listWidget.item(1)
        item.setText(_translate("RuntimeDebugToolSelectDialog", "New Item"))
        item = self.listWidget.item(2)
        item.setText(_translate("RuntimeDebugToolSelectDialog", "New Item"))
        item = self.listWidget.item(3)
        item.setText(_translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget.headerItem().setText(0, _translate("RuntimeDebugToolSelectDialog", "1"))
        self.treeWidget.headerItem().setText(1, _translate("RuntimeDebugToolSelectDialog", "2"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(5).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(6).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(7).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(8).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(9).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(10).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(11).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(12).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(13).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(14).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(15).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(16).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(17).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(18).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(19).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(20).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(21).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(22).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.topLevelItem(23).setText(0, _translate("RuntimeDebugToolSelectDialog", "New Item"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButtonConfirm.setText(_translate("RuntimeDebugToolSelectDialog", "Confirm"))
        self.pushButtonCancel.setText(_translate("RuntimeDebugToolSelectDialog", "Cancel"))
import resource_rc
