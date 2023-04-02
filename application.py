from flask import Flask, render_template, jsonify, request
import RPi.GPIO as GPIO


#commands to run server

#cd flaskServer
#source virt/bin/activate
#export FLASK_ENV=development
#export FLASK_APP=application.py
#flask run -h 10.171.226.213


app = Flask(__name__)
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
#define actuators GPIOs
Clockwise = 13
CountClock = 26
ElbowFor = 16
ElbowBack = 12
WristFor = 25
WristBack = 24
BaseUp = 23
BaseDown = 22
ClawOpen = 27
ClawClose = 17

#initialize GPIO status variables
ClockwiseState = 0
CountClockState = 0
# Define pins as output
GPIO.setup(Clockwise, GPIO.OUT)   
GPIO.setup(CountClock, GPIO.OUT) 
GPIO.setup(ElbowFor, GPIO.OUT)   
GPIO.setup(ElbowBack, GPIO.OUT) 
GPIO.setup(WristFor, GPIO.OUT)   
GPIO.setup(WristBack, GPIO.OUT) 
GPIO.setup(BaseUp, GPIO.OUT)   
GPIO.setup(BaseDown, GPIO.OUT) 
GPIO.setup(ClawOpen, GPIO.OUT)   
GPIO.setup(ClawClose, GPIO.OUT) 
# turn motors OFF 
GPIO.output(Clockwise, GPIO.LOW)
GPIO.output(CountClock, GPIO.LOW)
GPIO.output(ElbowFor, GPIO.LOW)
GPIO.output(ElbowBack, GPIO.LOW)
GPIO.output(WristFor, GPIO.LOW)   
GPIO.output(WristBack, GPIO.LOW) 
GPIO.output(BaseUp, GPIO.LOW)   
GPIO.output(BaseDown, GPIO.LOW) 
GPIO.output(ClawOpen, GPIO.LOW)   
GPIO.output(ClawClose, GPIO.LOW) 
#create a route decorator    www.whateva/index.html <- the index is the decorator route
@app.route('/')
def index():
    
	# Read Sensors Status
	ClockwiseState = GPIO.input(Clockwise)
	CountClockState = GPIO.input(CountClock)
#	ledGrnSts = GPIO.input(ledGrn)
	templateData = {
              'title' : 'GPIO output Status!',
              'Clockwise'  : ClockwiseState,
              'CountClock'  : CountClockState,
       #       'ledGrn'  : ledGrnSts,
        }
	return render_template('index.html', **templateData)

@app.route('/send/<button>')
def sendCommand(button):
	if button == "ShoulderForward":
		GPIO.output(Clockwise, GPIO.HIGH)	#counter clockwise
		print("down")
	if button == "ShoulderBackward":
		GPIO.output(CountClock, GPIO.HIGH)	#clockwise
		print("down")
	if button == "ElbowForward":
		GPIO.output(ElbowFor, GPIO.HIGH)
		print("down")
	if button == "ElbowBackward":
		GPIO.output(ElbowBack, GPIO.HIGH)
		print("down")
	if button == "WristForward":
		GPIO.output(WristFor, GPIO.HIGH)
		print("down")
	if button == "WristBackward":
		GPIO.output(WristBack, GPIO.HIGH)
		print("down")
	if button == "BaseUpward": 
		GPIO.output(BaseUp, GPIO.HIGH)   #clockwise
		print("down")
	if button == "BaseDownward":
		GPIO.output(BaseDown, GPIO.HIGH)  #counter clockwise
		print("down")
	if button == "ClawOutward":
		GPIO.output(ClawOpen, GPIO.HIGH)
		print("down")
	if button == "ClawInward":
		GPIO.output(ClawClose, GPIO.HIGH)
		print("down")
	templateData = {'button':button}
	return "{} - OK".format(button)
    
@app.route('/stop/<button>')
def stopCommand(button):
	if button == "ShoulderForward":
		GPIO.output(Clockwise, GPIO.LOW)
		print("up")
	if button == "ShoulderBackward":
		GPIO.output(CountClock, GPIO.LOW)
		print("up")
	if button == "ElbowForward":
		GPIO.output(ElbowFor, GPIO.LOW)
		print("up")
	if button == "ElbowBackward":
		GPIO.output(ElbowBack, GPIO.LOW)
		print("up")
	if button == "WristForward":
		GPIO.output(WristFor, GPIO.LOW)
		print("up")
	if button == "WristBackward":
		GPIO.output(WristBack, GPIO.LOW)
		print("up")
	if button == "BaseUpward":
		GPIO.output(BaseUp, GPIO.LOW)
		print("up")
	if button == "BaseDownward":
		GPIO.output(BaseDown, GPIO.LOW)
		print("up")
	if button == "ClawOutward":
		GPIO.output(ClawOpen, GPIO.LOW)
		print("up")
	if button == "ClawInward":
		GPIO.output(ClawClose, GPIO.LOW)
		print("up")


	templateData = {'button':button}
	return "{} - OK".format(button)
    
if __name__ == "__main__":
	app.run(debug=True, port=5000, host='0.0.0.0')