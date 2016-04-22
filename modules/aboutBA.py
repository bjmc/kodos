# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutBA.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AboutBA(object):
    def setupUi(self, AboutBA):
        AboutBA.setObjectName(_fromUtf8("AboutBA"))
        AboutBA.resize(474, 496)
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.ColorRole(0), QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.ColorRole(1), QtGui.QColor(214, 214, 214))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.ColorRole(2), QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.ColorRole(3), QtGui.QColor(234, 234, 234))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.ColorRole(4), QtGui.QColor(107, 107, 107))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.ColorRole(5), QtGui.QColor(142, 142, 142))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.ColorRole(6), QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.ColorRole(7), QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.ColorRole(8), QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.ColorRole(9), QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.ColorRole(10), QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.ColorRole(11), QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.ColorRole(12), QtGui.QColor(0, 0, 156))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.ColorRole(13), QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.ColorRole(14), QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.ColorRole(15), QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.ColorRole(0), QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.ColorRole(1), QtGui.QColor(214, 214, 214))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.ColorRole(2), QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.ColorRole(3), QtGui.QColor(246, 246, 246))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.ColorRole(4), QtGui.QColor(107, 107, 107))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.ColorRole(5), QtGui.QColor(142, 142, 142))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.ColorRole(6), QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.ColorRole(7), QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.ColorRole(8), QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.ColorRole(9), QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.ColorRole(10), QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.ColorRole(11), QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.ColorRole(12), QtGui.QColor(0, 0, 156))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.ColorRole(13), QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.ColorRole(14), QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.ColorRole(15), QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ColorRole(0), QtGui.QColor(128, 128, 128))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ColorRole(1), QtGui.QColor(214, 214, 214))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ColorRole(2), QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ColorRole(3), QtGui.QColor(246, 246, 246))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ColorRole(4), QtGui.QColor(107, 107, 107))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ColorRole(5), QtGui.QColor(142, 142, 142))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ColorRole(6), QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ColorRole(7), QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ColorRole(8), QtGui.QColor(128, 128, 128))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ColorRole(9), QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ColorRole(10), QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ColorRole(11), QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ColorRole(12), QtGui.QColor(0, 0, 156))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ColorRole(13), QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ColorRole(14), QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ColorRole(15), QtGui.QColor(0, 0, 0))
        AboutBA.setPalette(palette)
        AboutBA.setSizeGripEnabled(True)
        self.gridlayout = QtGui.QGridLayout(AboutBA)
        self.gridlayout.setMargin(11)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
