from ultraSonic import UltraSonic
from MotorDriver import L298N, Motors, my_sleep
import utime

LEFT_ENA = 0
LEFT_IN1 = 2
LEFT_IN2 = 1
RIGHT_ENA = 3
RIGHT_IN1 = 5
RIGHT_IN2 = 4
DEFAULT_SPEED = 65534
echo = 7
trigger = 8
ultra = UltraSonic(echo, trigger)
motors=Motors()
dist = 10


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


while True:
    print (" Distance: " + str(ultra.distance())+ "   ", end='\r')
    motors.manual_control(30000, 30000)
    my_sleep(500)


