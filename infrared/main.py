import machine
import utime
from maf import MovingAverageFilter

maf = MovingAverageFilter(10)

adc_pin = 27
#adc_pin2 = 28
adc = machine.ADC(0)
threshold =  700 

while True:
    raw_adc_value = adc.read_u16()
#    raw_adc_value2 = adc.read_u16()
    maf.add(raw_adc_value)
#    maf.add(raw_adc_value2)
    adc_value = maf.get_average()
#    adc_value2 = maf.get_average()
    print(adc_value)
    utime.sleep(0.1)