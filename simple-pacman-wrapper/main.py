#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from log import Log
from argparse import ArgumentParser
from contentdb import GetContent


def main():
	# Defining arguments
	parser = ArgumentParser(description='Simple, yet powerfull pacman wrapper')
	parser.add_argument('-v', '--verbose', action='store_true', help='Set loglevel to \'verbose\'')
	parser.add_argument('-D', '--debug', action='store_true', help='Set loglevel to \'verbose\'')
	parser.add_argument('--loglevel', choices=Log.loglevelids(Log), default="info", help='Set loglevel (default:info)')

	general = parser.add_argument_group('Genaral', 'General Package Management')
	general.add_argument('-i', '--install', nargs='+', type=list, help='Install programms')
	general.add_argument('-a', '--autoremove', action='store_true', help='Remove unsed programms')

	info = parser.add_argument_group('Info', 'Informations about the Program')
	info.add_argument('--show-commands', action='store_true', help="Show pacman commands used by the program")

	args = parser.parse_args()
	argsdict = args.__dict__

	# Starting loggers
	if args.verbose:
		args.loglevel = "verbose"
	if args.debug:
		args.loglevel = "debug"
	pal = Log(args.loglevel, 'PARSEARGS')
	gcl = Log(args.loglevel, 'GETCONTENT')
	pil = Log(args.loglevel, 'PRINTINFO')
	exl = Log(args.loglevel, 'EXECUTECMD')

	pal.debug(args)

	# Getting content
	contentdict = GetContent()
	gcl.debug("Contentdict: " + str(contentdict))
	infodict = contentdict['info']
	gcl.debug("Infodict: " + str(infodict))
	commandsdict = contentdict['commands']
	gcl.debug("Commandsdict: " + str(commandsdict))

	# Which Infos should be displayed
	for i in contentdict['info'].keys():
		pal.advanced("INFO: checking for arg " + i)
		if argsdict[i]:
			print(infodict[i])

	# Which Infos should be displayed
	for i in contentdict['commands'].keys():
		pal.advanced("COMMANDS: checking for arg " + i)
		if argsdict[i]:
			gcl.debug(commandsdict[i])


if __name__ == "__main__":
	exit(main())
