import uuid, pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(415, 95)
		self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(300, 40, 91, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.pushButton = QtWidgets.QPushButton(Dialog)
		self.pushButton.setGeometry(QtCore.QRect(110, 40, 151, 32))
		self.pushButton.setObjectName("pushButton")
		self.label = QtWidgets.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(10, 10, 371, 16))
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.cbURN = QtWidgets.QCheckBox(Dialog)
		self.cbURN.setGeometry(QtCore.QRect(10, 40, 87, 20))
		self.cbURN.setObjectName("cbURN")
		self.cbInQuotes = QtWidgets.QCheckBox(Dialog)
		self.cbInQuotes.setGeometry(QtCore.QRect(10, 60, 87, 20))
		self.cbInQuotes.setObjectName("cbInQuotes")

		self.retranslateUi(Dialog)
		self.buttonBox.accepted.connect(Dialog.accept)
		self.buttonBox.rejected.connect(Dialog.reject)
		self.pushButton.clicked.connect(self.generateGuid)
		# self.cbInQuotes.stateChanged['int'].connect(Dialog.exec)
		# self.cbURN.stateChanged['int'].connect(Dialog.exec)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def generateGuid(self):
		id = uuid.uuid4()
		self.label.setText(str(id))

		txt = str(id)
		if self.cbURN.isChecked():
			txt = id.urn
		if self.cbInQuotes.isChecked():
			txt = f'"{txt}"'

		pyperclip.copy(txt)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Guid Generator"))
		self.pushButton.setText(_translate("Dialog", "Generate Guid"))
		self.label.setText(_translate("Dialog", "00000000-0000-0000-0000-000000000000"))
		self.cbURN.setText(_translate("Dialog", "As URN"))
		self.cbInQuotes.setText(_translate("Dialog", "In Quotes"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
