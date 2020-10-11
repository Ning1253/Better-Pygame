from ctypes import *

double = c_double
cint = c_int
cbool = c_bool

file = CDLL("C:/Users/aslas/Desktop/EPQ/Files/collisions.dll")

def wrap_function(file, func, argtypes = None, restype = None):
    func = file.__getattr__(func)
    if argtypes: func.argtypes = argtypes
    if restype: func.restype = restype
    return func


rect_collision = wrap_function(file, "rect_collision", argtypes = (((double*2)*4), ((double*2)*4)), restype = cbool)
circle_collision = wrap_function(file, "circle_collision", argtypes = ((double*3), (double*3)), restype = cbool)
rect_circle_collision = wrap_function(file, "rect_circle_collision", argtypes = (((double*2)*4), (double*3)), restype = cbool)
pixel_collision = wrap_function(file, "pixel_collision", argtypes = (POINTER(double*2), cint, POINTER(double*2), cint), restype = cbool)
pixel_circle_collision = wrap_function(file, "pixel_circle_collision", argtypes = (POINTER(double*2), cint, (double*3)), restype = cbool)
pixel_rect_collision = wrap_function(file, "pixel_rect_collision", argtypes = (POINTER(double*2), cint, ((double*2)*4)), restype = cbool)

def r_coll(rect1, rect2):
    rect1 = ( (double*2) * 4) (*rect1)
    rect2 = ( (double*2) * 4) (*rect2)
    return rect_collision(rect1, rect2)

def c_coll(circ1, circ2):
    circ1 = (double*3) (*circ1)
    circ2 = (double*3) (*circ2)
    return circle_collision(circ1, circ2)

def rc_coll(rect, circ):
    rect = ( (double*2) * 4) (*rect)
    circ = (double*3) (*circ)
    return rect_circle_collision(rect, circ)

def p_coll(pixs1, pixs2):
    pixs1 = ( (double*2) * len(pixs1)) (*pixs1)
    pixs2 = ( (double*2) * len(pixs2)) (*pixs2)
    return pixel_collision(pixs1, len(pixs1), pixs2, len(pixs2))

def pc_coll(pixs, circ):
    pixs = ( (double*2) * len(pixs)) (*pixs)
    circ = (double*3) (*circ)
    return pixel_circle_collision(pixs, len(pixs), circ)

def pr_coll(pixs, rect):
    pixs = ( (double*2) * len(pixs)) (*pixs)
    rect = ( (double*2) * 4) (*rect)
    return pixel_rect_collision(pixs, len(pixs), rect)