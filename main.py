from time import sleep
from machine import Pin, I2C
from imu import MPU6050

i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=400000)
imu = MPU6050(i2c)

while True:
    gx=round(imu.gyro.x)
    gy=round(imu.gyro.y)
    gz=round(imu.gyro.z)
    
    print("gx",gx,"\t","gy",gy,"\t","gz",gz,"\t","        ",end="\r")
    sleep(1)