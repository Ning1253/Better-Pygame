import sys
import os, time
from math import sin, cos, atan, pi, sqrt
from Collisions.hitboxes import Rect, Circle, PixelArray

# Stop the sdl2 lib from printing warning

old_stdout = sys.stdout # backup current stdout
sys.stdout = open(os.devnull, "w")

import sdl2, sdl2.ext, sdl2.sdlgfx as gfx


sys.stdout = old_stdout # reset old stdout

sdl2.ext.init()



class DisplayError(Exception):
    pass

# Decision: only one display allowed at once

_displays = 0

class Display():
    def __init__(self, width, height, title = "Better Pygame", x=sdl2.SDL_WINDOWPOS_CENTERED, y=sdl2.SDL_WINDOWPOS_CENTERED):
        """
            Initialise a display with a title, width and height. 
        """
        title = title.encode()

        global _displays
        
        if not _displays:
            self.window = sdl2.SDL_CreateWindow(title, x, y, width, height, 0)
            self.renderer = sdl2.SDL_CreateRenderer(self.window, -1, 0)

            _displays += 1

        else:
            raise DisplayError("A display is already initialised. ")

    
    def update(self):
        sdl2.SDL_RenderPresent(self.renderer)

    
    def fill(self, colour):
        colour = (colour[0] % 256, colour[1] % 256, colour[2] % 256)
        sdl2.SDL_SetRenderDrawColor(self.renderer, colour[0], colour[1], colour[2], 255)
        sdl2.SDL_RenderClear(self.renderer)
    
    def blit(self, surface, src = None, dest = None, angle = 0):
        if src:
            srcrect = sdl2.SDL_Rect(src[0][0], src[0][1], src[1][0] - src[0][0], src[1][1] - src[0][1])

        else:
            srcrect = None
        if dest:
            if len(dest) == 2:
                if src:
                    dstrect = sdl2.SDL_Rect(round(dest[0] - srcrect.w / 2), round(dest[1] - srcrect.w / 2), srcrect.w, srcrect.h)
                else:
                    dstrect = sdl2.SDL_Rect(round(dest[0] - surface.w / 2), round(dest[1] - surface.h / 2), surface.w, surface.h)

            elif len(dest) == 4:
                dstrect = sdl2.SDL_Rect()
                dstrect.w = round(dest[1][0] - dest[0][0])
                dstrect.h = round(dest[1][1] - dest[0][1])
                dstrect.x = round(dest[0][0] - dstrect.w / 2)
                dstrect.y = round(dest[0][1] - dstrect.h / 2)
                
            
            else:
                raise IndexError("\'dest\' should have 2 or 4 values. ")
        else:
            if src:
                dstrect = sdl2.SDL_Rect(- srcrect.w / 2, - srcrect.h / 2, srcrect.w, srcrect.h)
            else:
                dstrect = sdl2.SDL_Rect(- surface.w / 2, - surface.h / 2, surface.w, surface.h)


        text = sdl2.SDL_CreateTextureFromSurface(self.renderer, surface.surface)

        sdl2.SDL_RenderCopyEx(self.renderer, text, srcrect, dstrect, -surface.angle - angle, sdl2.SDL_Point(round(surface.w / 2), round(surface.h / 2)), sdl2.SDL_FLIP_NONE)



