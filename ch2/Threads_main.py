# main.py -- Chapter 2 - Threads Example
##################################################################################
# Title                 :   Threads Main
# Filename              :   Threads_main.py
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
import _thread     # For thread support

# Buffer for interrupt error messages
micropython.alloc_emergency_exception_buf(100)

# Function that contains the task code for toggling the blue LED
def Led_BlueToggle():
    while True:
      pyb.LED(4).toggle()
      pyb.delay(250)

# Function that contains the task code for toggling the yellow LED
def Led_YellowToggle():
    while True:
      pyb.LED(3).toggle()
      pyb.delay(250)

# Setup the MCU and application code to starting conditions
# The blue LED will start on, the yellow LED will be off
def System_Init():
  print("Initializing system ...")
  pyb.LED(4).on()
  pyb.LED(3).off()
  print("LED's initialized ...")
  print("Starting application ...")

############################################################
#
# Start script execution ...
#
############################################################
# Initialize the system
System_Init()

_thread.start_new_thread(Led_BlueToggle, ())
_thread.start_new_thread(Led_YellowToggle, ())

# Tracks seconds since program started
SecondsLive = 0

while True:
  pyb.delay(5000)
  SecondsLive = SecondsLive + 5
  print("Executing for ", SecondsLive, " seconds")