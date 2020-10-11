import time

class Clock():
    def __init__(self):
        self.start = time.time()
        self.ctime = time.ctime(time.time())

        self.current = self.start

    def tick(self, freq):
        timed = time.time()
        if (timed - self.start) < 1 / freq:
            time.sleep((1 / freq - timed + self.start))

        self.start = time.time()
