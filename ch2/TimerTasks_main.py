# main.py -- Chapter 2 - Timer Tasks Example
##################################################################################
# Title                 :   Timer Tasks Main
# Filename              :   TimerTasks_main.py
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

import micropython # For emergency exception buffer
import pyb         # For uPython MCU features

# Buffer for interrupt error messages
micropython.alloc_emergency_exception_buf(100)

# Function that contains the task code for toggling the blue LED
def Led_BlueToggle(timer):
    pyb.LED(4).toggle()

    return 

# Function that contains the task code for toggling the yellow LED
def Led_YellowToggle(timer):
    pyb.LED(3).toggle()

    return 

# Setup the MCU and application code to starting conditions
# The blue LED will start on, the yellow LED will be off
def System_Init():
  print("Initializing system ...")
  pyb.LED(4).on()
  pyb.LED(3).off()
  print("LED's initialized ...")

  # Create task timer for Blue LED
  TimerBlueLed = pyb.Timer(1)
  TimerBlueLed.init(freq=5)
  TimerBlueLed.callback(Led_BlueToggle)
  print("Blue Task initialized ...")

  # Create task timer for Yellow LED
  TimerYellowLed = pyb.Timer(2)
  TimerYellowLed.init(freq=5)
  TimerYellowLed.callback(Led_YellowToggle)
  print("Yellow Task initialized ...")

  print("Starting application ...")

############################################################
#
# Start script execution ...
#
############################################################
# Initialize the system
System_Init()

# Tracks seconds since program started
SecondsLive = 0

while True:
  pyb.delay(5000)
  SecondsLive = SecondsLive + 5
  print("Executing for ", SecondsLive, " seconds")