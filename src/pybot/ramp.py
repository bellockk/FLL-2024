"""
Ramp capability.
"""
from pybricks.tools import StopWatch


def ramp(target, start=0, ramp_time=1000):
    """
    Ramp output.

    Args:
      target: Ending value of ramp.
      start: Starting value of ramp.
      ramp_time: Time to ramp in milliseconds.
    """
    timer = StopWatch()
    while True:
        current_time = timer.time()  # pylint: disable=E1111
        if current_time > ramp_time:
            yield target
        else:
            yield (start + target) * (1 - (
                ramp_time - current_time) / ramp_time)
