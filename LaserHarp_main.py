# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
LaserHarp_main
--------------------------------------------------------------------------
License:   
Copyright 2019 Jason Dennis

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------
Python code for running Laser Harp Controller 

"""

import time
import threading 
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM


# ------------------------------------------------------------------------
# Constants / Global Variables 
# ------------------------------------------------------------------------

LDR_pin1                          = "AIN0"
LDR_pin2                          = "AIN1"
LDR_pin3                          = "AIN2"
LDR_pin4                          = "AIN3"
LDR_pin5                          = "AIN4"
LDR_pin6                          = "AIN5"
LDR_pin7                          = "AIN6"
LDR_pin8                          = "AIN7"
piezo_pin                         = "P2_3"
BUTTON0                           = "P2_2"
# ------------------------------------------------------------------------
# Musical Note Library 
# ------------------------------------------------------------------------
NOTE_A7 = 3520
NOTE_B6 = 1976
NOTE_C6 = 1047
NOTE_D6 = 1175
NOTE_E6 = 1319
NOTE_F7 = 2794
NOTE_G6 = 1568

# ------------------------------------------------------------------------
# Main Function
# ------------------------------------------------------------------------
def setup():
    """Setup the hardware components."""
    

    # Initialize Button
    ADC.setup()
    GPIO.setup(BUTTON0, GPIO.IN)

# End def

def play_note(pin, vout):
    """ Play's note based on pin and vout inputs"""
    
    PWM.stop(piezo_pin)
    if (pin == "AIN0" and vout < 0.80):
        note = NOTE_A7
        PWM.start(piezo_pin, 50, note)
        time.sleep(3)
        PWM.stop(piezo_pin)
    elif (pin == "AIN1" and vout < 0.80):
        note = NOTE_B6
        PWM.start(piezo_pin, 50, note)
        time.sleep(3)
        PWM.stop(piezo_pin)
    elif (pin == "AIN2" and vout < 0.80):
        note = NOTE_C6
        PWM.start(piezo_pin, 50, note)
        time.sleep(3)
        PWM.stop(piezo_pin)
    elif (pin == "AIN3" and vout < 0.83 ):
        note = NOTE_D6
        PWM.start(piezo_pin, 50, note)
        time.sleep(3)
        PWM.stop(piezo_pin)
    elif (pin == "AIN4" and vout < 0.80):
        note = NOTE_E6 
        PWM.start(piezo_pin, 50, note)
        time.sleep(3)
        PWM.stop(piezo_pin)
    elif (pin == "AIN5" and vout < 0.40):
        note = NOTE_F7 
        PWM.start(piezo_pin, 50, note)
        time.sleep(3)
        PWM.stop(piezo_pin)
    elif (pin == "AIN6" and vout < 0.38):
        note = NOTE_G6
        PWM.start(piezo_pin, 50, note)
        time.sleep(3)
        PWM.stop(piezo_pin)
    elif (pin == "AIN7" and vout < 0.23):
        note = NOTE_A7
        PWM.start(piezo_pin, 50, note)
        time.sleep(3)
        PWM.stop(piezo_pin)
  
#end def 

# ------------------------------------------------------------------------
# Library Class
# ------------------------------------------------------------------------

class LDRThreading(threading.Thread):
    
    # initializes variables 
    button = None 
    pin = None 
    
    def __init__(self, button, pin):
        """Class initialization method"""
        threading.Thread.__init__(self)
        self.button = button 
        self.pin = pin
    # End def 
    
    def run(self):
        """
        Class run method
        
        Called automatically when a new thread is started.
        """
        
        while(True): 
            V_out = ADC.read(self.pin)
            play_note(self.pin, V_out)
            time.sleep(0.5)
                
    # End def 
    
    
# End Class 



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------


if __name__ == '__main__':
    
    setup()
    
    #start threading
    
    p1 = LDRThreading(button = BUTTON0, pin = LDR_pin1)
    p2 = LDRThreading(button = BUTTON0, pin = LDR_pin2)
    p3 = LDRThreading(button = BUTTON0, pin = LDR_pin3)
    p4 = LDRThreading(button = BUTTON0, pin = LDR_pin4)
    p5 = LDRThreading(button = BUTTON0, pin = LDR_pin5)
    p6 = LDRThreading(button = BUTTON0, pin = LDR_pin6)
    p7 = LDRThreading(button = BUTTON0, pin = LDR_pin7)
    p8 = LDRThreading(button = BUTTON0, pin = LDR_pin8)
    
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    
    #end threading 
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()

    
    #end def 
