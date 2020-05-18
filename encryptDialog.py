from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_encryptDlg(object):
    def setupUi(self, encryptDlg):
        encryptDlg.setObjectName("encryptDlg")
        encryptDlg.resize(660, 129)
        self.buttonBox = QtWidgets.QDialogButtonBox(encryptDlg)
        self.buttonBox.setGeometry(QtCore.QRect(560, 90, 81, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.txtInput = QtWidgets.QLineEdit(encryptDlg)
        self.txtInput.setGeometry(QtCore.QRect(80, 20, 411, 21))
        self.txtInput.setObjectName("txtInput")
        self.txtOutput = QtWidgets.QLineEdit(encryptDlg)
        self.txtOutput.setGeometry(QtCore.QRect(80, 60, 411, 21))
        self.txtOutput.setObjectName("txtOutput")
        self.label = QtWidgets.QLabel(encryptDlg)
        self.label.setGeometry(QtCore.QRect(20, 60, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(encryptDlg)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 41, 16))
        self.label_2.setObjectName("label_2")
        self.btnEncrypt = QtWidgets.QPushButton(encryptDlg)
        self.btnEncrypt.setGeometry(QtCore.QRect(496, 16, 80, 32))
        self.btnEncrypt.setObjectName("btnEncrypt")
        self.btnDecrypt = QtWidgets.QPushButton(encryptDlg)
        self.btnDecrypt.setGeometry(QtCore.QRect(566, 16, 80, 32))
        self.btnDecrypt.setObjectName("btnDecrypt")
        self.drpType = QtWidgets.QComboBox(encryptDlg)
        self.drpType.setGeometry(QtCore.QRect(500, 58, 141, 26))
        self.drpType.setObjectName("drpType")

        self.retranslateUi(encryptDlg)
        self.buttonBox.accepted.connect(encryptDlg.accept)
        self.buttonBox.rejected.connect(encryptDlg.reject)
        self.btnDecrypt.clicked.connect(encryptDlg.exec)
        self.btnEncrypt.clicked.connect(encryptDlg.exec)
        self.drpType.currentTextChanged['QString'].connect(encryptDlg.exec)
        QtCore.QMetaObject.connectSlotsByName(encryptDlg)

    def retranslateUi(self, encryptDlg):
        _translate = QtCore.QCoreApplication.translate
        encryptDlg.setWindowTitle(_translate("encryptDlg", "Encryption"))
        self.label.setText(_translate("encryptDlg", "Output"))
        self.label_2.setText(_translate("encryptDlg", "Input"))
        self.btnEncrypt.setText(_translate("encryptDlg", "Encrypt"))
        self.btnDecrypt.setText(_translate("encryptDlg", "Decrypt"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     encryptDlg = QtWidgets.QDialog()
#     ui = Ui_encryptDlg()
#     ui.setupUi(encryptDlg)
#     encryptDlg.show()
#     sys.exit(app.exec_())
