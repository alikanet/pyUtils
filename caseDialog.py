import stringcase, pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgCase(object):
	def setupUi(self, dlgCase):
		dlgCase.setObjectName("dlgCase")
		dlgCase.resize(310, 140)
		self.buttonBox = QtWidgets.QDialogButtonBox(dlgCase)
		self.buttonBox.setGeometry(QtCore.QRect(210, 100, 71, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.cbOptions = QtWidgets.QComboBox(dlgCase)
		self.cbOptions.setGeometry(QtCore.QRect(8, 10, 288, 26))
		self.cbOptions.setObjectName("cbOptions")
		self.txtInput = QtWidgets.QLineEdit(dlgCase)
		self.txtInput.setGeometry(QtCore.QRect(15, 40, 271, 26))
		self.txtInput.setObjectName("txtInput")
		self.lblResult = QtWidgets.QLabel(dlgCase)
		self.lblResult.setGeometry(QtCore.QRect(15, 70, 271, 26))
		self.lblResult.setObjectName('lblResult')

		self.retranslateUi(dlgCase)
		self.buttonBox.accepted.connect(dlgCase.accept)
		QtCore.QMetaObject.connectSlotsByName(dlgCase)
		self.cbOptions.currentTextChanged.connect(self.convertCase)


	def retranslateUi(self, dlgCase):
		_translate = QtCore.QCoreApplication.translate
		dlgCase.setWindowTitle(_translate("dlgCase", "Case Converter"))
		self.lblResult.setText(_translate("dlgCase", 'Result'))
		self.txtInput.setText(_translate("dlgCase", pyperclip.paste()))
		self.cbOptions.addItems(['Camel Case','Capital Case','Const Case','Lower Case','Pascal Case','Path Case','Sentence Case','Snake Case','Spinal Case','Title Case','Trim Case','Upper Case','Alpha Num Case'])

	def convertCase(self, data):
		txt = self.txtInput.text()
		result = txt;

		if data == 'Alpha Num Case':
			result = stringcase.alphanumcase(txt)
		if data == 'Camel Case':
			result = stringcase.camelcase(txt)
		if data == 'Capital Case':
			result = stringcase.capitalcase(txt)
		if data == 'Const Case':
			result = stringcase.constcase(txt)
		if data == 'Lower Case':
			result = stringcase.lowercase(txt)
		if data == 'Pascal Case':
			result = stringcase.pascalcase(txt)
		if data == 'Path Case':
			result = stringcase.pathcase(txt)
		if data == 'Sentence Case':
			result = stringcase.sentencecase(txt)
		if data == 'Snake Case':
			result = stringcase.snakecase(txt)
		if data == 'Spinal Case':
			result = stringcase.spinalcase(txt)
		if data == 'Title Case':
			result = stringcase.titlecase(txt)
		if data == 'Trim Case':
			result = stringcase.trimcase(txt)
		if data == 'Upper Case':
			result = stringcase.uppercase(txt)

		self.lblResult.setText(result)
		pyperclip.copy(result)





# if __name__ == "__main__":
	# import sys
	# app = QtWidgets.QApplication(sys.argv)
	# dlgCase = QtWidgets.QDialog()
	# ui = Ui_dlgCase()
	# ui.setupUi(dlgCase)
	# dlgCase.show()
	# sys.exit(app.exec_())

