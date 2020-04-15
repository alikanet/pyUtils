import shell
import sys

data = {
	"menu":
	[
		{
			"label": 'Dev',
			"type": "submenu",
			"icon": "icons/sun.png",
			"menu":
			[
				{
					"label": "Case Converter",
					"icon": "icons/lock-64.png",
					# "trigger": lambda: shell.exec('defaults write com.apple.finder CreateDesktop -bool false; killall Finder')
						# win.webContents.send('genGuid', { x: 470, y: 400, url: '/index.html#/case' });
				},
				{
					"label": "Guid Generator",
					"type": "checked"
					# "trigger": "lambda: self.send_command('defaults write com.apple.finder CreateDesktop -bool true; killall Finder')"
						# win.webContents.send('genGuid', { x: 470, y: 290, url: '/index.html#/guid' });
				},
				{
					"label": "Encryption",
					"type": "checked"
					# "trigger": "lambda: shell"trigger": lambda: shell.exec('defaults write com.apple.finder CreateDesktop -bool true; killall Finder')"
						# win.webContents.send('genGuid', { x: 470, y: 290, url: '/index.html#/encrypt' });
						# //						win.webContents.send('genGuid', '/index.html/#/guid');
				},
				{
					"label": "I am done",
					"shortcut": "Command+Q"
					# "trigger": "lambda: sys.exit()"
				# app.quit();n.webContents.send('genGuid', {x: 470, y: 290, url: '/index.html/#guid'});
				}
			]
		},
		{
			"label": "Dock",
			"type": "submenu",
			"icon": "icons/search",
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
			"icon": "icons/globe.png",
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
			"icon": "icons/error.png",
			"menu": [
				{
					"label": "Indexing On/Off",
					"type": "checkbox",
					"param": "Indexing",
					"trigger": lambda: shell.exec('echo {{password}} | sudo -S mdutil -a -i {{bIndexing}} == false ? "off" : "on"}')
				},
				{
					"label": "Re-Index Everything",
					"param": "Indexing",
					"trigger": lambda: shell.exec('ehcho {{password}} | sudo -S mdutil -aE')
				},
				{
					"label": "Remove the Index",
					"param": "Indexing",
					"trigger": lambda: shell.exec('ehcho {{password}} | sudo -S rm -rfv /.Spotlight-V100')
				}
			]
		},
		{
			"type": "separator"
		},
		{
			"label": "Exit",
			"shortcut": "Command+Q",
			"trigger": lambda: sys.exit()
		}
	]
}
