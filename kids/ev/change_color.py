#!/usr/bin/env python3
from ev3dev2.led import Leds
leds = Leds()
print("OK")
leds.set_color("LEFT", "GREEN")
