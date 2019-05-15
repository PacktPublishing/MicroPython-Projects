# main.py -- Chapter 6 - Visualizer Test Code
##################################################################################
# Title                 :   Visualizer Test Code
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
from pyb import UART

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
uart4 = UART(4, 115200)                         
uart4.init(115200, bits=8, parity=None, stop=1) 

# Create variables to store time, temperature and humidity
Time = 0.0
Temperature = -20.0
Humidity = 34.5
TempDir = 1
HumidDir = 1

# Main application loop
while True:

  # Update Time
  Time = Time + 1.0

  # Update Temperature
  if TempDir == 1:
    Temperature = Temperature + 1
    if Temperature >= 20:
      TempDir = 0
  else:
    Temperature = Temperature - 1
    if Temperature <= -20:
      TempDir = 1

  #Update Humidity
  if HumidDir == 1:
    Humidity = Humidity + 0.5
    if Humidity >= 35:
      HumidDir = 0
  else:
    Humidity = Humidity - 0.5
    if Humidity <= 25:
      HumidDir = 1

  # Create string data
  TemperatureDataString = '1,' + str(Time) + ',' + str(Temperature) +'\n'
  HumidityDataString = '2,' + str(Time) + ',' + str(Humidity) +'\n'

  # Send sensor data
  print(TemperatureDataString)
  uart4.write(TemperatureDataString)

  print(HumidityDataString)
  uart4.write(HumidityDataString)

  # Delay the loop by 1 second
  pyb.delay(1000)