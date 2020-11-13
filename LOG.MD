# Project Log

## Initial Planning - 21/09/2020-22/09/2020


The aim of this project will be to create a fully functional game engine which I could use to create a video game. After a bit of thinking, here are the decisions which I feel   would be most beneficial to the project.
  - The interface between the programmer and the code will be written in Python. The idea is to have this program be a Python Library, which the programmer can use to make his game, similar to the currently existing "Pygame" library, but with some features built to my preference. 
  - The mathematical sections which will be used the most, especially collision detection, will be coded in C. The reason for this is that C is an extremely fast language, being at a very low level, and unlike (for example) C# it is very easy to integrate as code in other languages. Creating this section in Python would cause the program to be too slow, so that is not at all something I would want to do.
  - The engine will use the graphics library SDL2.0, a library available for pretty much every OS which is currently in use. It is decently fast, easy to use, and does not require prerequisite drivers which other drivers and graphics libraries may use.
    - I will not be using my own graphics library because this would require interfacing with graphics card drivers, which is an altogether different subject for much lower level computing. 
  - Finally, I will most likely continue this project until it is in a working form - it will be considered complete once I have integrated all the features that I would need to create a low level game such as Snake or Pong. 

## Section 1: Collision Detection, in C. 23/09/2020-08/10/2020
#### 23-24/09/2020
- Installed an environment to be able to easily code in C - this involves VS Code 2019, and a few home-made batch files to Compile, Run, and Send to DLL various C files to allow for easy integration with Python when this eventually comes. 
- Coded rectangle collision, coded rectangle and circle collision, coded circle collision
#### 25/09/2020
- Rectangle and Circle Collision was completely wrong, so I have decided to remake it from scratch. I also recoded the Rectangle Collision using SAT, the [Separating Axis Theorem](https://en.wikipedia.org/wiki/Hyperplane_separation_theorem), which describes a way to calculate whether two polygons intersect.
![Collision2](/circrect.png)
#### 26-30/09/2020
- Dusted up code, made sure it worked. (Spoiler: It didn't, so I coded it again). 
- Finally got the Rectangle Collision and Circle Collision to work, so that's done. The Circle Rectangle Collision seems to work at least most of the time, so I will leave it for now to not get sidetracked. 
![Collision1](/rect.png)
![Code1](/code1.png)
#### 01-08/10/2020
- Created the wrappers for my various functions. Started planning for how I will create the various classes for colliders, which uses quite a lot of maths heavy equations - below is an example, for the coordinates of one corner of a rectangle based on its angle, its topleft corner, its width and its height:
![Maths](/maths1.png)

## Section 2: Display and Surfaces. Start of Python part of the project. 11/10/2020 - 25/10/2020
#### 11/10/2020
- Finally created Github page after having coding colliders!! This will be imperative for the future of the project:
  - It will allow me to store previous iterations of files in case of corruption or code which does not work.
  - It will allow me to keep an organised version of my work which I can edit as I please
  - It allows for working between devices, say for example between my laptop and my PC. 
#### 12/10/2020 - 16/10/2020
- Talked to Mrs Ralph about the progress of my project, and completed my Project Form's first iteration. 
- Programmed the display part of the project - this will probably still be a WIP for a while, considering the complexity of what I have to code. 
- I also started on the code for the display, although this may take a while - it will be imperative to make the code from here-on extremely neat, to allow for editing in the future if I decide to change any feature or code. 
#### 17/10/2020 - 25/10/2020
- Display and Surfaces now work. Decided to make coordinates centre-locked to allow for much easier work with rotations. Re-edited DLL C files to suit this. They are hopefully working now. 
- Started looking at already completed video games on [GameDev](https://www.gamedev.net) to look for features which may be useful in the next part of the project, the user library. 
