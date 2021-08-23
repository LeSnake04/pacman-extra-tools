#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from argcomplete import autocomplete
import sys as s

from spm import Spm
from log import Log


class ArgParser(ArgumentParser):
    def error(self, message):
        s.stderr.write('error: %s\n' % message)
        self.print_help()
        s.exit(2)

def main():
	# Defining arguments
	parser = ArgParser(description='Simple, yet powerfull pacman wrapper', epilog='{w}:Supports wildcard input  {y}:Refreshes Package database {x}:Exits Program')
	parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')
	parser.add_argument('-w', '--wildcard', action='store_true', help='Enable wildcard for supported commands - Supported on actions labeled with {w})')
	parser.add_argument('-f', '--force', action='store_true', help='Force action - Suported when FORCE in help text')
	parser.add_argument('-y', '--norefresh', action='store_true', help='Don´t refresh package Database - Supported on actions labeled with {y})')

	generalag = parser.add_argument_group('Genaral', 'General Package Management')
	generalag.add_argument('-i', '--install', nargs='+', type=str, help='Install programs {wy} (FORCE: Reinstall if already installed)')
	generalag.add_argument('-r', '--remove', nargs='+', type=str, help='Remove programs {w}')
	generalag.add_argument('-a', '--autoremove', action='store_true', help='Remove unsed programs')
	generalag.add_argument('-u', '--upgrade', action='store_true', help='Perform system upgrade {y}')

	infoag = parser.add_argument_group('Info', 'Informations about the Program')
	infoag.add_argument('--show-commands', action='store_true', help='Show pacman commands used by the program {x}')
	infoag.add_argument('--show-sources', action='store_true', help='Show the sources of the commands {x}')

	debuggingag = parser.add_argument_group('Debugging', 'Options for development purposes')
	debuggingag.add_argument('--loglevel', choices=Log.loglevelids(Log), default='info', help='Set loglevel (default:info)')
	debuggingag.add_argument('-D', '--debug', action='store_true', help='Set Loglevel to \"debug\"')
	debuggingag.add_argument('--log-traceback', action='store_true', help='Enable traceback before logging entrys')
	debuggingag.add_argument('--log-tracebacklimit', type=int, help='Set limit for traceback')

	autocomplete(parser)
	if len(s.argv)==1:
		parser.print_help()
		s.exit(1)
	Spm(parser.parse_args())


if __name__ == '__main__':
	main()
