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
`blit(surface, src = None, dest = None, angle = 0)` - blit a surface onto current surface. Works in the same way as Display.Surface(). 

`fill(colour)` - fill the surface with a colour of the form rgb, or the form rgba.

`fill_circle(colour)` - fill as large a circle as possible within the surface, with a colour of the form rgb, or the form rgba. 

`rotate(angle)` - change the default rotation of the surface by `angle`. Enables one to rotate a surface without re-initialising it. 

`get_rect()` - returns a Rect() collider object with coords and size of surface. 

`get_circle()` - returns a Circle() collider object with coords of the centre of the surface, and a size as large as possible which still fits in the surface. 

### Other functions:
`draw_circle(surface, x, y, rad, colour = (0, 0, 0, 0), Filled = True)` - draw a circle onto the chosen surface at chosen coordinates. Optional args:
  - `rad` - the radius of the circle to draw. 
  - `colour` - a tuple of the form rgb or rgba dictating the colour of the circle to draw
  - `Filled` - bool, whether or not to fill in the circle or draw only the outline. 
 
`draw_rect(surface, x, y, w, h, angle = 0, colour = (0, 0, 0, 0))` - draw a rectangle onto the chosen surface at chosen coordinates. Optional args:
  - `colour` - a tuple of the form rgb or rgba dictating the colour of the rectangle to draw
  - `angle` - the angle to draw the rectangle at. 

## Sprites:
`Sprite(x = 0, y = 0, angle = 0)` - create a new Sprite object.

Sprite objects have the following inbuilt methods/variables:
  - `image` - the image pasted onto the screen using the sprite.draw() method
  - `collider` - the hitbox of the sprite, to be used when checking collision between sprites - will be updated if the sprite is moved, or rotated. 
  - `x, y, angle` - self explanatory - angle is anticlockwise.
  - `+=` - it is possible to move a sprite by adding (or subtracting) a tuple to (or from) it, for example `sprite += (10, 0)` or `sprite -= (5, 6)`. 
  - `rotate(angle)` - rotate the sprite, image and collider all by a certain angle.
  - `draw(surface)` - draw the image of the sprite onto the chosen surface. Will draw it with angle `sprite.angle` mentioned above, at coords `x, y` above.
  - `get_rect(self)` - finds rect object for the sprite's image, as per the function `surface.get_rect`. 
  - `get_circle(self)` - similarly, finds maximum circle object for sprite's image. 
  - `update()` - this method can be changed when making one's own child class - it is called automatically in sprite groups, so it is preferable to keep the name the same. 

### Groups
`Group()` - Creates a new sprite group. These can be used to update multiple sprites at once. 
#### Methods
`add(*sprites)` - add as many sprites to the group as you want, one after the other (the same syntax as if you wanted to print multiple variables at once: `add(sprite1, sprite2, sprite3)`). 
`update()` - run the `update()` method for all sprites within the group. 
`draw(surface)` - draws all sprites within the group to the chosen surface. Again, the rotation and position of each sprite will be dictated by its current `x, y, angle` variables. 

## Colliders
There are three types of colliders - `Rect()`, `Circle()` and `PixelArray()` (although PixelArray hasn't been properly intergrated yet, it is still supported by the `collision()` function). 
##### Note: Colliders and objects generally use centred coordinates, so initialising an object at (0, 0) will put its centre, not its topleft corner, at those coords.
### Functions
`collision(obj1, obj2)` - detects whether two collider objects are touching, and returns `True` if they are, `False` if they are not. 
#### Rect
  - `Rect(x, y, width, height, angle = 0)` - pretty self explanatory. Creates a new `Rect()` collider with coords (x, y) and width and height as written. An optional `angle` parameter allows for the object to be created already rotated in some way. 
  - `update(x, y, width, height, angle = 0)` - allows you to essentially move the object in any way you want without needing to actually create a new object.
  - `rotate(angle)` - rotate the `Rect` collider by a certain angle. 
  - Like sprites it is possible to move any of these objects using `+=` or `-=`. 
  - `shiftx(num)` - move the rectangle horizontally bu `num` pixels. 
  - `shifty(num)` - as above but for height. 
  - `move(coords)` - "teleport" the object to any location written as an (x, y) tuple. 

#### Circle
  - `Circle(x, y, rad)` - create a new `Circle()` collider with coords (x, y) and radius as written.
  - `update(x, y, rad)` - move and/or resize the circle collider in any way you want without needing to reinitialise the object. 
  - Once again `+=` and `-=` can be used for movement, using tuples.
  - `move(coords)` - "teleport" the circle collider to any coords written as an (x, y) tuple. 

#### PixelArray
###### Will be updated once this is supported in a much more direct fashion than it currently is. 

## Taking Inputs
An `Event()` is, well, an event which takes place whenever a key is pressed or the mouse is moved or basically any event happens. The codes for the letters and numbers, as well as the space bar, is simply `ord("char")` for the character you wish. Events have the following properties:
  - `type` - the type of event it is. The types of events are:
```
    - AUDIODEVICEADDED
    - AUDIODEVICEREMOVED

    - CONTROLLERAXISMOTION
    - CONTROLLERBUTTONDOWN
    - CONTROLLERBUTTONUP

    - CONTROLLERDEVICEADDED
    - CONTROLLERDEVICEREMOVED
    - CONTROLLERDEVICEREMAPPED

    - FINGERMOTION
    - FINGERDOWN
    - FINGERUP

    - KEYDOWN
    - KEYUP

    - JOYAXISMOTION
    - JOYBALLMOTION


    - JOYHATMOTION

    - JOYBUTTONDOWN
    - JOYBUTTONUP

    - JOYDEVICEADDED
    - JOYDEVICEREMOVED

    - MOUSEMOTION

    - MOUSEDOWN
    - MOUSEUP

    - MOUSEWHEEL

    - MULTIGESTURE

    - QUIT

    - SYSWMEVENT

    - TEXTEDITING

    - TEXTINPUT

    - USEREVENT

    - WINDOWEVENT
```
  - These can be accessed like so: `engine.EVENTNAME`. 
  - `key` - If a key was pressed or unpressed, the code of that key. 
  - `event` - in case you want access to the original SDL2 event which was returned.
  - `x` and `y` for those events which would use those. 
  - `button` - for controller or mouse pressed or releases
  - `clicks` - the amount of times the button was pressed for the event, like a single or double click. 

#### Functions:
  - `get_events()` - returns an array with all events which have happened since this function was last called. It is recommended to call this function whether or not the events will be used. 
  - `get_pressed()` - returns an array with `1`s for every key code which is currently pressed/held down and `0`s for those which are not so.
  - `is_pressed(key)` - returns `True` if the inputted key code is currently pressed and `False` if it is not.
    - There is a list of key codes [here](https://wiki.libsdl.org/SDLKeycodeLookup). 

## Misc. 
  - `Clock()` - returns a `Clock()` object. Its main functionality is its `tick(freq)` method, which should be called at the start of the game loop. Its job is to limit the framerate, so `tick(30)` will limit the FPS to 30. 
  - `exit()` - force close the app. Should be used as the way to exit the game once everything else is done. 
