# APDS_9960.py -- Chapter 7 - Gesture Controller
##################################################################################
# Title                 :   Gesture Controller APDS-9660 "Driver"
# Filename              :   main.py
# Author                :   JWB
# Origin Date           :   06/07/2019
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
import micropython                      # For emergency exception buffer
from pyb import I2C
import utime 

#slave device is 0x39
APDS_9960_ADDRESS = 0x39
device_reg = 0x80

# Register Definitions
REGISTER_ENABLE = 0x80
REGISTER_CONTROL = 0x8F
REGISTER_PDATA = 0x9C
REGISTER_GPENTH = 0xA0
REGISTER_EXTH = 0xA1
REGISTER_GCONFIG1 = 0xA2
REGISTER_GCONFIG2 = 0xA3
REGISTER_GCONFIG4 = 0xAB
REGISTER_GFLVL = 0xAE
REGISTER_GSTATUS = 0xAF
REGISTER_GFIFO_U = 0xFC
REGISTER_GFIFO_D = 0xFD
REGISTER_GFIFO_L = 0xFE
REGISTER_GFIFO_R = 0xFF

# Register Bit Definitions
REGISTER_ENABLE_BIT_PON = 0x01
REGISTER_ENABLE_BIT_PEN = 0x04
REGISTER_ENABLE_BIT_GEN = 0x40
REGISETER_BIT_PIEN = 0x20
REGISTER_BIT_LDRIVE = 0xC0
REGISTER_GCONFIG4_BIT_GMODE = 0x1
REGISTER_GSTATUS_BIT_GVALID = 0x1
REGISTER_GCONTROL_BITS_GFIFOTH = 0x0C

APDS_9960_PRESENT = False
PROXIMITY_THRESHOLD_COUNT = 40
GESTURE_EXIT_THRESHOLD_COUNT = 30
GESTURE_PROCESS_TIMEOUT = 100
GESTURE_DATA_LIST_SIZE_MAX = 255

Gesture = 0x0

