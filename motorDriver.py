import time
from machine import Pin, PWM

led = Pin(25, Pin.OUT)


def my_sleep(delay):
    start = time.ticks_ms()
    end = start + delay
    while time.ticks_ms() < end:
        pass


"""
comments below is for testing
"""
# start_time = time.time()
# my_sleep(1000)
# led.toggle()
# print("--- %s seconds ---" % (time.time() - start_time))


class L298N:
    def __init__(self, ENA, IN1, IN2):
        self.IN1 = IN1
        self.IN2 = IN2
        self.pwm = ENA
        self.speed = 40000
        self.ismoving = False
        self.direction = "STOP"
        self.time = 0

    def forward(self):
        self.IN1.value(1)
        self.IN2.value(0)
        self.ismoving = True
        self.direction = "FORWARD"

    def backward(self):
        self.IN1.value(0)
        self.IN2.value(1)
        self.ismoving = True
        self.direction = "BACKWARD"

    def stop(self):
        self.IN1.value(0)
        self.IN2.value(0)
        self.ismoving = False
        self.Direction = "STOP"

    def setSpeed(self, speed):
        self.pwm.freq(15000)
        self.speed = speed
        self.pwm.duty_u16(speed)

    def getSpeed(self):
        return self.speed

    def getDirection(self):
        return self.direction

    def run(self, direction):
        self.direction = direction
        if self.direction == "FORWARD":
            self.forward()
        elif self.direction == "BACKWARD":
            self.backward()
        elif self.direction == "STOP":
            self.stop()
        else:
            pass

    def forwardFor(self, Time):
        self.time = Time
        self.forward()
        my_sleep(self.time)
        self.stop()

    def backwardFor(self, Time):
        self.time = Time
        self.backward()
        my_sleep(self.time)
        self.stop()

    def runFor(self, direction, Time):
        self.direction = direction
        self.time = Time
        if self.direction == "FORWARD":
            self.forward()
            my_sleep(self.time)
            self.stop()
        elif self.direction == "BACKWARD":
            self.backward()
            my_sleep(self.time)
            self.stop()
        elif self.direction == "STOP":
            self.stop()
            my_sleep(self.time)
        else:
            pass

    def isMoving(self):
        if self.ismoving is True:
            print("True")
        elif self.ismoving is False:
            print("False")
        else:
            pass


DEFAULT_SPEED = 65534
LEFT_ENA = 0
LEFT_IN1 = 1
LEFT_IN2 = 2
RIGHT_ENA = 3
RIGHT_IN1 = 4
RIGHT_IN2 = 5


class Motors:
    """
    Controls the Motors
    speed needs to be between 25000 and 65534
    """

    def __init__(self):
        self.left_motor = L298N(
            PWM(Pin(LEFT_ENA)), Pin(LEFT_IN1, Pin.OUT), Pin(LEFT_IN2, Pin.OUT)
        )
        self.right_motor = L298N(
            PWM(Pin(RIGHT_ENA)), Pin(RIGHT_IN1, Pin.OUT), Pin(RIGHT_IN2, Pin.OUT)
        )
        self.direction = "stop"

    def turn_right(self, speed=DEFAULT_SPEED):
        self.left_motor.setSpeed(speed)
        self.left_motor.forward()
        self.right_motor.stop()
        self.direction = "right"

    def turn_left(self, speed=DEFAULT_SPEED):
        self.right_motor.setSpeed(DEFAULT_SPEED)
        self.right_motor.forward()
        self.left_motor.stop()
        self.direction = "left"

    def start(self, speed=DEFAULT_SPEED):
        self.left_motor.setSpeed(speed)
        self.right_motor.setSpeed(speed)
        self.left_motor.forward()
        self.right_motor.forward()
        self.direction = "forward"

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
        self.direction = "stop"

    def reverse(self, speed=DEFAULT_SPEED):
        self.left_motor.setSpeed(speed)
        self.right_motor.setSpeed(speed)
        self.left_motor.backward()
        self.right_motor.backward()
        self.direction = "reverse"

    def manual_control(self, left_speed=DEFAULT_SPEED, right_speed=DEFAULT_SPEED):
        self.left_motor.setSpeed(abs(left_speed))
        if left_speed > 0:
            self.left_motor.forward()
        else:
            self.left_motor.backward()

        self.right_motor.setSpeed(abs(right_speed))
        if right_speed > 0:
            self.right_motor.forward()
        else:
            self.right_motor.backward()
        self.direction = "manual"


# motors=Motors()
# motors.manual_control(-65534, 65534)
