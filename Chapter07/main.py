# main.py -- Chapter 7 - Gesture Controller
##################################################################################
# Title                 :   Gesture Controller Test Application
# Filename              :   main.py
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
import micropython                      # For emergency exception buffer
from pyb import I2C                    # For i2c bus access
from APDS_9960 import APDS_9960         # Gesture control driver
import utime

# Buffer for interrupt error messages
micropython.alloc_emergency_exception_buf(100)

############################################################
# Application Constants
############################################################

############################################################
# Application Variables
############################################################
# Setup the MCU and application code to starting conditions
# The blue LED will start on, the yellow LED will be off
def System_Init():
  print("Initializing system ...")
  print("Starting application ...")

############################################################
#
# Start script execution ...
#
############################################################
# Initialize the system
System_Init()

# Create a uart object, uart4, and setup the serial parameters
i2c = I2C(1)                         # create on bus 1
i2c = I2C(1, I2C.MASTER)             # create and init as a master
i2c.init(I2C.MASTER, baudrate=400000) # init as a master

# Initialize the pins that will be used for LED control
LED_Forward = pyb.Pin('PD14', pyb.Pin.OUT_PP)
LED_Backward = pyb.Pin('PB0', pyb.Pin.OUT_PP)
LED_Left = pyb.Pin('PB4', pyb.Pin.OUT_PP)
LED_Right = pyb.Pin('PA3', pyb.Pin.OUT_PP)

# Set the LED's initial state to off
LED_Forward.value(1)
LED_Backward.value(1)
LED_Left.value(1)
LED_Right.value(1)

# Initialize the gesture driver and disable debug messages
Gesture = APDS_9960(i2c, False)

GestureDetected = False
GestureDetectedTime = utime.ticks_ms()

# Main application loop
while True:

  Result = Gesture.Detect()

  # Determine if there has been a validated gesture, if so tell us!
  if Result == APDS_9960.GESTURE_LEFT:
    GestureDetected = True
    GestureDetectedTime = utime.ticks_ms()
    LED_Left.low()
    print("Gesture Left!")
  elif Result == APDS_9960.GESTURE_RIGHT:
    GestureDetected = True
    GestureDetectedTime = utime.ticks_ms()
    LED_Right.low()
    print("Gesture Right!")
  elif Result == APDS_9960.GESTURE_FORWARD:
    GestureDetected = True
    GestureDetectedTime = utime.ticks_ms()
    LED_Forward.low()
    print("Gesture Forward!")
  elif Result == APDS_9960.GESTURE_BACKWARD:
    GestureDetected = True
    GestureDetectedTime = utime.ticks_ms()
    LED_Backward.low()
    print("Gesture Backward!")      

  if GestureDetected is True:
    if (utime.ticks_ms() - GestureDetectedTime) > 5000:
      GestureDetected = False
      LED_Backward.high()
      LED_Forward.high()
      LED_Right.high()
      LED_Left.high()