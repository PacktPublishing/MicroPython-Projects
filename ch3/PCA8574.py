# PCA8574.py -- Chapter 3 - RGB Pushbutton Example
##################################################################################
# Title                 :   PCA8574 Driver
# Filename              :   PCA8574.py
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
# PCA8574_IO contains the functionality required to 
# initialize and control a PCA8574 I/O expander chip. 
# The class requires the following:
# - I2CObject which is an initialized I2C object
# - SlaveAddress which is the address of the target device
#
# Use PCA8574_ChannelRead to read all 8 channels at once
# Use PCA8574_AllSet to write all 8 channels at once
#
############################################################
class PCA8574_IO():
# Initializer / Instance Attributes
  def __init__(self,I2CObject, SlaveAddress):
      assert SlaveAddress < 256, "Slave Address must be less than 256!"

      self.Address = SlaveAddress
      self.I2C = I2CObject

  def Read(self):
    try:
      return ord(self.I2C.recv(1, self.Address))
    except:
      print("Unable to retrieve I/O status")
      return 0xFF 

  def Write(self,State):
    assert State < 256, "Maximum state is 255"
    try:
      self.I2C.send(State, self.Address)
    except:
      print("Unable to set I/O state")