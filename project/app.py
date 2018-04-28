"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template,request, redirect, url_for
import time
import RPi.GPIO as GPIO

app= Flask(__name__)
#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#wsgi_app = app.wsgi_app

led_pin=26
fan = 6
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(fan, GPIO.OUT)
GPIO.output(led_pin,GPIO.LOW)
GPIO.output(fan,GPIO.LOW)


#apis
@app.route('/', methods = ['POST','GET'])
def index():
    # variables for template page (templates/index.html)
    author = "Shubham"
    # if we make a post request on the webpage aka press button then do stuff
    if request.method == 'POST':
        # if we press the turn on button
        if request.form['submit'] == 'Turn On': 
            print ("TURN ON")
            GPIO.output(led_pin,GPIO.HIGH)

            # turn on LED on arduino
            #stop automation
            
           
        # if we press the turn off button
        elif request.form['submit'] == 'Turn Off': 
            print ('TURN OFF')
            GPIO.output(led_pin,GPIO.LOW)
        elif request.form['submit'] =="TurnOnF":
            print("Fan Turned On")
            GPIO.output(fan,GPIO.HIGH)
            time.sleep(2)
        elif request.output.form['submit'] =='TurnOffF':
            print("FanTurnedOff")
            GPIO.output(fan,GPIO.LOW)
            time.sleep(4)
        elif request.form['submit'] == 'manual':
            f= open("abc.txt", "w+")
            f.write("manual\n")
            f.close()
        elif request.form['submit'] == 'auto':
            f= open("abc.txt", "w")
            f.write("auto\n")
            f.close()

            
           

        else:
            pass    
    # read in analog value from photoresistor
    
    # the default page to display will be our template with our template variables
    return render_template('index.html', author=author, value=0)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5040, debug=True)
