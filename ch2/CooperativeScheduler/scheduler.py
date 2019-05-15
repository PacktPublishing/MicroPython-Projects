# tasks - Chapter 2 Cooperative Scheduler Example
##################################################################################
# Title                 :   Cooperative Scheduler Main
# Filename              :   Cooperative Scheduler.py
# Author                :   JWB
# Origin Date           :   01/07/2019
# Version               :   1.0.0
# Copyright             :   Jacob Beningo
# All Rights Reserved
#
# THIS SOFTWARE IS PROVIDED BY BENINGO EMBEDDED GROUP "AS IS" AND ANY EXPRESSED
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL BENINGO EMBEDDED GROUP OR ITS CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.
#
##################################################################################

import pyb         # For uPython MCU features

# Defines the class that contains a Cooperative Scheduler
class Scheduler(object):
	# Class constructor
	def __init__(self):
		# Private variables used within the class context
		self.__Tick = 0
		self.__Timer = pyb.Timer(1)
		self.__Timer.init(freq=1000)	
		self.__Timer.callback(self.__Increment)
		self.__Frequency = 1000
		self.__TaskList = [[self.__TaskPlaceHolder,0,0]]
		self.__NumberofTasks = 0
		self.__ExitState = False

	# Frequency is private but we allow get and set funcationality
	# to change the rate at which the schduler ticks executes
	@property
	def Frequency(self):

		return self.__Frequency

	@Frequency.setter
	def Frequency(self, Value):
		if Value > 1 and Value < 1000:
			self.__Timer.init(freq=Value)
			self.__Frequency = Value
		else:
			raise ValueError("Frequency must be between 1 and 1000 Hz!")
		return

	# ExitState is private but we allow get and set funcationality
	# to change whether the scheduler should run or not.
	@property
	def ExitState(self):
		return self.__ExitState

	@ExitState.setter
	def ExitState(self):
		self.__ExitState = True

	# Acts as a placeholder for the first task added to the list
	def __TaskPlaceHolder(self):
		TempCount = TempCount + 1

		return

	# Increments the tick variable used by the scheduler to 
	# schedule tasks
	def __Increment(self, timer):
		self.__Tick = self.__Tick + 1

		return 

	# Adds a new task to the TaskList.
	def AddTask(self, Task):

		# Add a task to the list
		self.__TaskList.append(Task)

		# The first task is a dummy task and 
		# should be removed when the first real
		# task is added to the list.
		if(self.__NumberofTasks == 0):
			del(self.__TaskList[0])
			self.__NumberofTasks= 1
		else:
			self.__NumberofTasks += 1

		return

	# Is called in the background from the main execution loop
	# to identify tasks that need to be executed or to run any 
	# background tasks.
	def Run(self):
		for Task in range (len(self.__TaskList)):
			if(self.__TaskList[Task][2] <= self.__Tick):
				self.__TaskList[Task][2] += self.__TaskList[Task][1] 
				Result = self.__TaskList[Task][0]()

				if Result == True:
					self.ExitState = True

	