'''
	Raspberry Pi GPIO Status and Control
'''
import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define sensors GPIOs


#define actuators GPIOs
ledRed = 13
ledYlw = 19


#initialize GPIO status variables

ledRedSts = 0
ledYlwSts = 0


# Define led pins as output
GPIO.setup(ledRed, GPIO.OUT)   
GPIO.setup(ledYlw, GPIO.OUT) 

# turn leds OFF 
GPIO.output(ledRed, GPIO.LOW)
GPIO.output(ledYlw, GPIO.LOW)

	
@app.route("/")
def index():
	# Read GPIO Status
	ledRedSts = GPIO.input(ledRed)
	ledYlwSts = GPIO.input(ledYlw)
	

	templateData = {
      'ledRed'  : ledRedSts,
      'ledYlw'  : ledYlwSts,
      }
	return render_template('index.html', **templateData)
	
# The function below is executed when someone requests a URL with the actuator name and action in it:
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	if deviceName == 'ledRed':
		actuator = ledRed
	if deviceName == 'ledYlw':
		actuator = ledYlw
		
	if action == "on":
		GPIO.output(actuator, GPIO.HIGH)
	if action == "off":
		GPIO.output(actuator, GPIO.LOW)
		     
	ledRedSts = GPIO.input(ledRed)
	ledYlwSts = GPIO.input(ledYlw)

	templateData = {
                'ledRed'  : ledRedSts,
                'ledYlw'  : ledYlwSts,
                }
	return render_template('index.html', **templateData)

@app.route("/manual")
def manual():
        f= open("abc.txt", "w+")
        f.write("manual\n")
        f.close()
        #template data
        templateData = {
                'ledRed'  : ledRedSts,
                'ledYlw'  : ledYlwSts,
                }
        return render_template('index.html', **templateData)


@app.route("/automatic")
def automatic():
        f= open("abc.txt", "w+")
        f.write("auto\n")
        f.close()
        #template data
        templateData = {
                'ledRed'  : ledRedSts,
                'ledYlw'  : ledYlwSts,
                }
        return render_template('index.html', **templateData)




if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
