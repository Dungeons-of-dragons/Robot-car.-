from machine import Pin, time_pulse_us
import time

SOUND_SPEED=340 # speed of sound in air
TRIG_PULSE_DURATION_US=10

trig_pin = Pin(3 Pin.OUT)  
echo_pin = Pin(2, Pin.IN)  

def get_distance():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   dist = (timepassed * 0.0343) / 2
   return dist

 # def stop(self):
       # self.IN1.value(0)
        #self.IN2.value(0)
        #self.ismoving = False
        #self.Direction = 'STOP'

  while True:
    distance=get_distance() #Getting distance in cm
    print("Distance:", distance, "cm")
    #Defining direction based on conditions
    if distance < 25:
        stop(self)
        