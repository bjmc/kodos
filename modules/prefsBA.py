# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prefsBA.ui'
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

class Ui_PrefsBA(object):
    def setupUi(self, PrefsBA):
        PrefsBA.setObjectName(_fromUtf8("PrefsBA"))
        PrefsBA.resize(540, 257)
        PrefsBA.setWindowIcon(QtGui.QPixmap(_fromUtf8("image0")))
        PrefsBA.setSizeGripEnabled(False)
        self.layout5 = QtGui.QWidget(PrefsBA)
        self.layout5.setGeometry(QtCore.QRect(11, 6, 519, 246))
        self.layout5.setObjectName(_fromUtf8("layout5"))
        self.vboxlayout = QtGui.QVBoxLayout(self.layout5)
        self.vboxlayout.setMargin(11)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(11)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.TextLabel2 = QtGui.QLabel(self.layout5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0), QtGui.QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextLabel2.sizePolicy().hasHeightForWidth())
        self.TextLabel2.setSizePolicy(sizePolicy)
        self.TextLabel2.setWordWrap(False)
        self.TextLabel2.setObjectName(_fromUtf8("TextLabel2"))
        self.gridlayout.addWidget(self.TextLabel2, 1, 0, 1, 1)
        self.browserButton = QtGui.QPushButton(self.layout5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0), QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browserButton.sizePolicy().hasHeightForWidth())
        self.browserButton.setSizePolicy(sizePolicy)
        self.browserButton.setObjectName(_fromUtf8("browserButton"))
        self.gridlayout.addWidget(self.browserButton, 0, 3, 1, 1)
        self.browserEdit = QtGui.QLineEdit(self.layout5)
        self.browserEdit.setObjectName(_fromUtf8("browserEdit"))
        self.gridlayout.addWidget(self.browserEdit, 0, 1, 1, 2)
        self.fontButtonMatch = QtGui.QPushButton(self.layout5)
        self.fontButtonMatch.setText(_fromUtf8(""))
        self.fontButtonMatch.setObjectName(_fromUtf8("fontButtonMatch"))
        self.gridlayout.addWidget(self.fontButtonMatch, 2, 1, 2, 3)
        self.textLabel1 = QtGui.QLabel(self.layout5)
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridlayout.addWidget(self.textLabel1, 2, 0, 1, 1)
        self.fontButton = QtGui.QPushButton(self.layout5)
        self.fontButton.setText(_fromUtf8(""))
        self.fontButton.setObjectName(_fromUtf8("fontButton"))
        self.gridlayout.addWidget(self.fontButton, 1, 1, 1, 3)
        self.emailServerEdit = QtGui.QLineEdit(self.layout5)
        self.emailServerEdit.setObjectName(_fromUtf8("emailServerEdit"))
        self.gridlayout.addWidget(self.emailServerEdit, 4, 1, 1, 3)
        self.TextLabel1_2Emaii = QtGui.QLabel(self.layout5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0), QtGui.QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextLabel1_2Emaii.sizePolicy().hasHeightForWidth())
        self.TextLabel1_2Emaii.setSizePolicy(sizePolicy)
        self.TextLabel1_2Emaii.setWordWrap(False)
        self.TextLabel1_2Emaii.setObjectName(_fromUtf8("TextLabel1_2Emaii"))
        self.gridlayout.addWidget(self.TextLabel1_2Emaii, 3, 0, 2, 1)
        self.TextLabel1_2 = QtGui.QLabel(self.layout5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0), QtGui.QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextLabel1_2.sizePolicy().hasHeightForWidth())
        self.TextLabel1_2.setSizePolicy(sizePolicy)
        self.TextLabel1_2.setWordWrap(False)
        self.TextLabel1_2.setObjectName(_fromUtf8("TextLabel1_2"))
        self.gridlayout.addWidget(self.TextLabel1_2, 5, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(380, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 5, 2, 1, 2)
        self.recentFilesSpinBox = QtGui.QSpinBox(self.layout5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0), QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recentFilesSpinBox.sizePolicy().hasHeightForWidth())
        self.recentFilesSpinBox.setSizePolicy(sizePolicy)
        self.recentFilesSpinBox.setMaximum(25)
        self.recentFilesSpinBox.setProperty("value", 5)
        self.recentFilesSpinBox.setObjectName(_fromUtf8("recentFilesSpinBox"))
        self.gridlayout.addWidget(self.recentFilesSpinBox, 5, 1, 1, 1)
        self.TextLabel1 = QtGui.QLabel(self.layout5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0), QtGui.QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextLabel1.sizePolicy().hasHeightForWidth())
        self.TextLabel1.setSizePolicy(sizePolicy)
        self.TextLabel1.setWordWrap(False)
        self.TextLabel1.setObjectName(_fromUtf8("TextLabel1"))
        self.gridlayout.addWidget(self.TextLabel1, 0, 0, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.buttonHelp = QtGui.QPushButton(self.layout5)
        self.buttonHelp.setAutoDefault(True)
        self.buttonHelp.setObjectName(_fromUtf8("buttonHelp"))
        self.hboxlayout.addWidget(self.buttonHelp)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem2)
        self.buttonApply = QtGui.QPushButton(self.layout5)
        self.buttonApply.setAutoDefault(True)
        self.buttonApply.setObjectName(_fromUtf8("buttonApply"))
        self.hboxlayout.addWidget(self.buttonApply)
        self.buttonOk = QtGui.QPushButton(self.layout5)
        self.buttonOk.setAutoDefault(True)
        self.buttonOk.setDefault(True)
        self.buttonOk.setObjectName(_fromUtf8("buttonOk"))
        self.hboxlayout.addWidget(self.buttonOk)
        self.buttonCancel = QtGui.QPushButton(self.layout5)
        self.buttonCancel.setAutoDefault(True)
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.hboxlayout.addWidget(self.buttonCancel)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(PrefsBA)
        QtCore.QObject.connect(self.buttonOk, QtCore.SIGNAL(_fromUtf8("clicked()")), PrefsBA.accept)
        QtCore.QObject.connect(self.buttonCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), PrefsBA.reject)
        QtCore.QObject.connect(self.browserButton, QtCore.SIGNAL(_fromUtf8("pressed()")), PrefsBA.browser_slot)
        QtCore.QObject.connect(self.fontButton, QtCore.SIGNAL(_fromUtf8("pressed()")), PrefsBA.font_slot)
        QtCore.QObject.connect(self.buttonHelp, QtCore.SIGNAL(_fromUtf8("pressed()")), PrefsBA.help_slot)
        QtCore.QObject.connect(self.buttonApply, QtCore.SIGNAL(_fromUtf8("pressed()")), PrefsBA.apply_slot)
        QtCore.QObject.connect(self.fontButtonMatch, QtCore.SIGNAL(_fromUtf8("pressed()")), PrefsBA.match_font_slot)
        QtCore.QMetaObject.connectSlotsByName(PrefsBA)
        PrefsBA.setTabOrder(self.browserEdit, self.browserButton)
        PrefsBA.setTabOrder(self.browserButton, self.fontButton)
        PrefsBA.setTabOrder(self.fontButton, self.emailServerEdit)
        PrefsBA.setTabOrder(self.emailServerEdit, self.recentFilesSpinBox)
        PrefsBA.setTabOrder(self.recentFilesSpinBox, self.buttonHelp)
        PrefsBA.setTabOrder(self.buttonHelp, self.buttonApply)
        PrefsBA.setTabOrder(self.buttonApply, self.buttonOk)
        PrefsBA.setTabOrder(self.buttonOk, self.buttonCancel)

    def retranslateUi(self, PrefsBA):
        PrefsBA.setWindowTitle(_translate("PrefsBA", "Preferences", None))
        self.TextLabel2.setText(_translate("PrefsBA", "Editor Font:", None))
        self.browserButton.setText(_translate("PrefsBA", "...", None))
        self.textLabel1.setText(_translate("PrefsBA", "Match Font:", None))
        self.TextLabel1_2Emaii.setText(_translate("PrefsBA", "Email Server:", None))
        self.TextLabel1_2.setText(_translate("PrefsBA", "Recent Files:", None))
        self.TextLabel1.setText(_translate("PrefsBA", "Web Browser:", None))
        self.buttonHelp.setText(_translate("PrefsBA", "&Help", None))
        self.buttonApply.setText(_translate("PrefsBA", "&Apply", None))
        self.buttonOk.setText(_translate("PrefsBA", "&OK", None))
        self.buttonCancel.setText(_translate("PrefsBA", "&Cancel", None))

