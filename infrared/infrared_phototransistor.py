import machine
import utime
from maf import MovingAverageFilter

maf = MovingAverageFilter(5)

adc_pin = 27
adc = machine.ADC(0)
threshold =  700 

def is_signal_detected():
    raw_adc_value = adc.read_u16()
    maf.add(raw_adc_value)
    adc_value = maf.get_average()
    return adc_value > threshold


