# This is actuator program
def water_plants():
    a.digital_write(water_pump,1)
    #read soil moisture pin
    soil_moisture= a.digital_read(5)
    print (" plants are watered")

def light_on():
    a.digital_write(led_pin,1)

def light_off():
    a.digital_write(led_pin,0)

def fan_off():
    a.digital_write(fan,0)

def fan_on():
    a.digital_write(fan,1)

def water_null():
    a.digital_write(water_pump,0)

#read ldr values
def ldr_value():
    analog_val = a.analog_read(0)
    analog_val=int((analog_val/1023.)*100)
    return analog_val
    



