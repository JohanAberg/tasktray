# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'job_widget.ui'
#
# Created: Sat Dec 07 12:25:39 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from manifest import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(504, 64)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtGui.QFrame(Form)
        # self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setObjectName("frame")
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.label_5)
        self.horizontalLayout.addWidget(self.frame)
        self.frame1 = QtGui.QFrame(Form)
        # self.frame1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame1.setObjectName("frame1")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtGui.QLabel(self.frame1)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_6 = QtGui.QLabel(self.frame1)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_6)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.progressBar = QtGui.QProgressBar(self.frame1)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout.addWidget(self.frame1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Job:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Start:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "jobName", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "12:23:34", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Status:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

