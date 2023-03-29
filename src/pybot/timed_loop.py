import logging
from pybricks.tools import wait, StopWatch

log = logging.getLogger(__name__)

def timed_loop(frequency=10):
    frame = 0
    interval = 1000 / frequency
    timer = StopWatch()
    while True:
        remaining_time = frame * interval - timer.time()
        if frame and remaining_time < 0:
            log.warning('current frame saturated by %sms', -remaining_time)
        else:
            wait(remaining_time)
        frame += 1
        yield frame
