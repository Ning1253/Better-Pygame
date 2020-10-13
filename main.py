import Display.graphics as graphics
import Collisions.hitboxes as collisions
import time

class Sprite():
    def __init__(self, x = 0, y = 0, angle = 0):
        self.image = None
        self.collider = None

        self.x = x
        self.y = y
    
        self.angle = angle

        if self.collider:
            self.collider.rotate(angle)
        if self.image:
            self.image.rotate(angle)

    def __add__(self, other: tuple):
        self.x += other[0]
        self.y += other[1]
        
        if self.collider:
            self.collider += (other[0], other[1])

        return self
    
    def __sub__(self, other: tuple):
        self.x -= other[0]
        self.y -= other[1]

        if self.collider:
            self.collider += (other[0], other[1])

        return self

    def rotate(self, angle):
        self.angle += angle

        if self.collider:
            self.collider.rotate(angle)
        
        if self.image:
            self.image.rotate(angle)

    def draw(self, surface, dest = None):
        surface.blit(self.image, dest=(self.x, self.y), angle = self.angle)

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
