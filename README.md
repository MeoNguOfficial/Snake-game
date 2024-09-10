# SNAKE GAME - RẮN SĂN MỒI

## Overview
This is a simple implementation of the classic Snake game using the Pygame library in Python. Players control a growing snake that must consume food while avoiding walls and its own tail. As the game progresses, obstacles appear, and the snake's speed increases, adding to the challenge.

## Features
- **Fixed Window Size**: The game runs in a window of 1600x900 pixels.
- **Dynamic Levels**: Players can choose levels from 1 to 10, each increasing the game speed.
- **Invert Control**: Players can toggle inverted control for an additional challenge.
- **Sound Effects**: The game includes sounds for eating food, pausing, game over, and achieving high scores.
- **High Score Tracking**: The game tracks high scores for each level.

## Requirements
To run the game, make sure you have:
- Python installed (preferably version 3.6 or higher).
- Pygame library installed. You can install it via pip:
  ```bash
  pip install pygame
  ```

## Game Controls
- **Arrow Keys**: Control the direction of the snake.
- **Space Bar**: Toggle inverted control.
- **Number Keys (0-9)**: Choose the game level (0 for level 10).
- **Escape Key**: Pause/Unpause the game.

## Installation
1. Clone the repository or download the code file to your machine.
2. Ensure that the audio files are located as specified in the code (or modify the paths accordingly):
   ```
   ../Game1/Resources/eat_food.mp3
   ../Game1/Resources/pause_game.mp3
   ../Game1/Resources/high_score.mp3
   ../Game1/Resources/invert_control.mp3
   ../Game1/Resources/game_over.mp3
   ../Game1/Resources/start_game.mp3
   ```
3. Run the game by executing the Python file:
   ```bash
   python snake_game.py
   ```

## Gameplay Mechanics
- **Snake Movement**: The snake moves continuously in the last direction specified by the player. It grows in length each time it eats food.
- **Scoring**: Players gain points based on the current level; the higher the level, the more points are awarded for each food item consumed.
- **Obstacles**: As players gather points, the game randomly generates obstacles that the snake must avoid.
- **Game Over**: The game ends if the snake runs into the walls, itself, or an obstacle. Players can restart the game by pressing the arrow keys after a game over.

## Volume Control
While the game is paused, players can adjust the music and sound effect volumes using sliders with the mouse cursor.

## Conclusion
Enjoy the challenge of the Snake game and try to beat your high score! Happy gaming!

---

If you have any questions or bug detected, feel free to contact the developer or contribute to the project.
