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
class Pca8574_Io:
    """ This is a class for accessing the PCA8574 IO chip. """

    def __init__(self, i2c_object, slave_address):
        """
        The constructor for the PCA8574 class.

        :param i2c_object: The MicroPython i2c bus object that the PCA8574 is connected to
        :param slave_address: The i2c address assigned to the PCA8574 object
        """
        assert slave_address < 256, "Slave Address >= 256!"

        self.Address = slave_address
        self.I2C = i2c_object

    def read(self):
        """
        The function to read the I/O states of the PCA8574.

        :return: integer value of the 8-bit I/O port
        """
        try:
            return ord(self.I2C.recv(1, self.Address))
        except:
            print("Unable to retrieve I/O status")
            return 0xFF

    def write(self, state):
        """
        The function to write I/O states to the PCA8574.

        :param state: The integer value that represents the desired I/O state on the 8-bit port
        :return:
        """
        assert state < 256, "State >= 256"
        try:
            self.I2C.send(state, self.Address)
        except:
            print("Unable to set I/O state")
