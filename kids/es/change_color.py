xx#!/usr/bin/env python3 from ev3dev2.led import Leds

leds = Leds() 

print("I'm running!")

leds.set_color("LEFT", "AMBER")
