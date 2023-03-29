#!/usr/bin/env pybricks-micropython
"""
Run 1
test
"""
import logging

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
# from pybot.PID import PID
# from pybot.timed_loop import timed_loop
import pybot

import config

log = logging.getLogger('FLL')
log.setLevel(logging.DEBUG)

# Create a PyBot Environment
env = pybot.Environment()

# Brick
env.ev3 = EV3Brick()

# Initialize the motors.
env.left_motor = Motor(getattr(Port, config.LEFT_MOTOR_PORT))
env.right_motor = Motor(getattr(Port, config.RIGHT_MOTOR_PORT))

# Initialize the color sensor.
env.center_line_sensor = ColorSensor(getattr(Port, config.CENTER_COLOR_SENSOR_PORT))
env.left_line_sensor = ColorSensor(getattr(Port, config.LEFT_COLOR_SENSOR_PORT))
env.right_line_sensor = ColorSensor(getattr(Port, config.RIGHT_COLOR_SENSOR_PORT))

# Initialize the Gyro Sensor.
# env.gyro = GyroSensor(getattr(Port, config.GYRO_SENSOR_PORT))

# Initialize the drive base.
env.wheels = DriveBase(
    env.left_motor, env.right_motor,
    wheel_diameter=config.WHEEL_DIAMETER,
    axle_track=config.AXLE_TRACK)

def ramp(target, start=0, ramp_time=1000):
    timer = StopWatch()
    while True:
        current_time = timer.time()
        if current_time > ramp_time:
            yield target
        else:
            yield (start + target) * (1 - (ramp_time - current_time) / ramp_time)

def move_forward(env, distance):
    rampup = ramp(-400, ramp_time=750)
    rampdown = ramp(0, start=-400, ramp_time=750)
    timer = StopWatch()
    ramping_up = True
    while True:
        if ramping_up:
            speed = next(rampup)
            if speed == -400:
                ramping_up = False
        else:
            speed = next(rampdown)
            if speed == 0:
                log.info('break')
                break
        log.info('Speed: %s' % speed)
        env.wheels.drive(speed, 0)
        yield


env.queue.append(move_forward(env, 10))
env.run()

# rampup = ramp(-400, ramp_time=750)
# rampdown = ramp(0, start=-400, ramp_time=750)
# state = 'RAMPUP'
# for frame in timed_loop(config.LOOP_FREQUENCY):
#     if state == 'RAMPUP':
#         speed = next(rampup)
#         if speed == -400:
#             state = 'RAMPDOWN'
#     elif state == 'RAMPDOWN':
#         speed = next(rampdown)
#         if speed == 0:
#             break
#     log.info('Speed: %s' % speed)
#     robot.drive(speed, 0)
#     # log.info('Frame: %s' % frame)
#     # log.info('Time: %s' % current_time)
#     # log.info('Center Line Sensor Reflection: %s' % (center_line_sensor.reflection()))
#     # log.info('Left Line Sensor Reflection:   %s' % (left_line_sensor.reflection()))
#     # log.info('Right Line Sensor Reflection:  %s' % (right_line_sensor.reflection()))
#     # log.info('Gyro:  %s' % (gyro.angle()))


# # Calculate the light threshold. Choose values based on your measurements.
# BLACK = 5
# WHITE = 67
# threshold = (BLACK + WHITE) / 2
# 
# # Set the drive speed at 100 millimeters per second.
# DRIVE_SPEED = 150
# 
# # Set the gain of the proportional line controller. This means that for every
# # percentage point of light deviating from the threshold, we set the turn
# # rate of the drivebase to 1.2 degrees per second.
# 
# # For example, if the light value deviates from the threshold by 10, the robot
# # steers at 10*1.2 = 12 degrees per second.
# 
# # Get on Left line
# TARGET_LOOP_PERIOD = 10  # ms
# pid = PID(12.0, 0.0, 0.00, setpoint=0)
# def follow_line_until(callback):
# 
#     single_loop_timer = StopWatch()
#     control_loop_timer = StopWatch()
#     control_loop_count = 0
#     # Start following the line endlessly.
#     while True:
#         single_loop_timer.reset()
#         if control_loop_count == 0:
#             average_control_loop_period = TARGET_LOOP_PERIOD / 1000.
#             control_loop_timer.reset()
#         else:
#             average_control_loop_period = (control_loop_timer.time() / 1000 / control_loop_count)
#         control_loop_count += 1
# 
#         # Calculate the turn rate.
#         error = line_sensor.reflection() - threshold
#         control = pid(error)
#         turn_rate = control
#         if abs(control) > 350:
#             speed = 0
#         else:
#             speed = 0
#     
#         # Set the drive base speed and turn rate.
#         log.info('Turn Rate: %s Speed: %s Control: %s Error: %s' % (turn_rate, speed, control, error))
# 
#         robot.drive(speed, turn_rate)
#     
#         # First Change lines
#         if callback():
#             return
#     
#         # You can wait for a short time or do other things in this loop.
#         wait(TARGET_LOOP_PERIOD - single_loop_timer.time())
# # Effective range of speed 0-400
# # Effective range of turn 0-400
# # Error ranges from -30 - 30
# 
# 
# # Reset the distance calculator
# robot.reset()
# follow_line_until(lambda _ = None: robot.distance() > 100)
# # wait(100)
# # Calibration of light reflection sensor
# # while True:
# #     log.info(line_sensor.reflection())
