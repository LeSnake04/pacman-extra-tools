#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
import subprocess as sp
from argcomplete import autocomplete


from log import Log
from contentdb import getContent


class Spm():
	def __init__(self):
		# Defining arguments
		parser = ArgumentParser(description='Simple, yet powerfull pacman wrapper', epilog=' [*]Supports wildcard input [#]updates Package database [x]Exits Program')
		parser.add_argument('-v', '--verbose', action ='store_true', help='Increase output verbosity')
		parser.add_argument('-w', '--wildcard', action='store_true', help='Enable wildcard for supported commands')
		parser.add_argument('-f', '--force', action='store_true', help='')

		generalag = parser.add_argument_group('Genaral', 'General Package Management')
		generalag.add_argument('-i', '--install', nargs='+', type=str, help='Install programs [*#]')
		generalag.add_argument('-I', '--force-install', nargs='+', type=str, help='Install programs - Reinstall if already installed [*#]')
		generalag.add_argument('-r', '--remove', nargs='+', type=str, help='Remove programs [*]')
		generalag.add_argument('-a', '--autoremove', action='store_true', help='Remove unsed programs')
		generalag.add_argument('-u', '--upgrade', action='store_true', help='Perform system upgrade [#]')

		infoag = parser.add_argument_group('Info', 'Informations about the Program')
		infoag.add_argument('--show-commands', action='store_true', help='Show pacman commands used by the program [x]')
		infoag.add_argument('--show-sources', action='store_true', help='Show the sources of the commands [x]')

		debuggingag = parser.add_argument_group('Debugging', 'Options for development purposes')
		debuggingag.add_argument('--loglevel', choices = Log.loglevelids(Log), default='info', help='Set loglevel (default:info)')
		debuggingag.add_argument('-D', '--debug', action='store_true', help='Set Loglevel to \"debug\"')
		debuggingag.add_argument('--traceback', action='store_true', help='Enable traceback before logging entrys')
		debuggingag.add_argument('--tracebacklimit', type=int, help='Set limit for traceback')

		autocomplete(parser)
		args = parser.parse_args()
		argsdict = args.__dict__

		# Starting loggers
		if args.verbose:
			args.loglevel = 'verbose'
		self.loglevel = args.loglevel
		pal = Log(args.loglevel, 'PARSEARGS')
		gcl = Log(args.loglevel, 'GETCONTENT')
		pcl = Log(args.loglevel, 'PARSECONTENT')

		pal.debug(argsdict)

		gcl.advanced('Getting content')
		# Getting content
		contentdict = getContent()
		# gcl.debug('Contentdict: ' + str(contentdict))
		infodict = contentdict['info']
		# gcl.debug('Infodict: ' + str(infodict))
		commandsdict = contentdict['commands']
		# gcl.debug('Commandsdict: ' + str(commandsdict))

		# check Which Infos should be displayed
		for k, v in infodict.items():
			pal.advanced('INFO: checking for arg ' + k)
			if argsdict[k]:
				pal.verbose('Printing info for ' + k)
				print(v)

		# check which Commands should be executed
		for k, v in commandsdict.items():
			pal.advanced('COMMANDS: checking for arg ' + k)

			# if argument detected for commands
			if argsdict[k]:
				cmd = v[1]
				# Detect if command needs to parse pkglist
				if 'get' in v:
					pkgscmdorig = commandsdict[k][0]
					# Give user input to commandsting
					if 'input' in v:
						pkginputs = ''
						for pkginput in range(len(argsdict[k])):
							pcl.advanced('adding ' + pkginput + 'to command')
							pkgs += ' ' + pkginput
						pkgscmd = pkgscmdorig.replace('INPUT', pkginputs)
					else:
						pkgs = self.__execcmd(pkgscmdorig,False,False)
					pcl.verbose('Processing packages: ' + str(pkgs))
					cmd = cmd.replace('PKGS', str(pkgs))
				else:
					pcl.verbose('No pkglist to parse for ' + k)
				proc = self.__execcmd(cmd,True,False)

	def __execcmd(self,cmd:str,checkout:bool,showout:bool):
		exl = Log(self.loglevel, 'EXECUTECMD',)
		exl.verbose('Executing command ' + cmd)
		if showout:
			proc = sp.run(cmd, text=True, shell=True, check=checkout, stdout = sp.STDOUT)
		else:
			proc = sp.run(cmd, text=True, shell= True, check=checkout, stdout= sp.PIPE)

		exl.debug(proc.stdout)
		return proc.stdout



if __name__ == '__main__':
	Spm()
