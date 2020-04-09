# button_rgb.py -- Chapter 3 - RGB Pushbutton Example
##################################################################################
# Title                 :   Button RGB
# Filename              :   button_rgb.py
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
from LED_RGB import RGB_Generator


############################################################
#
# PushButton_RGB is a composition of the RGB_Generator and
# PCA8574_IO classes. All pushbutton functionality is
# accessed through the instantiated classes. 
#
############################################################
class PushButtonRGB:

    # Initializer / Instance Attributes
    def __init__(self, pinist, timer, frequency, channels, i2cobject, slaveaddress):
        self.RGB = RGB_Generator(pinlist, timer, frequency, channels)
        self.DeviceIO = PCA8574_IO(i2cobject, slaveaddress)
