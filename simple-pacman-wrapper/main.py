#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
import subprocess as sp
from argcomplete import autocomplete
from inspect import currentframe, getframeinfo


from log import Log
from contentdb import GetContent


class Spm():
	def __init__(self):
		# Defining arguments
		parser = ArgumentParser(description="Simple, yet powerfull pacman wrapper", epilog=" [*]Supports wildcard input [#]updates Package database [x]Exits Program")
		parser.add_argument('-v', '--verbose', action ='store_true', help='Increase output verbosity')
		parser.add_argument('-w', '--wildcard', action='store_true', help='Enable wildcard for supported commands')

		generalag = parser.add_argument_group('Genaral', 'General Package Management')
		generalag.add_argument('-i', '--install', nargs='+', type=str, help='Install programs [*#]')
		generalag.add_argument('-I', '--force-install', nargs='+', type=str, help='Install programs - Reinstall if already installed [*#]')
		generalag.add_argument('-r', '--remove', nargs='+', type=str, help='Remove programs [*]')
		generalag.add_argument('-a', '--autoremove', action='store_true', help='Remove unsed programs')
		generalag.add_argument('-u', '--upgrade', action='store_true', help='Perform system upgrade [#]')

		infoag = parser.add_argument_group('Info', 'Informations about the Program')
		infoag.add_argument('--show-commands', action='store_true', help="Show pacman commands used by the program [x]")
		infoag.add_argument('--show-sources', action='store_true', help="Show the sources of the commands [x]")

		debuggingag = parser.add_argument_group('Debugging', 'Options for development purposes')
		debuggingag.add_argument('--loglevel', choices = Log.loglevelids(Log), default="info", help='Set loglevel (default:info)')
		debuggingag.add_argument('--traceback', action='store_true', help='Enable traceback before logging entrys')
		debuggingag.add_argument('--tracebacklimit', type=int, help='Set limit for traceback')

		autocomplete(parser)
		args = parser.parse_args()
		argsdict = args.__dict__

		# Starting loggers
		if args.verbose:
			args.loglevel = "verbose"
		self.loglevel = args.loglevel
		pal = Log(args.loglevel, 'PARSEARGS')
		gcl = Log(args.loglevel, 'GETCONTENT')
		pcl = Log(args.loglevel, 'PARSECONTENT')

		pal.debug(argsdict)

		gcl.advanced("Getting content")
		# Getting content
		contentdict = GetContent()
		# gcl.debug("Contentdict: " + str(contentdict))
		infodict = contentdict['info']
		# gcl.debug("Infodict: " + str(infodict))
		commandsdict = contentdict['commands']
		# gcl.debug("Commandsdict: " + str(commandsdict))

		# check Which Infos should be displayed
		for i in infodict.keys():
			pal.advanced("INFO: checking for arg " + i)
			if argsdict[i]:
				pal.verbose("Printing info for " + i)
				print(infodict[i])

		# check which Commands should be executed
		for i in commandsdict.keys():
			pal.advanced("COMMANDS: checking for arg " + i)

			# if argument detected for commands
			if argsdict[i]:
				cmd = commandsdict[i][1]
				# Detect if command needs to parse pkglist
				if "PKGS" in cmd:
					pkgscmdorig = commandsdict[i][0]
					# Give user input to commandsting
					if "INPUT" in pkgscmdorig:
						for j in range(len(argsdict[i])):
							pkgs = ""
							pcl.debug(str(j) + ":" + argsdict[i][j])
							pkgscmd = pkgscmdorig.replace("INPUT", argsdict[i][j])
							pcl.debug("Command : "+ pkgscmd)
							pkgs += self.execcmd(pkgscmd,False,False)
					else:
						pkgs = self.execcmd(pkgscmdorig,False,False)
					pcl.verbose("Processing packages: " + str(pkgs))
					cmd = cmd.replace("PKGS", str(pkgs))
				else:
					pcl.verbose("No pkglist to parse for " + i)
				proc = self.execcmd(cmd,True,False)


	def execcmd(self,cmd:str,checkout:bool,showout:bool):
		l = Log(self.loglevel, 'EXECUTECMD',)
		l.verbose("Executing command " + cmd)
		if showout:
			proc = sp.run(cmd, text=True, shell=True, stdout = sp.STDOUT)
		else: 
			proc = sp.run(cmd, text=True, shell= True, stdout= sp.PIPE)

		l.debug(proc.stdout)
		return proc.stdout



if __name__ == "__main__":
	Spm()
