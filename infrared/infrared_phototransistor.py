import machine
import utime

adc_pin = 26
adc = machine.ADC(0)
threshold = 1000  

def is_signal_detected():
    adc_value = adc.read_u16()
    return adc_value > threshold

while True:
    if is_signal_detected():
        print("Signal detected!")
    else:
        print("No signal detected.")
    utime.sleep_ms(100)
