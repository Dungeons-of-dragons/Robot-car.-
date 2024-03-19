# The class `Servo` defines methods for controlling a servo motor based on specified angle ranges and
# pulse width values.
import machine
import math
from infrared_phototransistor import is_signal_detected  # Import the signal detection function

class Servo:
    def __init__(self,pin_id,min_us=544.0,max_us=2400.0,min_deg=0.0,max_deg=180.0,freq=50):
        self.pwm = machine.PWM(machine.Pin(pin_id))
        self.pwm.freq(freq)
        self.current_us = 0.0
        self._slope = (min_us-max_us)/(math.radians(min_deg)-math.radians(max_deg))
        self._offset = min_us
        
    def write(self,deg):
        self.write_rad(math.radians(deg))

    def read(self):
        return math.degrees(self.read_rad())
        
    def write_rad(self,rad):
        self.write_us(rad*self._slope+self._offset)
    
    def read_rad(self):
        return (self.current_us-self._offset)/self._slope
        
    def write_us(self,us):
        self.current_us=us
        self.pwm.duty_ns(int(self.current_us*1000.0))
    
    def read_us(self):
        return self.current_us

    def off(self):
        self.pwm.duty_ns(0)

    def reset_default(self):
        self.write(90)

    def servo_turn_right(self):
        self.reset_default()
        self.write(0)

    def servo_turn_left(self):
        self.reset_default()
        self.write(180)

    def scan_until_signal_detected(self, scan_times=5):
        for scan_count in range(scan_times):  
            for angle in range(0, 181):  
                self.write(angle) 
                if is_signal_detected(): 
                    return angle  
                machine.sleep(100)  
        return None  
