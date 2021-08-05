class log:
	def __init__(self, verbose:bool, stage:chr):
		self.verbose=verbose
		self.stage=stage
		self.info('Started logger for Stage ' + stage)
		self.verboseinfo('Verbose logging enabled for ' + stage)

	def info(self, message:chr): 
		print('[Info](' + self.stage + '):' + message)
	
	def warning(self, warning:chr): 
		print('[Warning]: (' + self.stage + '):' + warning)
	
	def error(self, error:chr): 
		print('[Error](' + self.stage + '):' + error)

	def verboseinfo(self, message:chr):
		if self.verbose:
			print('[Verbose](' + self.stage + '):' + message)