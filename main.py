"""Using a single threaded callback function, write python code such that:
– When switch #1 is pressed, LED #1 produces a single cycle of a 1 Hz triangle waveform
(smooth transition from low à high à low).
– When switch #2 is pressed, LED #2 produces a single cycle of a 1 Hz triangle waveform.
– LED #3 continually blinks on/off at 1 Hz, independent other actions.
– Use exception handling to exit elegantly on ctrl-C by cleaning up the GPIO ports."""


# for callback 
import RPi.GPIO as gpio
# Define input/output port numbers:
in1, in2 = 20, 21
led1, led2, led3 = 4, 17, 27

gpio.setmode(gpio.BCM)
gpio.setup(in1, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(in2, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(led1, gpio.out)
gpio.setup(led2, gpio.out)
gpio.setup(led3, gpio.out)
# Define a threaded callback function:
def myCallback1(channel):
  gpio.output(led1, 1)
def myCallback2(channel):
  gpio.output(led2, 1)

# Execute myCallback() if port 1 goes HIGH:
gpio.add_event_detect(in1, gpio.RISING, callback=myCallback1, bouncetime=100)
gpio.add_event_detect(in2, gpio.RISING, callback=myCallback2, bouncetime=100)

gpio.cleanup()





"""
# for triangles (LEDs 1 and 2)
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
p = 4
GPIO.setup(p, GPIO.OUT)

pwm = GPIO.PWM(p, 100) # create PWM object @ 1 Hz
try:
  pwm.start(0) # initiate PWM at 0% duty cycle
  while 1:
    for dc in range(101): # loop duty cycle from 0 to 100
      pwm.ChangeDutyCycle(dc) # set duty cycle
      sleep(0.01) # sleep 10 ms
except KeyboardInterrupt: # stop gracefully on ctrl-C
  print('\nExiting')

pwm.stop()
GPIO.cleanup()
"""








# for LED 3
"""
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
p = 4
GPIO.setup(p, GPIO.OUT)

try:
  while True:
    GPIO.output(p, 0)
    sleep(0.5)
    GPIO.output(p, 1)
    sleep(0.5)
except KeyboardInterrupt: # if user hits ctrl-C
  print('\nExiting')
except Exception as e: # catch all other errors
  print('\ne')

GPIO.cleanup() # clean up GPIO ports
"""