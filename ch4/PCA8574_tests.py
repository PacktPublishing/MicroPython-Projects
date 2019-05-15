# PCA8574_tests.py -- Chapter 4 - Test Casd Example
##################################################################################
# Title                 :   PCA8574 Test Cases
# Filename              :   PCA8574_tets.py
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

from PCA8574 import PCA8574_IO
from pyb import I2C
from pyb import Pin

# Defines the I2C bus that will be used
I2C_BUS1 = 1

def PCA8574_tests():

	try: 
	  # Initialize I2C 1
	  i2c = I2C(I2C_BUS1, I2C.MASTER, baudrate=100000)
	  # returns list of slave addresses
	  I2C_List = i2c.scan() 

	  if I2C_List: 
	    print("I2C Slaves Present =", I2C_List)
	  else:
	    print("There are no I2C devices present! Exiting application.")
	    sys.exit(0)
	except Exception as e: print(e)

	p_out = Pin('PD14', Pin.OUT_PP)
	p_out.high()

	# Test that we can initialize the object
	try:
		PCA8574_Object = PCA8574_IO(i2c, I2C_List[0])
		print("PCA8574, Object Creation, Passed")
	except:
		print("PCA8574, Object Creation, Failed")

	try:	
		PCA8574_Object1 = PCA8574_IO(i2c, 256)
		print("PCA8574, I2C Address Out-of-Bounds, Failed")
	except:
		print("PCA8574, I2C Address Out-of-Bounds, Passed")

	#######
	# Test reading the switch
    #######

	# Set the switch to not pressed
	p_out.high()
	Result = PCA8574_Object.Read()
	if Result is 0xFF:
		print("PCA8574, LSB I/O - High, Passed")
	else:
		print("PCA8574, LSB I/O - High, Failed,", Result)

	# Set the switch to pressed
	p_out.low()
	Result = PCA8574_Object.Read()
	if Result is 0xFE:
		print("PCA8574, LSB I/O - Low, Passed")
	else:
		print("PCA8574, LSB I/O - Low, Failed,", Result)

