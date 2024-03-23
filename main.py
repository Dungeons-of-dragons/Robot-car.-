from time import sleep
from machine import Pin, I2C
from imu import MPU6050
from ultraSonic import UltraSonic
from motorDriver import L298N, Motors, my_sleep
import utime

LEFT_ENA = 10
LEFT_IN1 = 12
LEFT_IN2 = 11
RIGHT_ENA = 15
RIGHT_IN1 = 13
RIGHT_IN2 = 14
DEFAULT_SPEED = 65534
echo = 7
trigger = 8
ultra = UltraSonic(echo, trigger)
motors=Motors()
dist = 25


def obstacle_detection():
    read_distance = ultra.distance()
    if read_distance < dist:
        return True
    else:
        return False

def obstacle_avoidance():
    if obstacle_detection():
        motors.reverse()
        my_sleep(1000)
        motors.stop()

i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=400000)
imu = MPU6050(i2c)

while True:
    gx=round(imu.gyro.x)
    gy=round(imu.gyro.y)
    gz=round(imu.gyro.z)
    
    print("gx",gx,"\t","gy",gy,"\t","gz",gz,"\t","        ",end="\r")
    sleep(1)
    print (" Distance: " + str(ultra.distance())+ "   ", end='\r')
    motors.start()
    my_sleep(500)


