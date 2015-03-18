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
	1: uinput.KEY_1,
	2: uinput.KEY_2,
	3: uinput.KEY_3,
	4: uinput.KEY_4,
	5: uinput.KEY_5,
	6: uinput.KEY_7,
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