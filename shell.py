import os, sys, pickle, pyperclip
from clipman import ClipboardWatcher
from stringUtils import findAll, getParams
from pwDialog import Ui_Password
from guidDialog import Ui_Dialog
from caseDialog import Ui_dlgCase
from settingsDialog import Ui_SettingsDialog
from PyQt5 import QtWidgets

"""
Show Password Dialog and return Password
"""
def convertParam(cmd):
	allStart = getParams(cmd)
	# print(f'all params: {allStart}')
	for exVal in allStart:
		# print(f'param got: {exVal}')
		if exVal == "pw":
			# print('yes pw found')
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
	print(f'Data: {data}')
	cmd = convertParam(data)
	print(f'Cmd: {cmd}')

	if cmd == 'true':
		print('start watcher')
		startClipboardMonitor()
	else:
		print('stop watcher')
		stopClipboardMonitor()


"""
Show Password Dialog and return Password
"""

def onClipboardChange(data):

	if options['ClipMonData']['isFirst'] == True:
		options['ClipMonData']['isFirst'] = False
	else:
		options['ClipMonData']['items'].append(f'{data} \n')
		print(data)

	save()

"""
Show Password Dialog and return Password
"""
def startClipboardMonitor():
	if options['ClipMonData']['isFirst'] == False:
		options['ClipMonData']['isFirst'] = True

	options['ClipMonData']['items'].clear()
	save()
	watcher.start()


"""
Show Password Dialog and return Password
"""
def stopClipboardMonitor():
	watcher.stop()
	pyperclip.copy(''.join(options['ClipMonData']['items']))


"""
Show Password Dialog and return Password
"""
def showSettingsDialog():
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

"""
Show Password Dialog and return Password
"""
def emptyGuid():
	pyperclip.copy('00000000-0000-0000-0000-000000000000')


def init():
	options = ''

	try:
		with open("menu_data", "rb") as pickle_in:
			options = pickle.load(pickle_in)
	except (OSError, IOError) as e:
		print(e)
		save()
		
	print(f'options 1: {options}')
	return options


def save():
	with open("menu_data", "wb") as pickle_out:
		pickle.dump(options, pickle_out)

options = {'RecentItems': False, 'ActiveApp': False, 'SingleApp': False, 'HiddenApp': False, 'HiddenFiles': False, 'DesktopIcon': False, 'Indexing': True, 'ClipMon': False, 'ClipMonData': {'isFirst': True, 'items': []}}
watcher = ClipboardWatcher(onClipboardChange, 5.)
options = init()
print(f'options 2: {options}')
