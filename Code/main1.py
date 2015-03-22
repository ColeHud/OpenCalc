'''
By Cole Hudson
Date: 3/18/2015

This program is used to handle key input from the raspberry pi's GPIO. When a pin is connected
to ground, it emits a keystroke.

The keys that can be emitted are set up with the device, and the key mapping is set up
with the dictionary mapping.
'''


#import uinput for emitting keystrokes
import uinput
#import time in order to save cpu
import time
#import RPi.GPIO to get info from the GPIO pins
import RPi.GPIO as GPIO

#set up the device for emitting keystrokes
device = uinput.Device([
        uinput.KEY_1,
        uinput.KEY_2,
        uinput.KEY_3,
        uinput.KEY_4,
        uinput.KEY_5,
        uinput.KEY_6,
        uinput.KEY_7,
        uinput.KEY_8,
        uinput.KEY_9,
        uinput.KEY_BACKSLASH,
        uinput.KEY_SLASH,
        uinput.KEY_DOT,
        uinput.KEY_ENTER,
        uinput.KEY_LEFTSHIFT,
        uinput.KEY_LEFTBRACE,
        uinput.KEY_RIGHTBRACE,
        uinput.KEY_NUMERIC_STAR,
        ])

#GPIO Mapping
mapping = {
	7: uinput.KEY_LEFTSHIFT,
	8: uinput.KEY_0,
	10: uinput.KEY_ENTER,
	#11 uinput.KEY_,
	12: uinput.KEY_LEFTBRACE,
	13: uinput.KEY_1,
	15: uinput.KEY_2,
	16: uinput.KEY_3,
	#18: uinput.KEY_1,
	19: uinput.KEY_RIGHTBRACE,
	21: uinput.KEY_4,
	22: uinput.KEY_5,
	23: uinput.KEY_6,
	#24: uinput.KEY_1,
	#26: uinput.KEY_1,
	29: uinput.KEY_7,
	31: uinput.KEY_8,
	32: uinput.KEY_9,
	33: uinput.KEY_BACKSLASH,
	#35: uinput.KEY_1,
	#36: uinput.KEY_1,
	#37: uinput.KEY_1,
	#38: uinput.KEY_1,
	#40: uinput.KEY_1,
}


#set up the gpio
GPIO.setmode(GPIO.BOARD)

#loop over the gpio mapping
for pin in mapping:
	#setup each pin
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#program loop
while 1:
	#for each pin in the mapping dictionary
	for pin in mapping:
		#check if it's ground
		if(GPIO.input(pin) == 0):
			#if it is then emit a click tied to that pin
			device.emit_click(mapping[pin])
			#do nothing until the button is released
			while GPIO.input(pin) == 0:
				time.sleep(.1)


#cleanup the GPIO
GPIO.cleanup()