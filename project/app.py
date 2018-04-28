"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template,request, redirect, url_for
import time

app= Flask(__name__)

wsgi_app = app.wsgi_app

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
            # turn on LED on arduino
            #stop automation
            
           
        # if we press the turn off button
        elif request.form['submit'] == 'Turn Off': 
            print ('TURN OFF')
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
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
