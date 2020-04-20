import uuid
import pyperclip

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(399, 88)
		self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(220, 40, 171, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.pushButton = QtWidgets.QPushButton(Dialog)
		self.pushButton.setGeometry(QtCore.QRect(10, 40, 171, 32))
		self.pushButton.setObjectName("pushButton")
		self.label = QtWidgets.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(10, 10, 371, 16))
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")

		self.retranslateUi(Dialog)
		self.buttonBox.accepted.connect(Dialog.accept)
		self.buttonBox.rejected.connect(Dialog.reject)
		self.pushButton.clicked.connect(self.generateGuid)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def generateGuid(self):
		id = uuid.uuid4()
		self.label.setText(str(id))
		pyperclip.copy(str(id))

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Guid Generator"))
		self.pushButton.setText(_translate("Dialog", "Generate Guid"))
		self.label.setText(_translate("Dialog", "TextLabel"))


# if __name__ == "__main__":
# 	import sys
# 	app = QtWidgets.QApplication(sys.argv)
# 	Dialog = QtWidgets.QDialog()
# 	ui = Ui_Dialog()
# 	ui.setupUi(Dialog)
# 	Dialog.show()
# 	sys.exit(app.exec_())

