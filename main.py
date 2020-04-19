import sys
import os
import json
import argparse
import menu as app_menu
import shell
from PyQt5 import QtGui, QtWidgets

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
	"""
	Constructor
	"""
	def __init__(self, icon, parent=None):
		# self.caller = self.open_calc
		QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
		self.setToolTip(f'VFX Pipeline Application Build - 3.2.56')

		# with open("menu.json", "r") as read_file:
		# 	data = json.load(read_file)

		menu = QtWidgets.QMenu(parent)
		self.makeMenu(app_menu.data['menu'], menu)

		self.setContextMenu(menu)
		self.activated.connect(self.onTrayIconActivated)

		# if args.quit:
		# 	sys.exit()

	"""
	When try icon gets activated 
	"""
	def onTrayIconActivated(self, reason):
		if reason == self.DoubleClick:
			self.open_calc
		if reason == self.Trigger:
			pass


	"""
	Makes the nmenu from json file
	"""
	def makeMenu(self, data, menu):
		if not data:
			return

		for item in data:
			if "type" in item and item["type"] == "separator":
				menu.addSeparator()
			elif "type" in item and item["type"] == "submenu" and "label" in item:
				smi = menu.addMenu(item["label"])
				if "icon" in item:
					smi.setIcon(QtGui.QIcon(item["icon"]))
				if "menu" in item:
					self.makeMenu(item["menu"], smi)
			elif "label" in item:
				mi = menu.addAction(item["label"])
				if "trigger" in item:
					mi.triggered.connect(item["trigger"])
				if "icon" in item:
					mi.setIcon(QtGui.QIcon(item["icon"]))
				if "shortcut" in item:
					mi.setShortcut(item["shortcut"])
				if "tooltip" in item:
					mi.setStatusTip(item["tooltip"])
				if "type" in item and item["type"] == "checkbox":
					mi.setCheckable(True)
					if "param" in item and item["param"] in shell.options:
						mi.setChecked(shell.options[item["param"]])


"""
Main entry point
"""
def main():
	my_parser = argparse.ArgumentParser(description='Lots of many things')

	my_parser.add_argument('-s','--splash', action='store_true', help='Show the splash screen')
	my_parser.add_argument('-q','--quit', action='store_true', help='Exit app on start')
	my_parser.add_argument('-i', '--icon', metavar='icon', type=str, help='Sets the app icon')

	args = my_parser.parse_args()
	appIcon = 'icon.png'

	if args.icon != None:
		appIcon = args.icon

	if args.splash:
		startText = "hello"
		with open("splash.txt", "r") as read_file:
			startText = read_file.read()
		print(startText)

	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()
	tray_icon = SystemTrayIcon(QtGui.QIcon(appIcon), w)
	tray_icon.show()
	tray_icon.showMessage('VFX Pipeline', 'Hello "Name of logged in ID')
	sys.exit(app.exec_())


"""
Check if this is being import or not
"""
if __name__ == '__main__':
    main()