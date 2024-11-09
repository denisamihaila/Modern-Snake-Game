# 🐍 Modern Snake Game

![image](https://github.com/user-attachments/assets/04c12211-6942-4606-b9f5-5674e40be111)
![image](https://github.com/user-attachments/assets/9addec0a-5dd5-4b1a-9a3f-0c694f1a036d)
![image](https://github.com/user-attachments/assets/549da0b6-becd-482b-a141-60572e5c2cbc)


## Overview

This project is a **Modern Snake Game** implemented in **Python** using the **Pygame library**. The game includes enhancements beyond the classic snake game, such as multiple enemies, food, level progression, and a high score feature that saves the best score across sessions. The game demonstrates various concepts, including animation, collision detection, and game state management.

## 🚀 Features

- **Advanced Gameplay**: Features include snake growth, increasing speed, and level progression with additional enemies.
- **Enemy Objects**: Enemies appear as obstacles and increase in number as the player progresses through levels.
- **Score Tracking**: Tracks the player’s score and saves the high score in a file (`highscore.txt`), preserving it between game sessions.
- **Customizable Settings**: Adjusts game speed, block size, and difficulty as the game progresses.
- **Graphics**: Integrates background, snake, food, and enemy images for an immersive experience.

## 📂 Project Structure

The project files are organized as follows:

- **Snake Class**: Manages the snake’s position, movement, growth, and rendering.
- **Food Class**: Handles the food’s random positioning and rendering.
- **Enemy Class**: Creates enemy objects that spawn and increase with level progression.
- **Game Functions**: Includes functions for displaying score, high score, and end messages, as well as managing the game state and collisions.

## 📝 Usage

Upon starting the game, control the snake using the arrow keys. The goal is to eat food to grow the snake and increase your score, while avoiding collision with enemies or the snake's own body. Each level introduces new enemies, making the game progressively challenging.

### Controls

- **Arrow Keys**: Move the snake in the desired direction.
- **Q**: Quit to the main screen when prompted.
- **C**: Continue and restart the game after a game over.

## ✨ Code Highlights

The code demonstrates several key programming concepts:

1. **Class-Based Design**: Uses OOP principles to manage the Snake, Food, and Enemy as individual classes.
2. **Collision Detection**: Implements accurate collision detection for food, enemies, and snake segments.
3. **File I/O for High Score**: Reads and writes the high score to a file, ensuring persistence across sessions.
4. **Dynamic Difficulty**: Increases game speed and enemy count as the player’s score progresses.

## 🔧 Future Improvements

Potential improvements to enhance the game:

- **Sound Effects**: Add sound effects for actions such as eating food, colliding, or progressing to a new level.
- **Additional Levels**: Introduce more distinct levels with unique themes or obstacles.
- **Power-Ups**: Add items that temporarily increase speed, slow down enemies, or provide immunity.
- **Enhanced Graphics**: Improve the graphical assets and animations for a more polished look.
