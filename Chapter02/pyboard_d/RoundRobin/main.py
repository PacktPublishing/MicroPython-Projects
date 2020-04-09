# main.py -- Chapter 2 - Round Robin Example
##################################################################################
# Title                 :   Round Robin Main
# Filename              :   RoundRobin_main.py
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
import pyb   # For uPython MCU features

# define LED color constants
LED_RED = 1
LED_GREEN = 2
LED_BLUE = 3


def task1():
    pyb.LED(LED_BLUE).toggle()


def task2():
    pyb.LED(LED_GREEN).toggle()


############################################################
#
# Start script execution ...
#
############################################################
# Setup the MCU and application code to starting conditions
# The blue LED will start on, the yellow LED will be off
pyb.LED(LED_BLUE).on()
pyb.LED(LED_GREEN).off()

# Main application loop
while True:
    # Run the first task
    task1()

    # Run the second task
    task2()

    # Delay 150 ms
    pyb.delay(150)