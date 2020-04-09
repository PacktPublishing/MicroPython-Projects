# main.py -- Chapter 6 - Visualizer Plotting Tool
##################################################################################
# Title                 :   Visualizer Plotting Tool
# Filename              :   RTPlotter.py
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
# Imports for using the serial port with command line
import serial
import argparse
import sys

# Imports for plotting data on a graph
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# The following can be used to test the data plot by importing data from
# a file located in a specific directory. See later in the script.
#from pathlib import Path 

# Defines that interval at which the plots in the script will be updated
# by the animate function. Updating at 100 ms or faster will result in 
# lab if you try to interact with the plot. 1 - 2 hertz provides a good
# balance.
INTERVAL_UPDATE_MS = 500

##
# Defines the serial port object that will be used to send and receive
# serial data.
##
ser = serial.Serial()

# Set generic paths
# See the following website for code description:
# https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
#data_folder = Path("C:/Python37/")
#file_to_open = data_folder / "example.txt"

# Setup Figure 1 for temperature plotting
fig = plt.figure()
fig.suptitle("Temperature", fontsize =16)
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Temperature (Degrees C)')

Figure1Manager = plt.get_current_fig_manager()
Figure1Manager.window.wm_geometry("+250+250")

# Setup Figure 2 for humidity plotting
fig2 = plt.figure()
fig2.suptitle("Humidity", fontsize =16)
ax2 = fig2.add_subplot(1,1,1)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Relative Humidity (%)')

Figure2Manager = plt.get_current_fig_manager()
Figure2Manager.window.wm_geometry("+900+250")

# Stores the x,y data for the temperature figure (1)
Fig1DataX = []
Fig1DataY = []

# Stores the x,y data for the humdiity figure (2)
Fig2DataX = []
Fig2DataY = []

# The animate function is called by the animate threads to update
# the figures. It first checks to see if there is any new serial data
# to process and if there is, will then empty the serial buffer. 
# The serial that is received will be parsed up to a newline character
# and split into its components by splitting on comas. The new data is
# then added to the appropriate dataset and the plots are redrawn.
def animate(i):
    InputString = ""

    # Check to see if there is data waiting to be processed.
    # If data is present, process it, otherwise, refresh the figures
    if(ser.inWaiting() > 0):

      # Process the serial stream until there are no characters waiting
      while(ser.inWaiting() > 0):

        SerData = ser.read(1)

        # A newline character signifies that the packet has been received.
        # When we receive a packet, process it and determine where it's data
        # should be stored at.
        if "\n" in SerData.decode("utf-8"):

          # Split the string data up when a coma is encountered
          SplitStrData = InputString.split(',')
          print(SplitStrData)

          # Check to see which list the data should be saved in
          if(int(SplitStrData[0]) == 1):
            Fig1DataX.append(float(SplitStrData[1]))
            Fig1DataY.append(float(SplitStrData[2]))

          elif(int(SplitStrData[0]) == 2):
            Fig2DataX.append(float(SplitStrData[1]))
            Fig2DataY.append(float(SplitStrData[2]))

          # Reset the variables for the next packet
          InputString = ""
          SplitStrData = None

        else:
          InputString = InputString + SerData.decode("utf-8")

    # Refresh the plots
    ax1.clear()
    ax1.plot(Fig1DataX, Fig1DataY)
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Temperature (Degrees C)')

    ax2.clear()
    ax2.plot(Fig2DataX, Fig2DataY)
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Relative Humidity (%)')
     

def main():
  # Create a command line argument parser object with a port option
  parser = argparse.ArgumentParser()
  parser.add_argument("--port", help="The communication port to connect to the target")

  # Parse the arguments that were passed into this script and store them in args
  args = parser.parse_args()

  # If the ports arguments was provided, setup the serial port 
  if args.port:
      # configure the serial connections
      ser.port = args.port
      ser.baudrate = 115200
      ser.parity = serial.PARITY_NONE
      ser.stopbits = serial.STOPBITS_ONE
      ser.bytesize = serial.EIGHTBITS

      try:
        ser.open()
        print(args.port + " Opened Successfully!")
      except Exception as e: print(e)
  else:
    print("A communication port was not provided using --port")
    sys.exit()

# Create the animation threads that will update the plots at our specified interval. 
  ani = animation.FuncAnimation(fig, animate, interval=INTERVAL_UPDATE_MS)
  ani2 = animation.FuncAnimation(fig2, animate, interval=INTERVAL_UPDATE_MS)
  plt.show()

if __name__ == "__main__":
    main()


