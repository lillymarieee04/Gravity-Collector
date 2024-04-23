# Gravity-Collector

Game Design Document (FINAL – Gravity Collector)

![alt text](image-3.png)


Summary of Project Goals:
    The player controls a blue box (representing the player character) using the arrow keys. The goal is to collect yellow squares that appear randomly on the screen while avoiding hitting the bottom of the screen. The player wins by collecting all the squares, and the game ends if the player hits the bottom without collecting all the squares. Every time a player collects one square, they restart and fall faster.


Instructions for the Player:
    Use the left and right arrow keys to move the blue box horizontally.
    Collect the yellow squares by moving the blue box over them.
    Avoid hitting the bottom of the screen.
    Collect all squares to win the game.

Technologies and Techniques Used:
    Python.
    Pygame.
    Random number generation for positioning squares on the screen.
    Collision detection to determine interactions between game objects.

Citations for External Resources:
    No external resources were used in the development of this project.


Description of Process:

    - Planning: Defined the game concept and mechanics, including player controls, win conditions, and game over conditions.

    - Coding: Implemented the game logic using Python and the Pygame library, including defining classes for the player character and squares, handling player input, updating game state, and rendering graphics.
    Testing: Conducted testing to ensure that player controls function as intended, collisions are detected accurately, and game over/win conditions are triggered correctly.

    - Refinement: Made the movement with arrow keys easier. As well as having the player move slower in the beginning and then faster with each collected square.


Lessons Learned:
    Learned how to use the Pygame library.
    Gained experience in implementing collision (similar to an earlier game we made, but fancier).


Challenges Faced:
    Understanding Pygame's event loop and event handling.
    Managing game state and transitioning between different states (e.g., game running, game over).
    SimpleGE was confusing to me with how to implement, I would have them in my directory and it would still not work.


Areas for Improvement:
    Adding sound effects and actual graphics instead of placeholders.
    Making the game fancier instead of just collecting squares. 
    Using SimpleGE effectively
    The game doesn’t crash if a player wins or loses.


Changes for Next Time:
    Trying to work with SimpleGE, it would work sometimes and other times it wouldn’t.
    Making the game fancier. 
    The game doesn’t crash if a player wins or loses.


Adherence to Game Design Document:
    The project largely adhered to the game design document, fulfilling the core objectives of player movement, square collection, and game over/win conditions. However, some additional features, such as sound effects and animations, were not included in the initial design but could be considered in future iterations.


Staying on Track:
    To stay on track, regular testing and debugging sessions were conducted to identify and address any issues promptly. Additionally, adhering to a structured development process helped maintain focus and progress towards achieving project goals.
