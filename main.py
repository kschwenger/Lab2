"""Using a single threaded callback function, write python code such that:
– When switch #1 is pressed, LED #1 produces a single cycle of a 1 Hz triangle waveform
(smooth transition from low à high à low).
– When switch #2 is pressed, LED #2 produces a single cycle of a 1 Hz triangle waveform.
– LED #3 continually blinks on/off at 1 Hz, independent other actions.
– Use exception handling to exit elegantly on ctrl-C by cleaning up the GPIO ports."""

# for LED 3
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
p = 4
GPIO.setup(pout, GPIO.OUT)

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