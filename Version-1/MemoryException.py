class MemoryException(Exception):
	""" 
	Process ID, Num of Bytes more than the stack could handle 
	"""
	def __init__(self, pidIn, addrIn):
		"""
		 Constructor for a Memory Exception
		 Parameters
		 pidIn = Process ID
		 addrIn = Process address
		"""
		self._pid = 0
		self._processAddress = 0
		self._pid = pidIn
		self._processAddress = addrIn

	def ToString(self):
		""" 
		 Pretty printing for MemoryException
		 returns Formatted string about the MemoryException
		"""
		#return String.Format("Process {0} tried to access memory at address {1} and will be terminated! ", self._pid, self._processAddress)
		return "Process " + self._pid.__str__() + " tried to access memory at address " + self._processAddress.__str__() +  "  and will be terminated! "