# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\Version2.0\05_extra\runtime_debug_tool.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RuntimeDebugToolDialog(object):
    def setupUi(self, RuntimeDebugToolDialog):
        RuntimeDebugToolDialog.setObjectName("RuntimeDebugToolDialog")
        RuntimeDebugToolDialog.resize(521, 635)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RuntimeDebugToolDialog.sizePolicy().hasHeightForWidth())
        RuntimeDebugToolDialog.setSizePolicy(sizePolicy)
        RuntimeDebugToolDialog.setMinimumSize(QtCore.QSize(521, 635))
        RuntimeDebugToolDialog.setMaximumSize(QtCore.QSize(521, 635))
        RuntimeDebugToolDialog.setStyleSheet("#RuntimeDebugToolDialog{\n"
"background:transparent;\n"
"border-top-left-radius:6px;\n"
"border-top-right-radius:6px;\n"
"border-bottom-left-radius:6px;\n"
"border-bottom-right-radius:6px;\n"
"}")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(RuntimeDebugToolDialog)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.centralWidget = QtWidgets.QWidget(RuntimeDebugToolDialog)
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
        self.label_6 = QtWidgets.QLabel(self.titleWidget)
        self.label_6.setStyleSheet("font-size: 14px;\n"
"font-weight: bold;\n"
"color:#E1E1E1;")
        self.label_6.setIndent(20)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
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
        self.widget.setMinimumSize(QtCore.QSize(0, 42))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 42))
        self.widget.setStyleSheet("#widget{\n"
"background: #232323;\n"
"}")
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButtonListPlay = QtWidgets.QPushButton(self.widget)
        self.pushButtonListPlay.setMinimumSize(QtCore.QSize(22, 22))
        self.pushButtonListPlay.setMaximumSize(QtCore.QSize(22, 22))
        self.pushButtonListPlay.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonListPlay.setStyleSheet("QPushButton{\n"
"font-size:14px;\n"
"color:#ffffff;\n"
"font-weight:bold;\n"
"background: transparent;\n"
"border:none;\n"
"image:url(:/resource/v2.0_new/ui_edit/new_icon/ui_edit_timeline_play.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #303030;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #191919;\n"
"}\n"
"")
        self.pushButtonListPlay.setText("")
        self.pushButtonListPlay.setObjectName("pushButtonListPlay")
        self.horizontalLayout_3.addWidget(self.pushButtonListPlay)
        self.pushButtonListAdd_3 = QtWidgets.QPushButton(self.widget)
        self.pushButtonListAdd_3.setMinimumSize(QtCore.QSize(22, 22))
        self.pushButtonListAdd_3.setMaximumSize(QtCore.QSize(22, 22))
        self.pushButtonListAdd_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonListAdd_3.setStyleSheet("QPushButton{\n"
"font-size:14px;\n"
"color:#ffffff;\n"
"font-weight:bold;\n"
"background: transparent;\n"
"border:none;\n"
"image:url(:/resource/v2.0_new/ui_edit/new_icon/ui_edit_timeline_pause.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #303030;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #191919;\n"
"}\n"
"")
        self.pushButtonListAdd_3.setText("")
        self.pushButtonListAdd_3.setObjectName("pushButtonListAdd_3")
        self.horizontalLayout_3.addWidget(self.pushButtonListAdd_3)
        self.pushButtonListStop = QtWidgets.QPushButton(self.widget)
        self.pushButtonListStop.setMinimumSize(QtCore.QSize(22, 22))
        self.pushButtonListStop.setMaximumSize(QtCore.QSize(22, 22))
        self.pushButtonListStop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonListStop.setStyleSheet("QPushButton{\n"
"font-size:14px;\n"
"color:#ffffff;\n"
"font-weight:bold;\n"
"background: transparent;\n"
"border:none;\n"
"image:url(:/resource/v2.0_new/object_edit/object_edit_window_stop.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #303030;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #191919;\n"
"}\n"
"")
        self.pushButtonListStop.setText("")
        self.pushButtonListStop.setObjectName("pushButtonListStop")
        self.horizontalLayout_3.addWidget(self.pushButtonListStop)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("color:#AAAAAA;\n"
"font-size:12px;")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_entity = QtWidgets.QLabel(self.widget)
        self.label_entity.setStyleSheet("color: #AD9AF9;\n"
"font-size:12px;\n"
"font-weight:bold;")
        self.label_entity.setObjectName("label_entity")
        self.horizontalLayout_3.addWidget(self.label_entity)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButtonSetting = QtWidgets.QPushButton(self.widget)
        self.pushButtonSetting.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSetting.sizePolicy().hasHeightForWidth())
        self.pushButtonSetting.setSizePolicy(sizePolicy)
        self.pushButtonSetting.setMinimumSize(QtCore.QSize(100, 32))
        self.pushButtonSetting.setMaximumSize(QtCore.QSize(100, 32))
        self.pushButtonSetting.setStyleSheet("QPushButton{\n"
"background: #6e54de;\n"
"border:none;\n"
"font-size:12px;\n"
"color:#ffffff;\n"
"border-radius:2px;\n"
"}\n"
"QPushButton:hover{\n"
"background: #7e63f1;\n"
"}\n"
"QPushButton:pressed{\n"
"background: #5844b3;\n"
"}")
        self.pushButtonSetting.setObjectName("pushButtonSetting")
        self.horizontalLayout_3.addWidget(self.pushButtonSetting)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralWidget)
        self.widget_2.setStyleSheet("#widget_2{\n"
"background:#1A1A1A;\n"
"border-bottom-left-radius:6px;\n"
"border-bottom-right-radius:6px;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setContentsMargins(0, -1, 0, 100)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(519, 100))
        self.pushButton.setMaximumSize(QtCore.QSize(519, 100))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background:transparent;\n"
"border:none;\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resource/v3.0/yxsg/plugin/icon_runing_test_plugin_check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(100, 100))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"color: #AAAAAA;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.widget_3 = QtWidgets.QWidget(self.page)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 32))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 32))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonSetting_2 = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSetting_2.sizePolicy().hasHeightForWidth())
        self.pushButtonSetting_2.setSizePolicy(sizePolicy)
        self.pushButtonSetting_2.setMinimumSize(QtCore.QSize(100, 32))
        self.pushButtonSetting_2.setMaximumSize(QtCore.QSize(100, 32))
        self.pushButtonSetting_2.setStyleSheet("QPushButton{\n"
"background: #6e54de;\n"
"border:none;\n"
"font-size:12px;\n"
"color:#ffffff;\n"
"border-radius:2px;\n"
"}\n"
"QPushButton:hover{\n"
"background: #7e63f1;\n"
"}\n"
"QPushButton:pressed{\n"
"background: #5844b3;\n"
"}")
        self.pushButtonSetting_2.setObjectName("pushButtonSetting_2")
        self.horizontalLayout_4.addWidget(self.pushButtonSetting_2)
        self.verticalLayout_3.addWidget(self.widget_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("/*以下是滑块设置*/\n"
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
        self.page_2.setObjectName("page_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.treeWidget = QtWidgets.QTreeWidget(self.page_2)
        self.treeWidget.setStyleSheet("QTreeWidget{\n"
"background:transparent;\n"
"border:none;\n"
"outline:none;\n"
"}\n"
"QTreeWidget::item{\n"
"background: transparent;\n"
"height:32px;\n"
"font-size:12px;\n"
"color: #D0D0D0;\n"
"padding: 0 12px;\n"
"margin-top:2px;\n"
"margin-bottom:2px;\n"
"}\n"
"QTreeWidget::item:hover,QTreeWidget::item:selected{\n"
"background: #333333;\n"
"}\n"
"\n"
"\n"
"QTreeWidget QLineEdit{\n"
"height:28px;\n"
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
"")
        self.treeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setIndentation(15)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setExpandsOnDoubleClick(True)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_5.addWidget(self.treeWidget)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setMaximumSize(QtCore.QSize(519, 16777215))
        self.page_3.setObjectName("page_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 100)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.icon_1 = QtWidgets.QPushButton(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_1.sizePolicy().hasHeightForWidth())
        self.icon_1.setSizePolicy(sizePolicy)
        self.icon_1.setMinimumSize(QtCore.QSize(519, 100))
        self.icon_1.setMaximumSize(QtCore.QSize(519, 100))
        self.icon_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.icon_1.setAutoFillBackground(False)
        self.icon_1.setStyleSheet("QPushButton{\n"
"background:transparent;\n"
"border:none;\n"
"}")
        self.icon_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resource/v3.0/yxsg/plugin/icon_runing_test_plugin_sx.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_1.setIcon(icon1)
        self.icon_1.setIconSize(QtCore.QSize(100, 100))
        self.icon_1.setObjectName("icon_1")
        self.verticalLayout_4.addWidget(self.icon_1)
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"color: #808080;\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout_6.addWidget(self.centralWidget)

        self.retranslateUi(RuntimeDebugToolDialog)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(RuntimeDebugToolDialog)

    def retranslateUi(self, RuntimeDebugToolDialog):
        _translate = QtCore.QCoreApplication.translate
        self.label_6.setText(_translate("RuntimeDebugToolDialog", "运行时调试工具"))
        self.label.setText(_translate("RuntimeDebugToolDialog", "已选中"))
        self.label_entity.setText(_translate("RuntimeDebugToolDialog", "name"))
        self.pushButtonSetting.setText(_translate("RuntimeDebugToolDialog", "字段配置"))
        self.label_3.setText(_translate("RuntimeDebugToolDialog", "本插件可以在Y3编辑器运行的时候，查看修改监听的数据字段"))
        self.pushButtonSetting_2.setText(_translate("RuntimeDebugToolDialog", "字段配置"))
        self.treeWidget.headerItem().setText(0, _translate("RuntimeDebugToolDialog", "1"))
        self.treeWidget.headerItem().setText(1, _translate("RuntimeDebugToolDialog", "2"))
        self.label_4.setText(_translate("RuntimeDebugToolDialog", "在编辑器中点选对象以查看其属性"))
import resource_rc
