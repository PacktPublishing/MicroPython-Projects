# main.py -- Chapter 4 - Test Harness Example
##################################################################################
# Title                 :   Test Harness Example
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
from test_harness import TestHarness_Run 

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

print("Starting Tests ...")
TestHarness_Run()
print("Testing Completed")

while True:
  i = 0