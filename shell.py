import os
import pickle
import sys
from pwDialog import Ui_Password
from PyQt5 import QtWidgets

options = { 'RecentItems': False, 'ActiveApp': False, 'SingleApp': False, 'HiddenApp': False, 'HiddenFiles': False, 'DesktopIcon': False, 'Indexing': True }

def exec(cmd):
	startIndex = cmd.find("{{")
	endIndex = cmd.find("}}")

	startIndex = startIndex + 2 if startIndex != -1 else startIndex
	if startIndex != -1 and endIndex != -1:
		exVal = cmd[startIndex:endIndex]
		if exVal in options:
			optVal = not options[exVal]
			cmd = cmd.replace("{{"+exVal+"}}", str(optVal).lower())
			options[exVal] = optVal
			save()

	print(f'got cmd: {cmd}')
	os.system(cmd)

	# if args.quit:
	# 	tray_icon.showPWDialog()


"""
Show Password Dialog and return Password
"""
def showPWDialog(self):
	dialog = QtWidgets.QDialog()
	ui = Ui_Password()
	ui.setupUi(dialog)
	dialog.show()
	resp = dialog.exec_()

	if resp == QtWidgets.QDialog.Accepted:
		return ui.getPassword()
	else:
		return ''


def init():
	with open("menu_data", "rb") as pickle_in:
		options = pickle.load(pickle_in)

	print(f'options 2: {options}')
	return options


def save():
	with open("menu_data", "wb") as pickle_out:
		pickle.dump(options, pickle_out)

options = init()