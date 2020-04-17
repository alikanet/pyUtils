from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgCase(object):
	def setupUi(self, dlgCase):
		dlgCase.setObjectName("dlgCase")
		dlgCase.resize(291, 139)
		self.buttonBox = QtWidgets.QDialogButtonBox(dlgCase)
		self.buttonBox.setGeometry(QtCore.QRect(70, 100, 211, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.cbOptions = QtWidgets.QComboBox(dlgCase)
		self.cbOptions.setGeometry(QtCore.QRect(10, 10, 271, 26))
		self.cbOptions.setObjectName("cbOptions")
		self.txtInput = QtWidgets.QLineEdit(dlgCase)
		self.txtInput.setGeometry(QtCore.QRect(10, 40, 271, 21))
		self.txtInput.setObjectName("txtInput")
		self.lblResult = QtWidgets.QLabel(dlgCase)
		self.lblResult.setGeometry(QtCore.QRect(10, 70, 271, 16))
		self.lblResult.setObjectName("lblResult")

		self.retranslateUi(dlgCase)
		self.buttonBox.accepted.connect(self.convertCase)
		self.buttonBox.rejected.connect(dlgCase.reject)
		QtCore.QMetaObject.connectSlotsByName(dlgCase)

	def retranslateUi(self, dlgCase):
		_translate = QtCore.QCoreApplication.translate
		dlgCase.setWindowTitle(_translate("dlgCase", "Case Converter"))
		self.lblResult.setText(_translate("dlgCase", "Result"))

	def convertCase(self):
		print('yeah baby')


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	dlgCase = QtWidgets.QDialog()
	ui = Ui_dlgCase()
	ui.setupUi(dlgCase)
	dlgCase.show()
	sys.exit(app.exec_())

