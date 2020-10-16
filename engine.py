import os

path = os.path.abspath(os.path.dirname(__file__))
os.environ['PATH'] = path + ';' + os.environ['PATH']

from classes import *
from Display.graphics import *
from Display.events import *
from Collisions.hitboxes import *
from winsound import PlaySound, Beep

pressed = [0 for _ in range(256)]


def get_events():
    global pressed

    array = []

    for event in events():
        event = Event(event)
        if event.key < 256 and event.type == KEYDOWN:
            pressed[event.key] = 1
        elif event.key < 256 and event.type == KEYUP:
            pressed[event.key] = 0
        
        array.append(event)
    
    return array

def get_pressed():
    global pressed
    return pressed