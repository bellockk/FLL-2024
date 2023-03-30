#!/usr/bin/env pybricks-micropython
"""
Run 1
test
"""
import sys
import logging
from pybot import Robot

log = logging.getLogger('MAIN')
log.setLevel(logging.DEBUG)
log.info('OMMS FLL 2024 Season')
log.info('Python Version: %s', sys.version)

# Create a PyBot Environment
robot = Robot()

robot.ev3.speaker.beep()
