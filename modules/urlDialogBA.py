# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urlDialogBA.ui'
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

class Ui_URLDialogBA(object):
    def setupUi(self, URLDialogBA):
        URLDialogBA.setObjectName(_fromUtf8("URLDialogBA"))
        URLDialogBA.resize(443, 170)
        URLDialogBA.setWindowIcon(QtGui.QPixmap(_fromUtf8("image0")))
        URLDialogBA.setSizeGripEnabled(True)
        self.gridlayout = QtGui.QGridLayout(URLDialogBA)
        self.gridlayout.setMargin(11)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.buttonHelp = QtGui.QPushButton(URLDialogBA)
        self.buttonHelp.setAutoDefault(True)
        self.buttonHelp.setObjectName(_fromUtf8("buttonHelp"))
        self.hboxlayout.addWidget(self.buttonHelp)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.buttonOk = QtGui.QPushButton(URLDialogBA)
        self.buttonOk.setShortcut(_fromUtf8(""))
        self.buttonOk.setAutoDefault(True)
        self.buttonOk.setDefault(True)
        self.buttonOk.setObjectName(_fromUtf8("buttonOk"))
        self.hboxlayout.addWidget(self.buttonOk)
        self.buttonCancel = QtGui.QPushButton(URLDialogBA)
        self.buttonCancel.setShortcut(_fromUtf8(""))
        self.buttonCancel.setAutoDefault(True)
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.hboxlayout.addWidget(self.buttonCancel)
        self.gridlayout.addLayout(self.hboxlayout, 1, 0, 1, 1)
