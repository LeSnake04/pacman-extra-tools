#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def getContent():
	content = {
		'info': {
			'show_sources': ''' Sources/Inspirations

			Source of most commans: https://wiki.archlinux.org/title/Pacman/Tips_and_tricks)
			Inspiration for wildcard implementation: https://bbs.archlinux.org/viewtopic.php?id=135649)
			'''
		},
		'commands': {
			# syntax: 'ID',['Pkglistcommand','Command']
			'upgrade':{
				'exec':'sudo pacman -Syu'
			},
			'install':{
				'input':True,
				'showexec':{'get':True,'force':True},
				'get':'pacman -Ssq INPUT',
				'wild':'pacman -Ssq | grep INPUT',
				'exec':'sudo pacman -Sy PKGS --needed',
				'force':'sudo pacman -Sy PKGS'
			},
			'remove':{
				'input':True,
				'showexec':{'get':True},
				'get':'pacman -Qsq INPUT',
				'wild':'pacman -Qq | grep INPUT',
				'exec':'sudo pacman -Rs PKGS'
			},
			'autoremove':{
				'get':'pacman -Qtdq',
				'exec':'sudo pacman -Rs PKGS'
			}
		}
	}
	
	
	content['info']['show_commands'] = '''
After having to search for many pacman hidden functions myself, i decided to help others by giving them by giving them an easy way to use the functions i found.
If you dont trust my program want to use the functions directly instead, you more are welcome to copy the lines from here:'''

	"""
	Parse commandlist by goint through commands one by one,
	"""
	def __addtocmdinfo(text:str):
		content['info']['show_commands'] += text
	for k, v in content['commands'].items():
		basecmd = str(v['exec'])
		__addtocmdinfo('\n\n' + k.upper())
		if 'get' in v or 'wild' in v or 'force' in v:
			if 'get' in v:
				getcmd = str(v['get'])
				if 'showexec' in v:
					if 'get' in v['showexec']:
						cmd = basecmd.replace('PKGS', 'INPUT')
				else:
					cmd = basecmd.replace('PKGS', '$(' + getcmd + ')')
			if 'wild' in v or 'force' in v:
				__addtocmdinfo( '\n' + 'Basic: ' + cmd)
				if 'wild' in v:
					if 'showexec' in v:
						wildcmd =  str(v['wild'])
						if 'wild' in v['showexec']:
							cmd = basecmd.replace('PKGS', 'INPUT')
						else:
							cmd = basecmd.replace('PKGS', '$(' + wildcmd + ')')
					__addtocmdinfo('\n' + 'Wildcard: ' + cmd)
				if 'force' in v:
					forcecmd = str(v['force'])
					if 'showexec' in v:
						if v['showexec']['force']:
							cmd = forcecmd.replace('PKGS', 'INPUT')
					else:
						cmd = forcecmd.replace('PKGS', '$(' + getcmd + ')')
					__addtocmdinfo( '\n' + 'Force: ' + cmd)
				if 'wild' in v and 'force' in v:
					if 'showexec' in v:
						if 'wild' in v['showexec']:
							print('f+w: wild')
							cmd = forcecmd.replace('PKGS', 'INPUT')
					else:
						print('f+w: else')
						cmd = forcecmd.replace('PKGS', '$(' + v['wild'] + ')')
					__addtocmdinfo( '\n' + 'Force+Wildcard: ' + cmd)
			else:
				__addtocmdinfo( '\n' + basecmd)

	print(content['info']['show_commands'])
	sys.exit()
	return content
