class GetContent():
	def content(self):
		content = {
			'info': {
				'show_sources': ''' Sources/Inspirations

				Source of most commans: https://wiki.archlinux.org/title/Pacman/Tips_and_tricks)
				Inspiration for wildcard implementation: https://bbs.archlinux.org/viewtopic.php?id=135649)
				'''
			},
			'commands': {
				'upgrade':{
					'exec':{
						'base':'sudo pacman -Syu',
						'mods':{
							'norefresh':['y','']
						}
					}
				},
				'install':{
					'pkgs':{
						'base':'pacman -Ssq INPUT',
						'mods':{
							'wild':['INPUT','| grep INPUT']
						}
					},
					'exec':{
						'base':'sudo pacman -Sy PKGS --needed',
						'mods':{
							'force':[' --needed',''],
							'norefresh':['y','']
						}
					}
				},
				'remove':{
					'pkgs':{
						'base':'pacman -Qsq INPUT',
						'mods':{
							'wild':['sq INPUT','q | grep INPUT']
						},
					},
					'exec':{
						'base':'sudo pacman -Rs PKGS'
					}
				},
				'autoremove':{
					'cmds': {
						'pkgs':{
							'base':'pacman -Qtdq',
						},
						'exec':{
							'base':'sudo pacman -Rs PKGS'
						}
					}
				}
			}
		}
		return content

	def cfg(self):
		cfg = {
			'prefixtxt':'''After having to search for many pacman hidden functions myself, i decided to help others by giving them by giving them an easy way to use the functions i found.
If you dont trust my program want to use the functions directly instead, you more are welcome to copy the lines from here:''',
			'noreplacepkgs':{
				'install':['base','force'],
				'remove':['base']
			},
			'mods':{
				'pkgs':{
					'wild':'Wildcard'
				},
				'exec':{
					'norefresh':'Norefresh','force':'Forced'
				}
			},
			'cmdpairs':[['exec','pkgs']]
		}
		return cfg
