import shell
import sys

data = {
	"menu":
	[
		{
			"label": 'Dev',
			"type": "submenu",
			"icon": "icons/sun-2-128.png",
			"menu":
			[
				{
					"label": "Case Converter",
					"icon": "icons/lock-128.png",
					"trigger": lambda: shell.showCaseDialog()
				},
				{
					"label": "Guid Generator",
					# "type": "checked",
					"trigger": lambda: shell.showGuidDialog()
				},
				{
					"label": "Encryption",
					# "type": "checked",
					"trigger": lambda: shell.showCaseDialog()
				},
				{
					"label": "Time Convert",
					"shortcut": "Command+Q",
					"trigger": lambda: shell.showPWDialog()
				}
			]
		},
		{
			"label": "Dock",
			"type": "submenu",
			"icon": "icons/brain-128",
			"menu": [
				{
					"label": "Add Spacer",
					"trigger": lambda: shell.exec('defaults write com.apple.dock persistent-apps -array-add \'{"tile-type"="spacer-tile";}\'; killall Dock')
				},
				{
					"label": "Recent Items",
					"type": "checkbox",
					"trigger": lambda: shell.exec('defaults write com.apple.dock persistent-others -array-add \'{"tile-data" = {"list-type" = 1;}; "tile-type" = "recents-tile";}\'; killall Dock')
				},
				{
					"label": "Active App Only",
					"type": "checkbox",
					"param": "ActiveApp",
					"trigger": lambda: shell.exec('defaults write com.apple.dock static-only -bool {{ActiveApp}}; killall Dock')
				},
				{
					"label": "Single App Mode",
					"type": "checkbox",
					"param": "SingleApp",
					"trigger": lambda: shell.exec('defaults write com.apple.dock single-app -bool {{SingleApp}}; killall Dock')
				},
				{
					"label": "Highlight Hidden Apps",
					"type": "checkbox",
					"param": "HiddenApp",
					"trigger": lambda: shell.exec('defaults write com.apple.Dock showhidden -bool {{HiddenApp}}; killall Dock')
				},
				{
					"label": "Annamation",
					"type": "submenu",
					"menu": [
						{
							"label": "Suck",
							"trigger": lambda: shell.exec('defaults write com.apple.dock mineffect -string suck; killall Dock')
						},
						{
							"label": "Genie",
							"trigger": lambda: shell.exec('defaults write com.apple.dock mineffect -string genie; killall Dock')
						},
						{
							"label": "Scale",
							"trigger": lambda: shell.exec('defaults write com.apple.dock mineffect -string scale; killall Dock')
						}
					]
				},
				{
					"type": "separator"
				},
				{
					"label": "Reset",
					"trigger": lambda: shell.exec('defaults delete com.apple.dock; killall Dock')
				},
				{
					"type": "separator"
				},
				{
					"label": "Backup"
					# "trigger": self.open_calc
						# toggleWindow();
				},
				{
					"label": "Restore"
					# "trigger": self.open_calc
						# toggleWindow();
				}
			]
		},
		{
			"label": "General System",
			"type": "submenu",
			"icon": "icons/globe-4-128.png",
			"menu": [
				{
					"label": "Show/Hide Hidden Files",
					"type": "checkbox",
					"param": "HiddenFiles",
					"trigger": lambda: shell.exec('defaults write com.apple.finder AppleShowAllFiles {{HiddenFiles}}; killall Finder')
				},
				{
					"label": "Show/Hide Desktop Icons",
					"type": "checkbox",
					"param": "DesktopIcon",
					"trigger": lambda: shell.exec('defaults write com.apple.finder CreateDesktop -bool {{DesktopIcon}}; killall Finder')
				}
			]
		},
		{
			"label": "Spotlight",
			"type": "submenu",
			"icon": "icons/error-4-128.png",
			"menu": [
				{
					"label": "Indexing On/Off",
					"type": "checkbox",
					"param": "Indexing",
					"trigger": lambda: shell.exec('echo {{pw}} | sudo -S mdutil -a -i {{Indexing}} == false ? "off" : "on"}')
				},
				{
					"label": "Re-Index Everything",
					"trigger": lambda: shell.exec('ehcho {{pw}} | sudo -S mdutil -aE')
				},
				{
					"label": "Remove the Index",
					"trigger": lambda: shell.exec('ehcho {{pw}} | sudo -S rm -rfv /.Spotlight-V100')
				}
			]
		},
		{
			"label": "Clipboard",
			"type": "submenu",
			"icon": "icons/error-4-128.png",
			"menu": [
				{
					"label": "Indexing On/Off",
					"type": "checkbox",
					"param": "ClipMon",
					"trigger": lambda: shell.ClipMonToggle('{{ClipMon}}')
				}
			]
		},
		{
			"type": "separator"
		},
		{
			"label": "Settings",
			"trigger": lambda: shell.showSettingsDialog()
		},
		{
			"label": "Exit",
			"shortcut": "Command+Q",
			"trigger": lambda: sys.exit()
		}
	]
}
