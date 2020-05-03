import os, sys, pickle
from clipman import ClipboardWatcher
from stringUtils import findAll, getParams
from pwDialog import Ui_Password
from guidDialog import Ui_Dialog
from caseDialog import Ui_dlgCase
from settingsDialog import Ui_SettingsDialog
from PyQt5 import QtWidgets

options = {'RecentItems': False, 'ActiveApp': False, 'SingleApp': False, 'HiddenApp': False, 'HiddenFiles': False, 'DesktopIcon': False, 'Indexing': True, 'ClipMon': False}
parent = None

"""
Show Password Dialog and return Password
"""
def convertParam(cmd):
	allStart = getParams(cmd)
	print(f'all params: {allStart}')
	for exVal in allStart:
		print(f'param got: {exVal}')
		if exVal == "pw":
			print('yes pw found')
			pw = showPWDialog()
			cmd = cmd.replace("{{pw}}", pw)
		elif exVal in options:
			optVal = not options[exVal]
			cmd = cmd.replace("{{"+exVal+"}}", str(optVal).lower())
			options[exVal] = optVal
			save()
	return cmd

"""
Show Password Dialog and return Password
"""
def exec(cmd):
	# startIndex = cmd.find("{{")
	# endIndex = cmd.find("}}")
	cmd = convertParam(cmd)

	print(f'got cmd: {cmd}')
	os.system(cmd)

	# if args.quit:
	# 	tray_icon.showPWDialog()

# def exitApp():
# 	sys.exit()

"""
Show Password Dialog and return Password
"""
def ClipMonToggle(data):
	cmd = convertParam(data)
	print(cmd)

	if cmd:
		watcher.start()
	else:
		watcher.stop()



"""
Show Password Dialog and return Password
"""
def onClipboardChange(data):
	print(data)

"""
Show Password Dialog and return Password
"""
# def startClipboardMonitor():
	# watcher = ClipboardWatcher(is_url_but_not_bitly, print_to_stdout, 5.)
	# watcher.start()
	# while True:
		# try:
		# 	print("Waiting for changed clipboard...")
		# 	time.sleep(10)
		# except KeyboardInterrupt:
		# 	watcher.stop()
		# 	break

"""
Show Password Dialog and return Password
"""
# def stopClipboardMonitor():
	# watcher = ClipboardWatcher(is_url_but_not_bitly, print_to_stdout, 5.)
	# watcher.start()
	# while True:
	# 	try:
	# 		print("Waiting for changed clipboard...")
	# 		time.sleep(10)
	# 	except KeyboardInterrupt:
	# 		break
	# watcher.stop()

"""
Show Password Dialog and return Password
"""
def showSettingsDialog():
	print(parent)
	gdialog = QtWidgets.QDialog()
	gui = Ui_SettingsDialog()
	gui.setupUi(gdialog)
	gdialog.show()
	resp = gdialog.exec_()

	return resp

"""
Show Password Dialog and return Password
"""
def showGuidDialog():
	print(parent)
	gdialog = QtWidgets.QDialog()
	gui = Ui_Dialog()
	gui.setupUi(gdialog)
	gdialog.show()
	resp = gdialog.exec_()

	return resp


"""
Show Password Dialog and return Password
"""
def showCaseDialog():
	cdialog = QtWidgets.QDialog()
	cui = Ui_dlgCase()
	cui.setupUi(cdialog)
	cdialog.show()
	resp = cdialog.exec_()

	return resp


"""
Show Password Dialog and return Password
"""
def showPWDialog():
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

watcher = ClipboardWatcher(onClipboardChange, 5.)
options = init()