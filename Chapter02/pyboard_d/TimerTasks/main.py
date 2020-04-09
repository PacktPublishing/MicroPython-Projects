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
import pyb         # For uPython MCU
import time

# Buffer for interrupt error messages
micropython.alloc_emergency_exception_buf(100)

# define LED color constants
LED_RED = 1
LED_GREEN = 2
LED_BLUE = 3


# Function that contains the task code for toggling the blue LED
def task1(timer):
    pyb.LED(LED_BLUE).toggle()

    return 


# Function that contains the task code for toggling the yellow LED
def task2(timer):
    pyb.LED(LED_GREEN).toggle()

    return 


############################################################
#
# Start script execution ...
#
############################################################
# Setup the MCU and application code to starting conditions
# The blue LED will start on, the yellow LED will be off
pyb.LED(LED_BLUE).on()
pyb.LED(LED_GREEN).off()

# Create task timer for Blue LED
TimerBlueLed = pyb.Timer(1)
TimerBlueLed.init(freq=5)
TimerBlueLed.callback(task1)
print("Task 1 - Blue LED Toggle initialized ...")

# Create task timer for Green LED
TimerGreenLed = pyb.Timer(2)
TimerGreenLed.init(freq=5)
TimerGreenLed.callback(task2)
print("Task 2 - Green LED Toggle initialized ...")

# Tracks seconds since program started
TimeStart = time.ticks_ms()

while True:
    time.sleep_ms(5000)
    SecondsLive = time.ticks_diff(time.ticks_ms(), TimeStart) /1000
    print("Executing for ", SecondsLive, " seconds")