from math import sin, cos, atan, sqrt, pi
import os
from PIL import Image
from Collisions.collisions import r_coll, c_coll, p_coll, rc_coll, pr_coll, pc_coll

def dcos(num):
    return cos(num / 360 * 2 * pi)

def dsin(num):
    return sin(num / 360 * 2 * pi)

def datan(num):
    return atan(num) * 360 / (2 * pi)

class Collider():
    pass


# Below are all hitbox types
class Rect(Collider):
    def __init__(self, x, y, width, height, angle = 0):
        self.update(x, y, width, height, angle)

    def update(self, x, y, width, height, angle):
        self.coords = (x, y)
        self.width = width
        self.height = height
        self.angle = angle % 360

        
        self.corners = [0, 0, 0, 0]

        self.corners[0] = (x, y)
        self.corners[1] = (round(x + width * dcos(angle), 10), round(y + width * dsin(angle), 10))
        self.corners[2] = (round(x + height * dcos(270 + angle), 10), round(y + height * dsin(270 + angle), 10))
        
        w = self.width
        h = self.height
        a = self.angle
        corner1 = x + sqrt(w ** 2 + h ** 2) * dcos(a - datan(h/w))
        corner2 = y - sqrt(w ** 2 + h ** 2) * dsin(a - datan(h/w))
        self.corners[3] = (round(corner1, 10), round(corner2, 10))

    def rotate(self, angle):
        self.update(self.coords[0], self.coords[1], self.width, self.height, angle + self.angle)

    def __add__(self, other: tuple):
        self.update(self.coords[0] + other[0], self.coords[1] + other[1], self.width, self.height, self.angle)
        return self
    
    def __sub__(self, other: tuple):
        self.update(self.coords[0] - other[0], self.coords[1] - other[1], self.width, self.height, self.angle)
        return self

    def shiftx(self, num):
        self.update(self.coords[0] + num, self.coords[1], self.width, self.height, self.angle)
    
    def shifty(self, num):
        self.update(self.coords[0], self.coords[1] + num, self.width, self.height, self.angle)
    
    def move(self, coords: tuple):
        """
            Shift the topleft corner of the rect to the chosen coordinates
            (x, y)
        """

        self.update(coords[0], coords[1], self.width, self.height, self.angle)

    def swidth(self, num):
        if num != 0:
            self.update(self.coords[0], self.coords[1], num, self.height, self.angle)
    
    def sheight(self, num):
        if num != 0:
            self.update(self.coords[0], self.coords[1], self.width, num, self.angle)

    def dimensions(self, width, height):
        """
            Set width and height of shape to args
        """

        self.update(self.coords[0], self.coords[1], width, height, self.angle)


class Circle(Collider):
    def __init__(self, x, y, radius):
        self.update(x, y, radius)

    def update(self, x, y, radius):
        self.coords = (x, y)
        self.rad = radius

    def __add__(self, other: tuple):
        self.update(self.coords[0] + other[0], self.coords[1] + other[1], self.rad)
        return self
    
    def __sub__(self, other: tuple):
        self.update(self.coords[0] - other[0], self.coords[1] - other[1], self.rad)
        return self
    
    def move(self, x, y):
        self.update(x, y, self.radius)
    
    def shiftx(self, num):
        self.update(self.coords[0] + num, self.coords[1], self.radius)
    
    def shifty(self, num):
        self.update(self.coords[0], self.coords[1] + num, self.radius)
    
    def radius(self, num):
        self.update(self.coords[0], self.coords[1], num)


class PixelArray(Collider):
    def __init__(self, file, coords = (0, 0)):
        """
            Finds all non black pixels within a bitmap file
            and turns them into a pixel array
        """
        self.file = Image.open(file)
        self.width, self.height = self.file.size
        self.image = self.file.load()
        self.offset = [coords[0], coords[1]]
        self.pixels = [(i + coords[0], j + coords[1]) for i in range(self.width) for j in range(self.height) if self.image[i, j] != (0, 0, 0)]

    def move(self, coords: tuple):
        self.pixels = [(i - self.offset[0] + coords[0], j - self.offset[1] + coords[1]) for i, j in self.pixels]
        self.offset = [coords[0], coords[1]]
    
    def __add__(self, other: tuple):
        self.pixels = [(i + other[0], j + other[1]) for i, j in self.pixels]
        self.offset[0] += other[0]
        self.offset[1] += other[1]
        return self

    def __sub__(self, other: tuple):
        self.pixels = [(i - other[0], j - other[1]) for i, j in self.pixels]
        self.offset[0] -= other[0]
        self.offset[1] -= other[1]
        return self

def collision(obj1: Collider, obj2: Collider):
    """
        Colliders can be either Rect(), Circle() or PixelArray() 
        instances
    """

    if type(obj1) == Rect and type(obj2) == Rect:
        return r_coll(obj1.corners, obj2.corners)
    
    if type(obj1) == Rect and type(obj2) == Circle:
        return rc_coll(obj1.corners, [obj2.coords[0], obj2.coords[1], obj2.rad])
    
    if type(obj1) == Rect and type(obj2) == PixelArray:
        if not obj2.pixels: return False
        return pr_coll(obj2.pixels, obj1.corners)
    
    if type(obj1) == Circle and type(obj2) == Rect:
        return rc_coll(obj2.corners, [obj1.coords[0], obj1.coords[1], obj1.rad])
    
    if type(obj1) == Circle and type(obj2) == Circle:
        return c_coll([obj1.coords[0], obj1.coords[1], obj1.rad], [obj2.coords[0], obj2.coords[1], obj2.rad])
    
    if type(obj1) == Circle and type(obj2) == PixelArray:
        if not obj2.pixels: return False
        return pc_coll(obj2.pixels, [obj1.coords[0], obj1.coords[1], obj1.rad])
    
    if type(obj1) == PixelArray and type(obj2) == Rect:
        if not obj1.pixels: return False
        return pr_coll(obj1, obj2.corners)
    
    if type(obj1) == PixelArray and type(obj2) == Circle:
        if not obj1.pixels: return False
        return pc_coll(obj1, [obj2.coords[0], obj2.coords[1], obj2.rad])
    
    if type(obj1) == PixelArray and type(obj2) == PixelArray:
        if not (obj1.pixels or obj2.pixels): return False
        return p_coll(obj1, obj2)
    
    else:
        raise TypeError("Attempted collision detecting between non-Collider objects")
