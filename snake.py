import engine, math, random

# Initialise display
display = engine.Display(400, 400, title = "Snake Game")
display.update()

# Initialise clock
clock = engine.Clock()

# Class for the body and head of the snake

class Snake(engine.Sprite):
    def __init__(self):
        # Set position to be off screen, and rotated at a 45 degree angle. 
        super().__init__(x = -10, y = -10, angle = 45)

        # Create the surface for the body, making it white. 
        self.image = engine.Surface(round(math.sqrt(200)), round(math.sqrt(200)), angle = 45)
        self.image.fill((255, 255, 255))

        # Create collider from self.image by calling self.get_rect(). 
        self.collider = self.get_rect()
        
# Create group of sprites to be drawn every frame (body + apple), and another for just the body
all_sprites = engine.Group()
body = engine.Group()

class Head(Snake):
    def __init__(self):
        super().__init__()
        # Set direction to going to the right
        self.dir = 0
        # Move to correct position. 
        self.move((200, 200))
        
    
    def update(self):
        if not self.dir:
            self += (20, 0)
        elif self.dir == 1:
            self -= (0, 20)
        elif self.dir == 2:
            self -= (20, 0)
        elif self.dir == 3:
            self += (0, 20)
        
        # Check for collisions with body, apple, or border
        for sprite in body.sprites:
            if engine.collision(self.collider, sprite.collider):
                engine.exit()
        
        for sprite in all_sprites.sprites:
            if type(sprite) == Apple:
                if engine.collision(self.collider, sprite.collider):
                    all_sprites.sprites.remove(sprite)
                    all_sprites.add(Apple(self))
                    body.add(Body())
        
        if self.coords[0] < 0 or self.coords[0] > 400 or self.coords[1] < 0 or self.coords[0] > 400: 
            engine.exit()

class Body(Snake):
    def __init__(self):
        super().__init__()


class Apple(engine.Sprite):
    def __init__(self, snake):
        super().__init__()
        self.image = engine.Surface(20, 20)
        self.image.fill_circle((255, 0, 0))
        
        self.collider = self.get_circle()

        coords = (20 * random.randint(0, 20), 20 * random.randint(0, 20))

        while coords == snake.coords:
            coords = (20 * random.randint(0, 20), 20 * random.randint(0, 20))
        

        self.move(coords)

snake = Head()
apple = Apple(snake)

all_sprites.add(snake, apple)

while True:
    # Set framerate to 10 using clock.tick(10)
    clock.tick(10)

    # Get events of the last frame
    events = engine.get_events()

    for event in events:
        # Detect if someone has pressed the X button
        if event.type == engine.QUIT:
            engine.exit()
    

    # Take inputs. 
    if engine.is_pressed(ord("w")) and snake.dir != 3: snake.dir = 1
    elif engine.is_pressed(ord("a")) and snake.dir != 0: snake.dir = 2
    elif engine.is_pressed(ord("s")) and snake.dir != 1: snake.dir = 3
    elif engine.is_pressed(ord("d")) and snake.dir != 2: snake.dir = 0
    
    # Update all sprites
    
    
    # Update body. 
    if len(body.sprites) > 1:
        for i in range(len(body.sprites), 1, -1):
            body.sprites[i - 1].move(body.sprites[i - 2].coords)
    
    if body.sprites:
        body.sprites[0].move(snake.coords)
    
    snake.update()


    # Draw sprites onto display and refresh
    display.fill((0, 0, 0))
    all_sprites.draw(display)
    body.draw(display)

    
    display.update()