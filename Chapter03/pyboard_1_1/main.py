# main.py -- Chapter 3 - RGB Pushbutton Example
##################################################################################
# Title                 :   RGB Pushbutton Main
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

import micropython  # For emergency exception buffer
import pyb  # For uPython MCU features
from pyb import Pin  # For pin names
from pyb import Timer  # For PWM generation
from pyb import I2C  # For I2C functions
from button_rgb import PushButton_RGB  # For PushButton control
import sys  # For exit function

# Buffer for interrupt error messages
micropython.alloc_emergency_exception_buf(100)

############################################################
# Application Constants
############################################################
# Defines the PWM value for LED FULL On
LED_FULL_ON = 0

# Defines the PWM value for LED Full Off
LED_FULL_OFF = 100

# Defines the Duty Cycle increment rate
DUTY_CYCLE_CHANGE_RATE = 2.5

# Defines if the LED is brightening
PWM_COUNT_DOWN = True

# Defines if the LED is dimming
PWM_COUNT_UP = False

# Defines PCA7485 don't pressed state
BUTTON_NOT_PRESSED = 0xFF

# Defines PCA7485 button pressed state
BUTTON_PRESSED = 0xFE

# Defines the maximum state supported by the pushbutton application
MAX_SYSTEM_STATE = 4

# Defines the address the I/O expander is on
PCA8574_ADDRESS = 0x38

# Defines the I2C bus that will be used
I2C_BUS1 = 1

############################################################
# Application Variables
############################################################

# List object that contains the duty cycle for RGB
# Valid values are 0 - 100. Due to the hardware, the
# duty cycle is reversed! 0% provides a ground which is
# full on to the LED's. 100% is full voltage and LED is off.
DutyCycle = 100

# Defines the pins used to drive the RGB duty cycle
PinList = [Pin('X1'), Pin('X2'), Pin('X3')]

# Defines the timers used to generate the PWM
TimerList = [2, 2, 2]

# Defines the timer frequency in Hz for the RGB
FrequencyList = [1000, 1000, 1000]

# Specifies the timer channels used to drive the RGB LED's
TimerChList = [1, 2, 3]

# Holds the button state based on how many times its been
# pressed
System_State = 0

# If 0, the duty cycle is counting down.
# If 1, the duty cycle is counting up. 
PwmDirection = 0

# Holds the button state from the last time it was read.
# This is used to determine if the button has been released.
ButtonLastState = False


# Setup the MCU and application code to starting conditions
# The blue LED will start on, the yellow LED will be off
def system_init():
    print("Initializing system ...")
    print("Starting application ...")


############################################################
#
# Start script execution ...
#
############################################################
# Initialize the system
system_init()

try:
    i2c = I2C(I2C_BUS1, I2C.MASTER, baudrate=100000)
    I2C_List = i2c.scan()

    if I2C_List:
        print("I2C Slaves Present =", I2C_List)
    else:
        print("There are no I2C devices present! Exiting application.")
        sys.exit(0)
except Exception as e:
    sys.print_exception(e)

try:
    RGB_Button = PushButton_RGB(PinList, TimerList, FrequencyList, TimerChList, i2c, PCA8574_ADDRESS)
except Exception as e:
    sys.print_exception(e)

try:
    # Make sure that the I2C device is present before proceeding.
    RGB_Button.RGB.Write(LED_FULL_OFF, LED_FULL_OFF, LED_FULL_OFF)
except Exception as e:
    sys.print_exception(e)

# Main application loop
while True:

    # Make sure we have an I2C device to talk to, if so, try to read from it
    try:
        PushButton = RGB_Button.DeviceIO.Read()
    except Exception as e:
        sys.print_exception(e)
        print("Exiting application ...")
        sys.exit(0)

    # Check the Pushbutton to see if it has been pressed and released.
    # When released, move to the next system state.
    if PushButton == BUTTON_NOT_PRESSED:
        if ButtonLastState == True:
            ButtonLastState = False
            DutyCycle = LED_FULL_OFF
            System_State += 1

            if System_State >= MAX_SYSTEM_STATE:
                System_State = 0
    elif PushButton == BUTTON_PRESSED:
        ButtonLastState = True

    # The example application will toggle the LED from full on to
    # full off and then back again.
    if PwmDirection == PWM_COUNT_DOWN:
        DutyCycle -= DUTY_CYCLE_CHANGE_RATE

        if DutyCycle <= LED_FULL_ON:
            PwmDirection = PWM_COUNT_UP
    else:
        DutyCycle += DUTY_CYCLE_CHANGE_RATE

        if DutyCycle >= LED_FULL_OFF:
            PwmDirection = PWM_COUNT_DOWN

    # This is a simple "State Machine" that will run different
    # colors and patterns based on how many times the button
    # has been pressed
    try:
        if System_State == 0:
            RGB_Button.RGB.Write(DutyCycle, LED_FULL_OFF, LED_FULL_OFF)
        elif System_State == 1:
            RGB_Button.RGB.Write(LED_FULL_OFF, DutyCycle, LED_FULL_OFF)
        elif System_State == 2:
            RGB_Button.RGB.Write(LED_FULL_OFF, LED_FULL_OFF, DutyCycle)
        elif System_State == 3:
            RGB_Button.RGB.Write(DutyCycle, DutyCycle, DutyCycle)
    except Exception as e:
        sys.print_exception(e)

    # This sets a periodic delay so that the DutyCycle doesn't
    # change too fast
    pyb.delay(25)
