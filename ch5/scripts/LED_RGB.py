# LED_RGB.py -- Chapter 3 - RGB Pushbutton Example
##################################################################################
# Title                 :   RGB Pushbutton Example
# Filename              :   LED_RGB.py
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
# - Frequency is the startign PWM frequency
# - Channels is a list of timer channels to use to generate
#   the PWM.
#
# Use RGB_Set to with a value between 0 and 100 for each LED
#
############################################################
class RGB_Generator():
  # Initializer / Instance Attributes
    def __init__(self,PinList,Timer, Frequency, Channels):
#        self.TimerR = pyb.Timer(2, freq=1000)
        self.TimerR = pyb.Timer(Timer[0], freq=Frequency[0]) 
        self.TimerG = pyb.Timer(Timer[1], freq=Frequency[1])
        self.TimerB = pyb.Timer(Timer[2], freq=Frequency[2])

        self.R_Ch = self.TimerR.channel(Channels[0], pyb.Timer.PWM, pin=PinList[0])
        self.G_Ch = self.TimerG.channel(Channels[1], pyb.Timer.PWM, pin=PinList[1])
        self.B_Ch = self.TimerB.channel(Channels[2], pyb.Timer.PWM, pin=PinList[2])

    def Write(self,Red, Green, Blue):

        self.R_Ch.pulse_width_percent(Red)
        self.G_Ch.pulse_width_percent(Green)
        self.B_Ch.pulse_width_percent(Blue)