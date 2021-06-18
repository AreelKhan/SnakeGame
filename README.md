# SnakeGame
Snake Game in python. This was my first time using the pygame module.
I watched a step by step youtube tutorial to code this.
Credit goes to Clear Code.
Link to youtube video:
https://www.youtube.com/watch?v=QFvqStqPCRU&t=6843s

## Implementation:
This Snake game is written in python. In the frontend, the GUI is designed using the pygame module. The user can make inputs using the keyboard. In the backend, the game is designed as a grid of cells. The position of the head of the snake is stored as a tuple of coordinates while the direction the snake is moving in is stored as a 2D vector. When a user makes an input, the direction of the 2D vector is updated accordingly. When the position of the snake equals the position of the apple, the position of the apple is changed arbitrarily and the length of the snake is incremented by one. 
