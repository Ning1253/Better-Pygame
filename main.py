import os

path = os.path.abspath(os.path.dirname(__file__))
os.environ['PATH'] = path + ';' + os.environ['PATH']

from classes import *
from Display.graphics import *
from Display.events import *
from Collisions.hitboxes import *