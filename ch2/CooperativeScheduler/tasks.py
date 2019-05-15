# tasks - Chapter 2 Cooperative Scheduler Example
##################################################################################
# Title                 :   Tasks
# Filename              :   Tasks.py
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

import pyb
import sys
import scheduler

# define LED color constants
LED_RED = 0
LED_GREEN = 1
LED_YELLOW = 2
LED_BLUE = 3

# Define a list of LED objects
LEDs = [pyb.LED(1), pyb.LED(2)]
LEDs.append(pyb.LED(3))
LEDs.append(pyb.LED(4))

# Resultant Accelerometer Vector
VectorSum = 0

# TaskYellowLed is used to toggle the LED. The
# toggle rate is determined by the application.
def TaskBlueLed():

    LEDs[LED_BLUE].toggle()

    return

# TaskYellowLed is used to toggle the LED. The
# toggle rate is determined by the application.
def TaskYellowLed():

    LEDs[LED_YELLOW].toggle()

    return

# Accelerometer_Sample is used to sample the pyboard
# accelerometer and generate a vector result.
# toggle rate is determined by the application.
def Accelerometer_Sample():
    # Create an object to the accelerometer
    Accelerometer = pyb.Accel()

    # Retrieve the filtered data
    Data = Accelerometer.filtered_xyz()

    # Clear the sum before recalculating on new data
    VectorData = 0

    # Calculate the vector sum
    for axis in Data:
        VectorData += axis**2

    # Calculate the square root
    VectorData = VectorData ** 0.5

    return VectorData 

# Task AccelerometerSample samples the sensor and prints
# the result to the REPL
def TaskAccelerometer():

    VectorSum = Accelerometer_Sample()

    print("VectorSum =", "{0:.2f}".format(VectorSum))

    return