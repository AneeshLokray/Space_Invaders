# Space Invaders

Space Invaders is a classic arcade game built with Pygame, where players control a spaceship to defeat waves of aliens and achieve the highest score possible.

## Features

- **Player-controlled spaceship** that can move left and right and shoot bullets.
- **Multiple waves of aliens** that move and shoot back at the player.
- **Health system** for the player's spaceship.
- **Score system** that rewards the player for shooting down aliens.
- **Explosions and sound effects** to enhance gameplay experience.
- **Username input** to track high scores.
- **Leaderboard** to display top scores.
- **Background music** playing during the game.

## Prerequisites

- Python 3.x
- Pygame library

## Installation

To run the game, follow these steps:

1. **Python Installation:**
   - Ensure you have Python 3.x installed on your system.

2. **Pygame Installation:**
   - Install the Pygame library if you haven't already:
     ```sh
     pip install pygame
     ```

3. **Clone the Repository:**
   - Clone or download this repository to your local machine:
     ```sh
     git clone https://github.com/AneeshLokray/Space_Invaders.git
     cd Space_Invaders
     ```

4. **Ensure Required Assets:**
   - Make sure the following images and sounds are in the `img` directory within the game's folder:
     - `bg.png`: Background image
     - `spaceship.png`: Spaceship image
     - `bullet.png`: Player bullet image
     - `alien1.png`, `alien2.png`, `alien3.png`, `alien4.png`, `alien5.png`: Alien images
     - `alien_bullet.png`: Alien bullet image
     - `exp1.png`, `exp2.png`, `exp3.png`, `exp4.png`, `exp5.png`: Explosion images
     - `explosion.wav`, `explosion2.wav`, `laser.wav`: Sound effects
     - `stranger_things.mp3`: Background music

## How to Play

1. **Run the Game:**
   - Open a terminal or command prompt.
   - Navigate to the `Space_Invaders` directory.
   - Start the game by running:
     ```sh
     python Space_Invaders.py
     ```

2. **Game Controls:**
   - Use the **left** and **right arrow keys** to move the spaceship.
   - Press the **spacebar** to shoot bullets from the spaceship.

3. **Objective:**
   - Destroy all aliens to win the game.
   - Avoid getting hit by alien bullets.

4. **Game Over:**
   - The game ends when all aliens are destroyed (win) or the spaceship's health is depleted (lose).

5. **Options After Game Over:**
   - You can choose to **play again**, **quit**, or **view the leaderboard**.

## Code Breakdown

### Game Components

- **Spaceship Class:** Handles player spaceship movement, shooting bullets, and health management.
- **Bullets Class:** Manages player bullets and detects collisions with aliens.
- **Aliens Class:** Controls alien behavior, including movement patterns.
- **Alien_Bullets Class:** Manages bullets fired by aliens and detects collisions with the player spaceship.
- **Explosion Class:** Animates explosion effects when objects are destroyed.

### Additional Features

- **Background Music:** Continuous playback of background music during gameplay.
- **Username Input:** Input prompt at the start to enter a username for tracking high scores.
- **Leaderboard:** Displays top scores with usernames, saved in a text file.

---

Enjoy playing Space Invaders and aim for the high score! 🚀👾
