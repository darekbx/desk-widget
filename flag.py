import RPi.GPIO as GPIO
import time

class Flag():
	
	servoPin = 32
	cycle0Degrees = 2.5
	cycle90Degrees = 7.5
	cycle180Degrees = 12.5

	openFlagAngle = 90
	closedFlagAngle = 0
	shouldOpenFlag = False
	pwm = None

	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.servoPin, GPIO.OUT)
		self.pwm = GPIO.PWM(self.servoPin, 50)
		self.pwm.start(7.5)

	def showFlag(self):
		if self.shouldOpenFlag:
			self.runServo(self.cycle90Degrees)

	def hideFlag(self):
		if self.shouldOpenFlag:
			self.shouldOpenFlag = False
			self.runServo(self.cycle0Degrees)

	def forceHideFlag(self):
		self.runServo(self.cycle0Degrees)

	def updateFlag(self, value):
		self.shouldOpenFlag = value

	def runServo(self, cycle):
		self.pwm.start(7.5)
		self.pwm.ChangeDutyCycle(cycle)
		time.sleep(1)
		self.pwm.start(0)
		if cycle == self.cycle90Degrees:
			print "Show flag"
		else:
			print "Hide flag"
