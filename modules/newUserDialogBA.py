# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newUserDialogBA.ui'
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

class Ui_NewUserDialog(object):
    def setupUi(self, NewUserDialog):
        NewUserDialog.setObjectName(_fromUtf8("NewUserDialog"))
        NewUserDialog.resize(338, 326)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1), QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewUserDialog.sizePolicy().hasHeightForWidth())
        NewUserDialog.setSizePolicy(sizePolicy)
        NewUserDialog.setWindowIcon(QtGui.QPixmap(_fromUtf8("image0")))
        self.vboxlayout = QtGui.QVBoxLayout(NewUserDialog)
        self.vboxlayout.setMargin(11)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(11)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.textLabel1 = QtGui.QLabel(NewUserDialog)
        self.textLabel1.setAlignment(QtCore.Qt.AlignVCenter)
        self.textLabel1.setWordWrap(True)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.vboxlayout1.addWidget(self.textLabel1)
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(11)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.pixmapLabel2 = QtGui.QLabel(NewUserDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0), QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixmapLabel2.sizePolicy().hasHeightForWidth())
        self.pixmapLabel2.setSizePolicy(sizePolicy)
        self.pixmapLabel2.setPixmap(QtGui.QPixmap(_fromUtf8("image1")))
        self.pixmapLabel2.setScaledContents(True)
        self.pixmapLabel2.setWordWrap(False)
        self.pixmapLabel2.setObjectName(_fromUtf8("pixmapLabel2"))
        self.gridlayout.addWidget(self.pixmapLabel2, 1, 1, 1, 1)
        self.textLabel4 = QtGui.QLabel(NewUserDialog)
        self.textLabel4.setWordWrap(False)
        self.textLabel4.setObjectName(_fromUtf8("textLabel4"))
        self.gridlayout.addWidget(self.textLabel4, 1, 0, 1, 1)
        self.pixmapLabel1 = QtGui.QLabel(NewUserDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0), QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixmapLabel1.sizePolicy().hasHeightForWidth())
        self.pixmapLabel1.setSizePolicy(sizePolicy)
        self.pixmapLabel1.setPixmap(QtGui.QPixmap(_fromUtf8("image2")))
        self.pixmapLabel1.setScaledContents(True)
        self.pixmapLabel1.setWordWrap(False)
        self.pixmapLabel1.setObjectName(_fromUtf8("pixmapLabel1"))
        self.gridlayout.addWidget(self.pixmapLabel1, 0, 1, 1, 1)
        self.textLabel3 = QtGui.QLabel(NewUserDialog)
        self.textLabel3.setWordWrap(False)
        self.textLabel3.setObjectName(_fromUtf8("textLabel3"))
        self.gridlayout.addWidget(self.textLabel3, 0, 0, 1, 1)
        self.vboxlayout1.addLayout(self.gridlayout)
        self.vboxlayout.addLayout(self.vboxlayout1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(11)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        spacerItem = QtGui.QSpacerItem(241, 21, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(NewUserDialog)
        self.okButton.setDefault(True)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.hboxlayout.addWidget(self.okButton)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(NewUserDialog)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), NewUserDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(NewUserDialog)

    def retranslateUi(self, NewUserDialog):
        NewUserDialog.setWindowTitle(_translate("NewUserDialog", "Kodos new user information", None))
        self.textLabel1.setText(_translate("NewUserDialog", "<h3>Welcome to Kodos.</h3>\n"
"<p></p>\n"
"It appears that this is your first time using \n"
"Kodos - The Python Regular Expression Debugger.\n"
"<p></p>\n"
"In order to help you familiarize yourself with Kodos, you may wish to explore\n"
"the Regex Library.  Additionally, Kodos contains a Python Regex Reference Guide. \n"
"You can access these tools by clicking on the appropriate toolbar icon.", None))
        self.textLabel4.setText(_translate("NewUserDialog", "<b>Regex Reference Guide</b>", None))
        self.textLabel3.setText(_translate("NewUserDialog", "<b>Regex Library</b>", None))
        self.okButton.setText(_translate("NewUserDialog", "&OK", None))
        self.okButton.setShortcut(_translate("NewUserDialog", "Alt+O", None))

