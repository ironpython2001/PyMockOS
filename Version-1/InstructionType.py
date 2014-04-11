class InstructionType(object):
	"""
	 No op
	"""
	Noop = 0,

	"""
	 Increments register
	 1 r1
	"""
	Incr = 1,
	"""
	  Adds constant 1 to register 1
	 
	 2 r1, $1
	 
	"""
	Addi = 2,

	"""
	 Adds r2 to r1 and stores the value in r1
	 
	 3 r1, r2
	 
	"""
	Addr = 3,

	"""
	 Pushes contents of register 1 onto stack
	 
	 4 r1
	 
	"""
	Pushr = 4,

	"""
	 Pushes constant 1 onto stack
	 
	 5 $1
	 
	"""
	Pushi = 5,

	"""
	 Moves constant 1 into register 1
	 
	 6 r1, $1
	 
	"""
	Movi =6,

	"""
	 Moves contents of register2 into register 1
	 
	 7 r1, r2
	 
	"""
	Movr = 7,

	"""
	 Moves contents of memory pointed to register 2 into register 1
	 
	 8 r1, r2
	 
	"""
	Movmr=8,

	"""
	 Moves contents of register 2 into memory pointed to by register 1
	 
	 9 r1, r2
	 
	"""
	Movrm=9,

	"""
	 Moves contents of memory pointed to by register 2 into memory pointed to by register 1
	 
	 10 r1, r2
	 
	"""
	Movmm =10,

	"""
	 Prints out contents of register 1
	 
	 11 r1
	 
	"""
	Printr = 11,

	"""
	 Prints out contents of memory pointed to by register 1
	 
	 12 r1
	 
	"""
	Printm =12,

	"""
	 Control transfers to the instruction whose address is r1 bytes relative to the current instruction. 
	 r1 may be negative.
	 
	 13 r1
	 
	"""
	Jmp =13,

	"""
	 Compare contents of r1 with 1.  If r1 &lt; 9 set sign flag.  If r1 &gt; 9 clear sign flag.
	 If r1 == 9 set zero flag.
	 
	 14 r1, $9
	 
	"""
	Cmpi = 14,


	"""
	 Compare contents of r1 with r2.  If r1 &lt; r2 set sign flag.  If r1 &gt; r2 clear sign flag.
	 If r1 == r2 set zero flag.
	 
	 15 r1, r2
	 
	"""
	Cmpr =15,


	"""
	 If the sign flag is set, jump to the instruction that is offset r1 bytes from the current instruction
	 
	 16 r1
	 		
	"""
	Jlt = 16,

	"""
	 If the sign flag is clear, jump to the instruction that is offset r1 bytes from the current instruction
	 
	 17 r1
	 		
	"""
	Jgt =17,

	"""
	 If the zero flag is set, jump to the instruction that is offset r1 bytes from the current instruction
	 
	 18 r1
	 		
	"""
	Je =18,

	"""
	 Call the procedure at offset r1 bytes from the current instrucion.  
	 The address of the next instruction to excetute after a return is pushed on the stack
	 
	 19 r1
	 		
	"""
	Call = 19,

	"""
	 Call the procedure at offset of the bytes in memory pointed by r1 from the current instrucion.  
	 The address of the next instruction to excetute after a return is pushed on the stack
	 
	 20 r1
	 		
	"""
	Callm = 20,

	"""
	 Pop the return address from the stack and transfer control to this instruction
	 
	 21
	 		
	"""
	Ret = 21,

	"""
	 Allocate memory of the size equal to r1 bytes and return the address of the new memory in r2.  
	 If failed, r2 is cleared to 0.
	 
	 22 r1, r2
	 		
	"""
	Alloc = 22,

	"""
	 Acquire the OS lock whose # is provided in register r1.  
	 Icf the lock is not held by the current process
	 the operation is a no-op
	 
	 23 r1
	 		
	"""
	AcquireLock = 23,

	"""
	 Release the OS lock whose # is provided in register r1.  
	 Another process or the idle process 
	 must be scheduled at this point.  
	 if the lock is not held by the current process, 
	 the instruction is a no-op
	 
	 24 r1
	 		
	"""
	ReleaseLock= 24,

	"""
	 Sleep the # of clock cycles as indicated in r1.  
	 Another process or the idle process 
	 must be scheduled at this point.  
	 If the time to sleep is 0, the process sleeps infinitely
	 
	 25 r1
	 		
	"""
	Sleep = 25,

	"""
	 Set the priority of the current process to the value
	 in register r1
	 
	 26 r1
	 		
	"""
	SetPriority = 26,

	"""
	 This opcode causes an exit and the process's memory to be unloaded.  
	 Another process or the idle process must now be scheduled
	 
	 27
	 		
	"""
	Exit = 27,

	"""
	 Free the memory allocated whose address is in r1
	 
	 28 r1
	 		
	"""
	FreeMemory = 28,

	"""
	 Map the shared memory region identified by r1 and return the start address in r2
	 
	 29 r1, r2
	 		
	"""
	MapSharedMem = 29,

	"""
	 Signal the event indicated by the value in register r1
	 
	 30 r1
	 		
	"""
	SignalEvent = 30,

	"""
	 Wait for the event in register r1 to be triggered resulting in a context-switch
	 
	 31 r1
	 		
	"""
	WaitEvent = 31,

	"""
	 Read the next 32-bit value into register r1
	 
	 32 r1
	 		
	"""
	Input = 32,

	"""
	 set the bytes starting at address r1 of length r2 to zero
	 
	 33 r1, r2
	 		
	"""
	MemoryClear =33,

	"""
	 Terminate the process whose id is in the register r1
	 
	 34 r1
	 		
	"""
	TerminateProcess = 34,

	"""
	 Pop the contents at the top of the stack into register r1 
	 
	 35 r1
	 		
	"""
	Popr = 35,

	"""
	 Pop the contents at the top of the stack into the memory pointed to by register r1 
	 
	 36 r1
	 		
	"""
	Popm = 36