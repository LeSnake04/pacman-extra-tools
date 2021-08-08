#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import traceback as tb
from typing import Union


class Log:
	def __init__(self, loglevel:Union[str, int], stage:str = None, traceback:bool = False, tracebacklimit:int = 2):
		loglevelids = self.loglevelids()
		loglevels = self.__loglevels()
		self.loglevel = loglevel
		self.traceback = traceback
		self.tracebacklimit = tracebacklimit
		self.enabledlevels = {}

		if isinstance(loglevel, int):
			loglevel = loglevelids[loglevel]
		for i in loglevels[loglevel].keys():
			self.enabledlevels[i] = loglevels[loglevel][i]

		self.stage = "INITLOGGER"
		self.advanced('Started logger for Stage ' + stage)
		self.debug('Debugging enabled for ' + stage)
		self.stage = stage

	def critical(self, msg):
		self.__printmsg("critical", msg)

	def error(self, msg):
		self.__printmsg("error", msg)

	def warning(self, msg):
		self.__printmsg("warning", msg)

	def info(self, msg):
		self.__printmsg("info", msg)

	def verbose(self, msg):
		self.__printmsg("verbose", msg)

	def advanced(self, msg):
		self.__printmsg("advanced", msg)

	def debug(self, msg):
		self.__printmsg("debug", msg)

	def __printmsg(self, msgloglevel: str, msg):
		if self.enabledlevels[msgloglevel]:
			outputmsg = '[' + msgloglevel.upper() + ']'
			if self.traceback:
				tb.print_stack(limit=self.tracebacklimit)
			if self.stage:
				outputmsg += '(' + self.stage + '):'
			outputmsg += str(msg)
			print(outputmsg)

	def loglevelids(self):
		loglevelids = ["none", "critical", "error", "warning", "info", "verbose", "advanced", "debug"]
		return loglevelids

	@classmethod
	def __loglevels(cls):
		loglevels = {
			"none": {
				"critical": False,
				"error": False,
				"warning": False,
				"info": False,
				"verbose": False,
				"advanced": False,
				"debug": False
			},
			"critical": {
				"critical": True,
				"error": False,
				"warning": False,
				"info": False,
				"verbose": False,
				"advanced": False,
				"debug": False
			},
			"error": {
				"critical": True,
				"error": True,
				"warning": False,
				"info": False,
				"verbose": False,
				"advanced": False,
				"debug": False
			},
			"warning": {
				"critical": True,
				"error": True,
				"warning": True,
				"info": False,
				"verbose": False,
				"advanced": False,
				"debug": False
			},
			"info": {
				"critical": True,
				"error": True,
				"warning": True,
				"info": True,
				"verbose": False,
				"advanced": False,
				"debug": False
			},
			"verbose": {
				"critical": True,
				"error": True,
				"warning": True,
				"info": True,
				"verbose": True,
				"advanced": False,
				"debug": False
			},
			"advanced": {
				"critical": True,
				"error": True,
				"warning": True,
				"info": True,
				"verbose": True,
				"advanced": True,
				"debug": False
			},
			"debug": {
				"critical": True,
				"error": True,
				"warning": True,
				"info": True,
				"verbose": True,
				"advanced": True,
				"debug": True
			}
		}
		return loglevels