############################################################
#
# APDS_9960 contains the functionality required to 
# initialize and control the APDS_9960 gesture ic from Avago. 
# The class requires the following:
# - I2CObject which is an initialized I2C object
#
# Use Detect() to return whether a valid gesture has been detected
#
############################################################
class APDS_9960():

	GESTURE_FORWARD = 0x0
	GESTURE_BACKWARD = 0x1
	GESTURE_LEFT = 0x2
	GESTURE_RIGHT = 0x3

	def __init__(self,I2CObject, Verbose):
		self.__Verbose = Verbose
		self.i2c = I2CObject
		self.DeviceList = self.i2c.scan()

		for Device in range(len(self.DeviceList)):
			if self.DeviceList[Device] == APDS_9960_ADDRESS:
				self.APDS_9960_PRESENT = True 
			else:
				print("APDS9960 not present!")
				return False

		# Enable the PON, PEN, GEN
		self.mode = REGISTER_ENABLE_BIT_PEN + REGISTER_ENABLE_BIT_GEN

		# Set the analog engine mode
		self.i2c.mem_write(self.mode, APDS_9960_ADDRESS, REGISTER_ENABLE,timeout=1000)

		# Set the IR gain to maximum
		self.i2c.mem_write(0x0C, APDS_9960_ADDRESS, REGISTER_CONTROL,timeout=1000)

		# Set the proximity threshold that will enable GMODE
		self.i2c.mem_write(PROXIMITY_THRESHOLD_COUNT, APDS_9960_ADDRESS, REGISTER_GPENTH, timeout=1000)

		# Set the gesture exit threshold
		self.i2c.mem_write(GESTURE_EXIT_THRESHOLD_COUNT, APDS_9960_ADDRESS, REGISTER_EXTH, timeout=1000)

		# Read the GCONFIG2 register and set the gain to 4. Also set maximum wait time
		self.registerData = self.i2c.mem_read(1, APDS_9960_ADDRESS, REGISTER_GCONFIG2)
		self.registerData = ord(self.registerData) | 0x40 | 0x0
		self.i2c.mem_write(self.registerData, APDS_9960_ADDRESS, REGISTER_GCONFIG2, timeout=1000)

		self.GestureCount = ord(self.i2c.mem_read(1,APDS_9960_ADDRESS, REGISTER_GFLVL))

		while self.GestureCount > 0:
		  self.gestureData = self.i2c.mem_read(4, APDS_9960_ADDRESS, REGISTER_GFIFO_U)
		  self.GestureCount = ord(self.i2c.mem_read(1,APDS_9960_ADDRESS, REGISTER_GFLVL))
		  if self.__Verbose == True:
		  	print("GestureRemaining= ", self.GestureCount)

		# Enable the PON, PEN, GEN
		self.mode = REGISTER_ENABLE_BIT_PON + REGISTER_ENABLE_BIT_PEN + REGISTER_ENABLE_BIT_GEN

		# Set the analog engine mode
		self.i2c.mem_write(self.mode, APDS_9960_ADDRESS, REGISTER_ENABLE,timeout=1000)

		self.GestureData = []
		self.GestureDataCount = 0
		self.TimeSinceLastGestureData = utime.ticks_ms()
		self.TimeNow = utime.ticks_ms()
		self.GestureInProgress = False
		

	def Verbose(self, State):
		self.__Verbose = State
	
	def GestureData_Process(self,GestureData, GestureDataCount):
	  Gesture_Vertical = 0
	  Gesture_Horizontal = 0

	  for i in range ((GestureDataCount- 5), (GestureDataCount -1)):
		if self.__Verbose == True:
			print("GestureData=", GestureData[i][0],GestureData[i][1],GestureData[i][2],GestureData[i][3])

		Gesture_Vertical += GestureData[i][0] - GestureData[i][1] 
		Gesture_Horizontal += GestureData[i][2] - GestureData[i][3] 

	  if(abs(Gesture_Vertical) > abs(Gesture_Horizontal)):
	    if Gesture_Vertical < 0:
	        Gesture = self.GESTURE_BACKWARD
	    else:
	        Gesture = self.GESTURE_FORWARD
	  else:
	    if Gesture_Horizontal < 0:
	        Gesture = self.GESTURE_RIGHT
	    else:
	        Gesture = self.GESTURE_LEFT

	  return Gesture		

	def GestureDataClear(self):
		self.GestureData.clear()
		self.GestureDataCount = 0
		self.GestureCount = 0

	def Detect(self):
		 # Check to see if there is valid gesture data present
	  	self.GesturePresent = ord((self.i2c.mem_read(1, APDS_9960_ADDRESS, REGISTER_GSTATUS))) & REGISTER_GSTATUS_BIT_GVALID

		if self.GesturePresent == 0x1:
			self.GestureInProgress = True
			self.GestureCount = ord(self.i2c.mem_read(1,APDS_9960_ADDRESS, REGISTER_GFLVL))

			while self.GestureCount > 0:
				self.GestureData.append(self.i2c.mem_read(4, APDS_9960_ADDRESS, REGISTER_GFIFO_U))
				self.GestureDataCount+=1
				self.GestureCount = ord(self.i2c.mem_read(1,APDS_9960_ADDRESS, REGISTER_GFLVL))

				if(self.GestureDataCount > GESTURE_DATA_LIST_SIZE_MAX):
					self.GestureDataClear()

			if (self.GestureDataCount > 0) and (self.__Verbose == True):
				print("GestureData=", self.GestureData[self.GestureDataCount-1][0],self.GestureData[self.GestureDataCount-1][1],self.GestureData[self.GestureDataCount-1][2],self.GestureData[self.GestureDataCount-1][3])
			self.TimeSinceLastGestureData = utime.ticks_ms()
		else:
			if self.GestureInProgress == False:
				self.TimeSinceLastGestureData = utime.ticks_ms()
	        
		self.TimeNow = utime.ticks_ms()

		if((self.TimeNow - self.TimeSinceLastGestureData) > GESTURE_PROCESS_TIMEOUT):
			self.GestureInProgress = False
			if self.__Verbose == True:
				print("Process Gesture Data!")
			self.Result = self.GestureData_Process(self.GestureData, self.GestureDataCount)
			self.GestureDataClear()
			return self.Result