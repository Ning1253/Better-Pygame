import os

path = os.path.abspath(os.path.dirname(__file__))
os.environ['PATH'] = path + ';' + os.environ['PATH']

from classes import *
from Display.graphics import *
from Display.events import *
from Collisions.hitboxes import *
from winsound import PlaySound, Beep
import Collisions.collisions

pressed = [0 for _ in range(256)]
specials = []


def get_events():
    global pressed
    global specials

    array = []

    for event in events():
        event = Event(event)
        if event.type == KEYDOWN:
            if event.key < 256: pressed[event.key] = 1
            elif event.key not in specials: specials.append(event.key)
        elif event.type == KEYUP:
            if event.key < 256: pressed[event.key] = 0
            else: specials.remove(event.key)
        array.append(event)
    
    return array

def get_pressed():
    global pressed
    return pressed

def is_pressed(key):
    global pressed
    global specials

    if key < 256:
        return pressed[key]
    else:
        return key in specials