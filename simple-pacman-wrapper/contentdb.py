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
				'dont_parse_get':{'get':True,'force':True},
				'get':'pacman -Ssq INPUT',
				'wild':'pacman -Ssq | grep INPUT',
				'exec':'sudo pacman -Sy PKGS --needed',
				'force':'sudo pacman -Sy PKGS'
			},
			'remove':{
				'input':True,
				'dont_parse_get':{'get':True},
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
		print(k,v)
		__addtocmdinfo('\n\n' + k.upper())
		for l, m in {'get':'Basic: ','wild':'Wildcard: ','force':'Forced: '}.items():
			print(k,l, m)
			if l in v:
				if l == 'force':
					basecmd = str(v['force'])
				else:
					basecmd = str(v['exec'])
				if 'dont_parse_get' in l:
					if l in v['dont_parse_get']:
						cmd = basecmd.replace('PKGS', 'INPUT')
				else:
					cmd = basecmd.replace('PKGS', '$(' + v[l] + ')')
				print('Adding' + cmd)
				__addtocmdinfo( '\n' + m + cmd)

		if 'wild' in v and 'force' in v:
			print('wild+force')
			basecmd = str(v['force'])
			if 'dont_parse_get' in v:
				if 'wild' in v['dont_parse_get']:
					cmd = basecmd.replace('PKGS', 'INPUT')
			else:
				cmd = basecmd.replace('PKGS', '$(' + v['wild'] + ')')
			__addtocmdinfo( '\nForce+Wildcard: ' + cmd)
	print(content['info']['show_commands'])
	sys.exit()
	return content
