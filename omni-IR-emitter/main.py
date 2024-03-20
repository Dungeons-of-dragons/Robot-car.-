import time
from rc_servo import Servo

# Initialize the servo on pin 26
my_servo = Servo(pin_id=26)

start_time = time.time() 


def last_angle():
    """
    A function that continuously updates a servo's position, moving it in increments of 1 degree from 0 to 180 degrees. 
    It breaks the loop after 10 seconds have passed, reads the final angle of the servo, and returns it.
    """
    current_angle = 0 
    while True:
        # Update the servo's position
        my_servo.write(current_angle)
    
        # Wait for a short period before moving to the next angle
        time.sleep(0.5)  
    
        current_angle += 1
        if current_angle > 180:
            current_angle = 0  #make it rotate
            
    
        # Check if 20 seconds have passed
        if time.time() - start_time > 10:
            break
    
    
    # After 20 seconds, read and print the servo's current angle
    last_angle = my_servo.read()
    return last_angle

