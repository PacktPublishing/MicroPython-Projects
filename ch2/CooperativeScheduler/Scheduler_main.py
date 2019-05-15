# main.py - Chapter 2 Cooperative Scheduler Test
##################################################################################
# Title                 :   Scheduler Main
# Filename              :   Scheduler_main.py
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
import tasks
import scheduler
import micropython

# Buffer for interrupt error messages
micropython.alloc_emergency_exception_buf(100)

# Setup the MCU and application code to starting conditions
# The blue LED will start on, the yellow LED will be off
def System_Init():
  print("Initializing system ...")
  pyb.LED(4).on()
  pyb.LED(3).off()
  print("Starting application ...")

############################################################
#
# Start script execution ...
#
############################################################
# Initialize the system
System_Init()

# Create a scheduler object
TaskScheduler = scheduler.Scheduler()

# Define the system tasks, interval and start tick
Task1=[tasks.TaskBlueLed,100, 0]
Task2=[tasks.TaskYellowLed, 100, 0]
Task3=[tasks.TaskAccelerometer, 500, 0]

# Add the tasks to the scheduler
TaskScheduler.AddTask(Task1)
TaskScheduler.AddTask(Task2)
TaskScheduler.AddTask(Task3)

# Main execution loop
while TaskScheduler.ExitState == False:
    # Run the scheduler
    TaskScheduler.Run()