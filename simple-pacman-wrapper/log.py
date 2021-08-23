#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import traceback as tb
import sys as s
from typing import Union

class Log:
	def __init__(self, loglevel:Union[str, int], subprog:str = 'main', stage:str = None, traceback:bool = False, tracebacklimit:int = 1, verbose_internal_logging:str = False):
		loglevelids = self.loglevelids()
		loglevels = self.__loglevels()
		self.loglevel = loglevel
		self.traceback = traceback
		self.verbose_internal_logging = verbose_internal_logging
		self.tracebacklimit = tracebacklimit
		self.enabledlevels = {}
		if isinstance(loglevel, int):
			loglevel = loglevelids[loglevel]
		for k, v in loglevels[loglevel].items():
			self.enabledlevels[k] = v

		self.subprog = subprog.upper()
		self.chstage('InitLogger')
		self.advanced('Started logger for subprogram ' + subprog.upper() + ', Stage ' + stage)
		self.__advanced('Debugging enabled for ' + stage)
		self.chstage(stage)

	def chsubprog(self, subprog:str):
		subprog = subprog.upper()
		self.advanced('changing to Subprogram ' + subprog)
		self.subprog = subprog
		return self

	def chstage(self, newstage:str):
		self.stage = 'chstage'
		self.__advanced('Switching to stage ' + newstage )
		self.stage = newstage
		return self

	def __advanced(self, msg):
		if self.verbose_internal_logging:
			self.advanced(msg)

	def critical(self, *msg):
		self.__printmsg('critical', msg)

	def error(self, *msg):
		self.__printmsg('error', msg)

	def warning(self, *msg):
		self.__printmsg('warning', msg)

	def info(self, *msg):
		self.__printmsg('info', msg)

	def verbose(self, *msg):
		self.__printmsg('verbose', msg)

	def advanced(self, *msg):
		self.__printmsg('advanced', msg)

	def debug(self, *msg):
		self.__printmsg('debug', msg)


	def __printmsg(self, msgloglevel: str, msgin):
		if self.enabledlevels[msgloglevel]:
			msg = ''
			for msgp in msgin:
				msg += str(msgp)

			outputmsg = '[' + msgloglevel.upper() + ']'

			if self.subprog:
				outputmsg += '{' + self.subprog + '}'

			if self.stage:
				outputmsg += '(' + self.stage + ')'
			outputmsg += ': ' + str(msg)
			print(outputmsg)

			if self.traceback:
				tblist = list(reversed(tb.format_list(tb.extract_stack())))
				for i in range(self.tracebacklimit-0):
					print(tblist[2+i])
			

	def loglevelids(self):
		loglevelids = ['none', 'critical', 'error', 'warning', 'info', 'verbose', 'advanced', 'debug']
		return loglevelids

	@classmethod
	def __loglevels(cls):
		loglevels = {
			'none': {
				'critical': False,
				'error': False,
				'warning': False,
				'info': False,
				'verbose': False,
				'advanced': False,
				'debug': False
			},
			'critical': {
				'critical': True,
				'error': False,
				'warning': False,
				'info': False,
				'verbose': False,
				'advanced': False,
				'debug': False
			},
			'error': {
				'critical': True,
				'error': True,
				'warning': False,
				'info': False,
				'verbose': False,
				'advanced': False,
				'debug': False
			},
			'warning': {
				'critical': True,
				'error': True,
				'warning': True,
				'info': False,
				'verbose': False,
				'advanced': False,
				'debug': False
			},
			'info': {
				'critical': True,
				'error': True,
				'warning': True,
				'info': True,
				'verbose': False,
				'advanced': False,
				'debug': False
			},
			'verbose': {
				'critical': True,
				'error': True,
				'warning': True,
				'info': True,
				'verbose': True,
				'advanced': False,
				'debug': False
			},
			'advanced': {
				'critical': True,
				'error': True,
				'warning': True,
				'info': True,
				'verbose': True,
				'advanced': True,
				'debug': False
			},
			'debug': {
				'critical': True,
				'error': True,
				'warning': True,
				'info': True,
				'verbose': True,
				'advanced': True,
				'debug': True
			}
		}
		return loglevels
