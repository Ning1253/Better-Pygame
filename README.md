# Better-Pygame
My EPQ project - the creation of a 2D game engine in Python (a sort of pygame, if you will) except that it supports drawing rotated images and shapes, as well as rotated rectangular and circular hitboxes.

Features:
  - Graphics Windows, Surfaces
  - Collision Detection
  - Support for rectangles (and hitboxes) rotated in any direction
  - Python-esque code
  - DLLs for both 32bit and 64bit windows to allow for faster maths calculations in the background
  - FPS control

# Documentation:

`import engine`. This will directly import everything necessary for your project. 

## Graphics:
### Window:

`Display(width, height, title="Better Pygame")`. Optionally one can also add the arguments `x` and `y` to set the coordinates of the window onto the screen. 

####   Methods:
`Display.update()` - refresh the display. 

`Display.fill(colour) - fill the display, with colour being an rgb length 3 tuple. 

`Display.blit(surface, src = None, dest = None, angle = 0)` - copy a surface onto the display. Optional args:
  - `src`: A pair of tuples dictating the topleft and bottomright corners of the area of the surface to blit from. 
  - `dest`: A tuple dicating the centre of the destination where the surface will be blit. 
  - `angle`: the angle at which the surface will be drawn, where positive = anti-clockwise. 


### Surface:

`Surface(width, height, angle = 0, depth = 32)` - create a new Surface object which you can draw on. Optional args:
  - `angle`: the angle at which the surface will be drawn if it is drawn onto a display, where positive = anti-clockwise. If one takes a rotated surface and draws it rotated more onto a display, the angles will add up.
  - `depth`: the depth of the surface is the level onto which it is drawn - higher or lower number means it will be drawn above or below other surfaces.
  - `mask`: Do not edit this unless you know what you are doing. An rgb tuple of form (r, g * 256, b * 256 ^ 2, a * 256 ^ 3). 

####   Methods:
`Surface.blit(surface, src = None, dest = None, angle = 0)` - blit a surface onto current surface. Works in the same way as Display.Surface(). 

`Surface.fill(colour)` - fill the surface with a colour of the form rgb, or the form rgba.

`Surface.fill_circle(colour)` - fill as large a circle as possible within the surface, with a colour of the form rgb, or the form rgba. 

`Surface.rotate(angle)` - change the default rotation of the surface by `angle`. Enables one to rotate a surface without re-initialising it. 

`Surface.get_rect()` - returns a Rect() collider object with coords and size of surface. 

`Surface.get_circle()` - returns a Circle() collider object with coords of the centre of the surface, and a size as large as possible which still fits in the surface. 

### Other functions:
`draw_circle(surface, x, y, rad, colour = (0, 0, 0, 0), Filled = True)` - draw a circle onto the chosen surface at chosen coordinates. Optional args:
  - `rad` - the radius of the circle to draw. 
  - `colour` - a tuple of the form rgb or rgba dictating the colour of the circle to draw
  - `Filled` - bool, whether or not to fill in the circle or draw only the outline. 
 
`draw_rect(surface, x, y, w, h, angle = 0, colour = (0, 0, 0))` - draw a rectangle onto the chosen surface at chosen coordinates. Optional args:
  - `colour` - a tuple of the form rgb or rgba dictating the colour of the rectangle to draw
  - `angle` - the angle to draw the rectangle at. 
