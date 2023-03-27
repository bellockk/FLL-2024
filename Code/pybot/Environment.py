class Environment():
    def __init__(self):
        self.queue = []
    
    def run(self, frequency=10):
        for frame in timed_loop(config.LOOP_FREQUENCY):
            if self.queue:
                try:
                    next(self.queue[0])
                except StopIteration:
                    del self.queue[0]
            else:
                break