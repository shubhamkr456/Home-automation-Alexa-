 

#Shubham Dht
import Adafruit_DHT
import time
def temp():
    

        humidity, temperature= Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,21)
        if humidity is not None and temperature is not None:
            humidity= round(humidity,2)
            temperature= round(temperature, 2)
            print('Temp= {0:0.1f}*C Humidity= {1:0.1f}%'.format(temperature, humidity))
            return temperature,humidity  
        else:
            print('Cant connect')
            time.sleep(30)
temp()
# This would be the Ajax Requestz

