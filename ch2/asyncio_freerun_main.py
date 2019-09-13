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

# Function that contains the task code for toggling the blue LED
async def Led_BlueToggle():
    while True:
      pyb.LED(3).toggle()
      await asyncio.sleep_ms(500)

    return 

# Function that contains the task code for toggling the yellow LED
async def Led_YellowToggle():
    while True:
      pyb.LED(4).toggle()
      await asyncio.sleep_ms(500)

    return 

# Setup the MCU and application code to starting conditions
# The blue LED will start on, the yellow LED will be off
def System_Init():
  print("Initializing system ...")
  pyb.LED(3).on()
  pyb.LED(4).off()
  print("LED's initialized ...")

System_Init()
loop = asyncio.get_event_loop()
loop.create_task(Led_BlueToggle())
loop.create_task(Led_YellowToggle())
loop.run_forever()