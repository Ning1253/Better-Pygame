import time, inspect

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
            self.collider -= (other[0], other[1])

        return self

    def rotate(self, angle):
        self.angle += angle

        if self.collider:
            self.collider.rotate(angle)
        
        if self.image:
            self.image.rotate(angle)

    def draw(self, surface):
        surface.blit(self.image, dest=(self.x, self.y), angle = 0)
    
    def update(self):
        ...

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

class Group():
    def __init__(self):
        self.sprites = []
    
    def add(self, *sprites):
        for sprite in sprites:
            if type(sprite) != Sprite and not issubclass(type(sprite), Sprite):
                raise TypeError("Can only add sprite to sprite group object. ")
            else:
                self.sprites.append(sprite)
    
    def update(self):
        for sprite in self.sprites:
            sprite.update()
        
    def draw(self, surface):
        for sprite in self.sprites:
            sprite.draw(surface)

class Event():
    def __init__(self, event):
        self.type = event.type
        self.key = event.key.keysym.sym
        self.event = event

        self.x = event.motion.x
        self.y = event.motion.y

        self.x = event.button.x
        self.y = event.button.y
        self.button = event.button.button
        self.clicks = event.button.clicks
