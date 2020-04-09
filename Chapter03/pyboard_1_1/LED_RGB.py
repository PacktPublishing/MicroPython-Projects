# LED_RGB.py -- Chapter 3 - RGB Pushbutton Example
##################################################################################
# Title                 :   LED RGB
# Filename              :   LED RGB.py
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


############################################################
#
# RGB_Generator contains the functionality required to 
# initialize and control a red, green and blue LED using 
# a PWM. The class requires the following:
# - The PinList is a list of pins to use for the LED's
# - Timer is a timer peripheral
# - Frequency is the starting PWM frequency
# - Channels is a list of timer channels to use to generate
#   the PWM.
#
# Use RGB_Set to with a value between 0 and 100 for each LED
#
############################################################
class RGBGenerator:
    """
    This is a class for controlling an RGB LED.
    """

    def __init__(self, pinlist, timer, frequency, channels):
        """
        The constructor for initializing the RGB Generator.

        :param pinlist: list of pins that the LED's are located on
        :param timer: list of timers that are used to generate the PWM signals
        :param frequency: list of frequencies that the PWM's will run at
        :param channels: the timer channel that is used to output the PWM
        """
        self.TimerR = pyb.Timer(timer[0], freq=frequency[0])
        self.TimerG = pyb.Timer(timer[1], freq=frequency[1])
        self.TimerB = pyb.Timer(timer[2], freq=frequency[2])

        self.R_Ch = self.TimerR.channel(channels[0], pyb.Timer.PWM, pin=pinlist[0])
        self.G_Ch = self.TimerG.channel(channels[1], pyb.Timer.PWM, pin=pinlist[1])
        self.B_Ch = self.TimerB.channel(channels[2], pyb.Timer.PWM, pin=pinlist[2])

    def write(self, red, green, blue):
        """
        Writes the desired LED PWM to the hardware.

        :param red: The duty cycle from 0 to 100 for the red LED
        :param green: The duty cycle from 0 to 100 for the green LED
        :param blue:  The duty cycle from 0 to 100 for the blue LED
        """
        self.R_Ch.pulse_width_percent(red)
        self.G_Ch.pulse_width_percent(green)
        self.B_Ch.pulse_width_percent(blue)
