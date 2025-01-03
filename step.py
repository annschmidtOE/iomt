from stepper import Stepper 
from machine import Pin

in1 = Pin(16,Pin.OUT)
in2 = Pin(17,Pin.OUT)
in3 = Pin(5,Pin.OUT)
in4 = Pin(18,Pin.OUT)

s1 = Stepper.create(in1, in2, in3, in4, delay=1)

#s1.step(18)
#s1.step(18-1)
#s1.step(1820)
while True:
    s1.step(1820,1)
    s1.step(1820,-1)
#s1.step(360*2)