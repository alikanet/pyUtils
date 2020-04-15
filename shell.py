import os
import pickle
import sys

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


def init():
	with open("menu_data", "rb") as pickle_in:
		options = pickle.load(pickle_in)

	print(f'options 2: {options}')
	return options


def save():
	with open("menu_data", "wb") as pickle_out:
		pickle.dump(options, pickle_out)

options = init()