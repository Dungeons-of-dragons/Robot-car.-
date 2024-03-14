from machine import Pin
import utime

class UltraSonic:
    def __init__(self, echo, trig):
        self.echo = echo
        self.trig = trig
    def distance (self):        
        new_reading = False
        counter = 0
        distance = 0
        duration = 0
        
        echoPIN = Pin(self.echo, Pin.IN)
        trigPIN = Pin(self.trig, Pin.OUT)
        
        trigPIN.value(0)
        utime.sleep_us(2)
        trigPIN.value(1)
        utime.sleep_us(10)
        trigPIN.value(0)
        utime.sleep_us(2)
        
        while not echoPIN.value():
            # pass
            counter += 1
            if counter == 5000:
                new_reading = True
                break

        if new_reading:
            return False
        
        startT = utime.ticks_us()/1000000
        while echoPIN.value(): pass
        feedbackT = utime.ticks_us()/1000000
     
        if feedbackT == startT:
            distance = "N/A"
        else:
            duration = feedbackT - startT
            soundSpeed = 34300 # cm/s
            distance = duration * soundSpeed / 2
            distance = round(distance, 1)
     
        return distance
