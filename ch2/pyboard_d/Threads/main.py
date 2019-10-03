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
import time        # For time features
import _thread     # For thread support

# Buffer for interrupt error messages
micropython.alloc_emergency_exception_buf(100)

# define LED color constants
LED_RED = 1
LED_GREEN = 2
LED_BLUE = 3


# Function that contains the task code for toggling the blue LED
def task1():
    while True:
        pyb.LED(LED_BLUE).toggle()
        time.sleep_ms(250)


# Function that contains the task code for toggling the yellow LED
def task2():
    while True:
        pyb.LED(LED_GREEN).toggle()
        time.sleep_ms(250)


############################################################
#
# Start script execution ...
#
############################################################
pyb.LED(LED_BLUE).on()
pyb.LED(LED_GREEN).off()

_thread.start_new_thread(task1, ())
_thread.start_new_thread(task2, ())

# Tracks seconds since program started
TimeStart = time.ticks_ms()

while True:
    time.sleep_ms(5000)
    SecondsLive = time.ticks_diff(time.ticks_ms(), TimeStart) / 1000
    print("Executing for ", SecondsLive, " seconds")