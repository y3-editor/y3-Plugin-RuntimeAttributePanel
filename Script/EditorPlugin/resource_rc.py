# -*- coding: utf-8 -*-
import os
from PyQt5 import QtCore
import G

# 兼容非游戏环境中加载资源数据
def read_file(file):
    try:
        import C_file
    except:
        p = os.path.join(G.plugin_config['root_path'], 'Resource', file)
        with open(p, 'rb') as f:
            return f.read()
    return C_file.get_res_file(file, "")


# 必须在全局且不能被销毁
qt_resource_name = read_file("pyqt/qt_resource_name")
qt_resource_data = read_file("pyqt/qt_resource_data")

qt_version = QtCore.qVersion().split('.')
if qt_version < ['5', '8', '0']:
    rcc_version = 1
    qt_resource_struct = read_file("pyqt/qt_resource_struct_v1")

else:
    rcc_version = 2
    qt_resource_struct = read_file("pyqt/qt_resource_struct_v2")


def qInitResources():
    QtCore.qRegisterResourceData(
        rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)


def qCleanupResources():
    QtCore.qUnregisterResourceData(
        rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)


qInitResources()
