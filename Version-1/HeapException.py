class HeapException(Exception):
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
		Pretty printing for Heap Exception
		returns Formatted string about the HeapException
		"""
		#return string.format("Process {0} tried to alloc {1} bytes more from the heap than were free and will be terminated! ", self._pid, self._tooManyBytes)
		return "Process " + self._pid.__str__() + " tried to alloc " + self._tooManyBytes.__str__() +  "  bytes more from the heap than were free and will be terminated! "


