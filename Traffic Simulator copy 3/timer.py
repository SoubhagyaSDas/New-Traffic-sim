import time


class Timer:

    def __init__(self, interval):
        self.interval = interval

    def start(self, callback):
        while True:
            callback()
            time.sleep(self.interval)
