"""
Robot class.

This class simplifies the process of initializing all the motors and sensors
for the OMMS FLL 2024 team robot.
"""
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from . import config
from .timed_loop import timed_loop


class Robot:
    """Robot controller."""

    def __init__(self):
        # Initialize Brick
        self.ev3 = EV3Brick()

        # Initialize Motors
        self.motors = {
            'left': Motor(getattr(Port, config.LEFT_MOTOR_PORT)),
            'right': Motor(getattr(Port, config.RIGHT_MOTOR_PORT)),
            'front': Motor(getattr(Port, config.FRONT_MOTOR_PORT)),
            'back': Motor(getattr(Port, config.BACK_MOTOR_PORT))}

        # Initialize Sensors
        self.sensors = {
            'center_color': ColorSensor(
                getattr(Port, config.CENTER_COLOR_SENSOR_PORT)),
            'left_color': ColorSensor(
                getattr(Port, config.LEFT_COLOR_SENSOR_PORT)),
            'right_color': ColorSensor(
                getattr(Port, config.RIGHT_COLOR_SENSOR_PORT)),
            'gyro': GyroSensor(getattr(Port, config.GYRO_SENSOR_PORT))}

        # Initialize the drive base.
        self.drivebase = DriveBase(
            self.motors['left'], self.motors['right'],
            wheel_diameter=config.WHEEL_DIAMETER,
            axle_track=config.AXLE_TRACK)

        # Initialize the action queue
        self.queue = []

    def run(self, frequency=config.LOOP_FREQUENCY):
        """
        Run queued events.

        Args:
          frequency: Loop frequency.
        """
        for _ in timed_loop(frequency):
            if self.queue:
                try:
                    next(self.queue[0])
                except StopIteration:
                    del self.queue[0]
            else:
                break

    def wait(self, time):
        """
        Wait for a given number of milliseconds.

        Args:
          time: Time to wait in milliseconds.
        """
        wait(time)
