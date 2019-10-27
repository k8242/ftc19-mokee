#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sound import Sound
from ev3dev2.led import Leds

leds=Leds()
sound=Sound()
ts=TouchSensor()

while True:
	if ts.is_pressed:
		leds.set_color("LEFT", "GREEN")
		leds.set_color("RIGHT", "GREEN")
		sound.speak('Text to speech Ex Deee!')
	else:
		leds.set_color("LEFT", "RED")
		leds.set_color("RIGHT", "RED")
		sound.speak('Freeshavahcadoo?')
