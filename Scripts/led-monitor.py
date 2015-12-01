#! /usr/bin/env python
#
# Monitor a file and toggle onboard LED when it is changed.
#
# Usage:
#   sudo python led-monitor.py [file]

import argparse
import RPi.GPIO as GPIO
import subprocess
import pyinotify
from time import sleep


# Folder to watch.
watch_file = "/path/to/default/folder"

# LED pin mapping.
red = 22
green = 23
blue = 24

# GPIO Setup.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

class LogMonitorRGB(object):
    def __init__(self, mask=pyinotify.ALL_EVENTS):
        self.mask = mask

    def run(self):
        """Configure inotify to toggle LEDs on file changes."""
        self.initialize()
        watch_manager = pyinotify.WatchManager()
        watch_manager.add_watch(watch_file, self.mask, rec=True, auto_add=True)
        notifier = pyinotify.Notifier(watch_manager, default_proc_fun=self.toggle_leds)
        notifier.loop()

    def toggle_leds(self, event):
        GPIO.output(green, 0)
        GPIO.output(red, 1)
        sleep(0.1)
        GPIO.output(red, 0)
        GPIO.output(green, 1)

    def initialize(self):
        """Reset LED to Green. """
        GPIO.output(red, 0)
        GPIO.output(green, 1)
        GPIO.output(blue, 0)

def main():
    LogMonitorRGB().run()

if __name__ == '__main__':
    main()