class Surface():
    def __init__(self, w, h, angle = 0, depth = 32, mask = (255, 65280, 16711680, 4278190080)):

        self.type = "rect"

        self.surface = sdl2.SDL_CreateRGBSurface(0, w, h, depth, mask[0], mask[1], mask[2], mask[3]).contents
        self.renderer = sdl2.SDL_CreateSoftwareRenderer(self.surface, -1, 0)


        self.w = w
        self.h = h

        self.depth = depth
        self.mask = mask

        self.angle = angle


    def blit(self, surface, src = None, dest = None, angle = 0):
        if src:
            srcrect = sdl2.SDL_Rect(src[0][0], src[0][1], src[1][0] - src[0][0], src[1][1] - src[0][1])

        else:
            srcrect = None
        
        if dest:
            if len(dest) == 2:
                if src:
                    dstrect = sdl2.SDL_Rect(dest[0] - srcrect.w / 2, dest[1] - srcrect.h / 2, srcrect.w, srcrect.h)
                else:
                    dstrect = sdl2.SDL_Rect(dest[0] - surface.w / 2, dest[1] - surface.h / 2, surface.w, surface.h)

            elif len(dest) == 4:
                dstrect = sdl2.SDL_Rect()
                dstrect.w = dest[1][0] - dest[0][0]
                dstrect.h = dest[1][1] - dest[0][1]
                dstrect.x = dest[0][0] - dstrect.w / 2
                dstrect.y = dest[0][1] - dstrect.h / 2
            
            else:
                raise IndexError("\'dest\' should have 2 or 4 values. ")
        else:
            if src:
                dstrect = sdl2.SDL_Rect(dest[0] - srcrect.w / 2, dest[1] - srcrect.h / 2, srcrect.w, srcrect.h)
            else:
                dstrect = sdl2.SDL_Rect(0 - surface.w / 2, 0 - surface.h / 2, surface.w, surface.h)
        
        text = sdl2.SDL_CreateTextureFromSurface(self.renderer, surface.surface)

        sdl2.SDL_RenderCopyEx(self.renderer, text, srcrect, dstrect, -surface.angle - angle, sdl2.SDL_Point(round(surface.w / 2), round(surface.h / 2)), sdl2.SDL_FLIP_NONE)
    
    def fill_circle(self, colour, filled = True):

        self.type = "circle"

        if self.w >= self.h:
            draw_circle(self, round(self.w / 2), round(self.h / 2), round(self.h / 2), (colour[0], colour[1], colour[2], 255), filled)
        else:
            draw_circle(self, round(self.w / 2), round(self.h / 2), round(self.w / 2), (colour[0], colour[1], colour[2], 255), filled)
    
    def fill(self, colour):
        self.type = "rect"
        
        colour = (colour[0] % 256, colour[1] % 256, colour[2] % 256)
        sdl2.SDL_SetRenderDrawColor(self.renderer, colour[0], colour[1], colour[2], 255)
        sdl2.SDL_RenderClear(self.renderer)
    
    def rotate(self, angle):
        if self.type == "rect":
            self.angle += angle


    def get_rect(self, x, y):
        return Rect(x, y, self.w, self.h, self.angle)
    
    def get_circle(self, x, y):
        if self.w >= self.h:
            r = self.h / 2
        else:
            r = self.w / 2
        #x += self.w / 2
        #y += self.h / 2
        return Circle(x, y, r)

def events():
    return sdl2.ext.get_events()

def draw_circle(surface, x, y, rad, colour = (0, 0, 0, 0), Filled = True):
    if Filled:
        gfx.filledCircleRGBA(surface.renderer, x, y, rad, colour[0], colour[1], colour[2], colour[3])
    
    else:
        gfx.circleRGBA(surface.renderer, x, y, rad, colour[0], colour[1], colour[2], colour[3])

def draw_rect(surface, x, y, w, h, angle = 0, colour = (0, 0, 0)):
    surf = Surface(w, h)
    surf.fill((colour[0], colour[1], colour[2]))
    text = sdl2.SDL_CreateTextureFromSurface(surface.renderer, surf.surface)
    
    dstrect = sdl2.SDL_Rect(x, y, w, h)

    sdl2.SDL_RenderCopyEx(surface.renderer, text, None, dstrect, -angle, sdl2.SDL_Point(0, 0), sdl2.SDL_FLIP_NONE)

def load(bitmap):
    return sdl2.SDL_LoadBMP(bitmap)


def exit():
    sdl2.SDL_Quit()
    sys.exit()
