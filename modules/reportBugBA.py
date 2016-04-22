# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reportBugBA.ui'
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

class Ui_reportBugBA(object):
    def setupUi(self, reportBugBA):
        reportBugBA.setObjectName(_fromUtf8("reportBugBA"))
        reportBugBA.resize(750, 653)
        self.gridlayout = QtGui.QGridLayout(reportBugBA)
        self.gridlayout.setMargin(11)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.submitButton = QtGui.QPushButton(reportBugBA)
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.hboxlayout.addWidget(self.submitButton)
        self.cancelButton = QtGui.QPushButton(reportBugBA)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.hboxlayout.addWidget(self.cancelButton)
        self.gridlayout.addLayout(self.hboxlayout, 3, 0, 1, 1)
