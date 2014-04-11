class StackException(Exception):
	""" 
	Process ID, Num of Bytes more than the stack could handle 
	"""
	def __init__(self, pidIn, tooManyBytesIn):
		"""
		 Constructor for a Memory Exception
		 Parameters
		 pidIn = Process ID
		 tooManyBytesIn = Process address
		"""
		self._pid = 0
		self._tooManyBytes = 0
		self._pid = pidIn
		self._tooManyBytes = tooManyBytesIn

	def ToString(self):
		""" 
		Pretty printing for StackException
		returns Formatted string about the StackException
		"""
		#return String.Format("Process {0} tried to push {1} too many bytes on to the stack and will be terminated! ", self._pid, self._tooManyBytes)
		return "Process " + self._pid.__str__() + " tried to push " + self._tooManyBytes.__str__() +  "  too many bytes on to the stack and will be terminated! "