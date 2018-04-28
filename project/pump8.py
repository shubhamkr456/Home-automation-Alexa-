
#from temperature import *
import time
import RPi.GPIO as GPIO 

if __name__ == '__main__' :
    print("Establishing connection with Raspberry")
    GPIO.setmode(GPIO.BCM)            ## Use BOARD pin numbering

    #pins Setup
    led_pin = 4
    water_pump=12
    soil= 20 
    pir= 16
    fan = 6
    GPIO.cleanup()
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.setup(water_pump, GPIO.OUT)
    GPIO.setup(fan, GPIO.OUT)

    GPIO.setup(soil, GPIO.IN)
    GPIO.setup(pir, GPIO.IN)


    

    time.sleep(0.0001)
    GPIO.output(led_pin,0)
    GPIO.output(water_pump,0)
    GPIO.output(fan,0)
    
    #f= open("abc.txt", "r")
    #content= f.read()
    print("Entering tthe infinite loop")
    while(True):
        print("Entered loop")
        if GPIO.input(soil) == False:
            GPIO.output(water_pump,1)
            print('water plants')
        else:
      #f  while GPIO.input(soil) == True:
            print('Dont water plants')
            GPIO.output(water_pump,0)




        m =GPIO.input(pir)
        print("Entering loop")
        print(m)
        if(m==1):
            print('motion detcted')
            f=open("abc.txt", "r")
            content= f.read()
            f.close()
         
            while(content == 'resumed' and m==1):
                try:
                    #analog_val = a.analog_read(0)
                    #analog_val=int((analog_val/1023.)*100)
                    #print(analog_val)
                    #if analog_val<50 and m==1: #pir values
                        #light_on()
                    #else:
                        #light_off()
                    ##tempe=temp()
                    #print(tempe)
                    #if tempe[0]>=27 and m==1: # for fan assign temperature
                     #   GPIO.output(fan,HIGH)
                    #else:
                      #  GPIO.output(fan,HIGH)
                    #m =GPIO.input(pir)
                    print("Exiting loop")
                    m =GPIO.input(pir)

                    f=open("abc.txt", "r")
                    content= f.read()
                    f.close()

                

                except KeyboardInterrupt :
                    break
        else:
            try:
                continue
            except KeyboardInterrupt :
                GPIO.cleanup()
                break
                
    print("Closing .....")
    a.close()        

                

        
