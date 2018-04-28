"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template,request, redirect, url_for
import time
import RPi.GPIO as GPIO


app= Flask(__name__)

wsgi_app = app.wsgi_app



#apis
@app.route('/', methods = ['POST','GET'])
def index():
	GPIO.setmode(GPIO.BCM) 
	led_pin = 26
	fan = 6
	GPIO.cleanup()
	GPIO.setup(led_pin, GPIO.OUT)
	GPIO.setup(fan, GPIO.OUT)
	time.sleep(0.0001)
	GPIO.output(led_pin,0)
	GPIO.output(fan,0)
	author ="Shubham"
	if request.method == 'POST':
		if request.form['submit'] == 'Turn On': 
			print ("TURN ON")
			GPIO.output(led_pin,1)
            # turn on LED on arduino
            #stop automation
            
           
        # if we press the turn off button
        elif request.form['submit'] == 'Turn Off': 
            print ('TURN OFF')
            GPIO.output(led_pin,0)
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
        return render_template('index.html', author=author, value=0)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
