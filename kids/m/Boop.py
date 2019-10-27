#!/usr/bin/env python3
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.button import Button

leds = Leds()
sound = Sound()
button= Button



print("You do it for cheese!")

while True:
  if button.enter:
    leds.set_color("LEFT", "GREEN")
    leds.set_color("RIGHT", "GREEN")
    sound.play_file('/home/robot/pydev/madeleine/SU.wav')
    sleep
  else:
    leds.set_color("LEFT", "RED")
    leds.set_color("RIGHT", "RED")

# A long time ago in a galaxy far,
# far away...
  Sound.play_song((
    ('D4', 'e3'),      # intro anacrouse
    ('D4', 'e3'),
    ('D4', 'e3'),
    ('G4', 'h'),       # meas 1
    ('D5', 'h'),
    ('C5', 'e3'),      # meas 2
    ('B4', 'e3'),
    ('A4', 'e3'),
    ('G5', 'h'),
    ('D5', 'q'),
    ('C5', 'e3'),      # meas 3
    ('B4', 'e3'),
    ('A4', 'e3'),
    ('G5', 'h'),
    ('D5', 'q'),
    ('C5', 'e3'),      # meas 4
    ('B4', 'e3'),
    ('C5', 'e3'),
    ('A4', 'h.'),
    ))
