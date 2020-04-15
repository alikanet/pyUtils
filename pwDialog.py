from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Password(object):
    def setupUi(self, Password):
        Password.setObjectName("Password")
        Password.resize(250, 101)
        self.label = QtWidgets.QLabel(Password)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Password)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 226, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.buttonBox = QtWidgets.QDialogButtonBox(Password)
        self.buttonBox.setGeometry(QtCore.QRect(70, 60, 171, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Password)
        QtCore.QMetaObject.connectSlotsByName(Password)

    def retranslateUi(self, Password):
        _translate = QtCore.QCoreApplication.translate
        Password.setWindowTitle(_translate("Password", "Dialog"))
        self.label.setText(_translate("Password", "Password:"))

