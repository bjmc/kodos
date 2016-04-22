# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultsBA.ui'
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

class Ui_unnamed(object):
    def setupUi(self, Form3):
        Form3.setObjectName(_fromUtf8("Form3"))
        Form3.setGeometry(QtCore.QRect(0, 0, 715, 250))
        self.gridlayout = QtGui.QGridLayout(Form3)
        self.gridlayout.setMargin(11)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.infoTabWidget = QtGui.QTabWidget(Form3)
        self.infoTabWidget.setObjectName(_fromUtf8("infoTabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.vboxlayout = QtGui.QVBoxLayout(self.tab)
        self.vboxlayout.setMargin(11)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
