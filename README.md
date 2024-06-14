Space Invaders
A simple Space Invaders game implemented using Pygame. The player controls a spaceship to shoot down waves of aliens and achieve the highest score possible.

Features
Player-controlled spaceship that can move left and right and shoot bullets.
Multiple waves of aliens that move and shoot back at the player.
Health system for the player's spaceship.
Score system that rewards the player for shooting down aliens.
Explosions and sound effects to enhance gameplay experience.
Username input to track high scores.
Leaderboard to display top scores.
Background music playing during the game.
Prerequisites
Python 3.x
Pygame library
Installation
Ensure you have Python 3.x installed.
Install Pygame library if you haven't already:
sh
Copy code
pip install pygame
Clone or download this repository.
Ensure the following images and sounds are in the img directory:
bg.png (background image)
spaceship.png (spaceship image)
bullet.png (bullet image)
alien1.png, alien2.png, alien3.png, alien4.png, alien5.png (alien images)
alien_bullet.png (alien bullet image)
exp1.png, exp2.png, exp3.png, exp4.png, exp5.png (explosion images)
explosion.wav, explosion2.wav, laser.wav (sound effects)
stranger_things.mp3 (background music)
How to Play
Run the game:
sh
Copy code
python space_invaders.py
Enter your username when prompted and press Enter.
Use the left and right arrow keys to move the spaceship.
Press the spacebar to shoot bullets.
Destroy all aliens to win and avoid getting hit by alien bullets.
When the game is over, you can choose to play again, quit, or view the leaderboard.
Code Breakdown
Game Initialization
Import necessary modules and libraries.
Initialize Pygame and Pygame mixer.
Define screen dimensions, fonts, colors, and load images and sounds.
Main Game Classes
Spaceship: Handles player spaceship's movement, shooting, and health.
Bullets: Handles player bullets and collision with aliens.
Aliens: Handles alien movement.
Alien_Bullets: Handles alien bullets and collision with player spaceship.
Explosion: Handles explosion animations.
Game Logic
Create sprite groups for spaceship, bullets, aliens, and explosions.
Generate aliens and handle their movement and shooting.
Update and draw all sprites.
Handle player input for movement and shooting.
Check collisions between bullets and aliens, and between alien bullets and the spaceship.
Display score and health on the screen.
Save and load high scores to a text file.
Display leaderboard and allow replaying the game.
Additional Features
Background music plays during the game.
Username input at the beginning to track high scores.
Leaderboard displays top scores with username and score.
