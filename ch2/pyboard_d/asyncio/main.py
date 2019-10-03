# main.py -- put your code here!
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

import uasyncio as asyncio

# Define LED color constants
LED_RED = 1
LED_GREEN = 2
LED_BLUE = 3


# Function that contains the task code for toggling the blue LED
async def task1():
    while True:
        pyb.LED(LED_BLUE).toggle()
        await asyncio.sleep_ms(150)


# Function that contains the task code for toggling the yellow LED
async def task2():
    while True:
        pyb.LED(LED_GREEN).toggle()
        await asyncio.sleep_ms(150)

# Setup the MCU and application code to starting conditions
# The blue LED will start on, the yellow LED will be off
pyb.LED(LED_BLUE).on()
pyb.LED(LED_GREEN).off()

loop = asyncio.get_event_loop()
loop.create_task(task1())
loop.create_task(task2())
loop.run_forever()
