# Dodgeball Game 🎯

A fast-paced, arcade-style dodgeball game built using Python and gamebox. Players must dodge incoming balls while eliminating opponents by throwing dodgeballs back. The game increases in difficulty with each level.

## Collaboration 👥

This project was created in collaboration with Ben Cohan. It utilizes gamebox, an original work by Luther Tychonievich.

## Game Overview 🎮

**Objective:** Avoid getting hit while eliminating all opponents. Progress through levels as difficulty increases.

**Game Mechanics:**

* Move left/right to dodge incoming balls.
* Throw dodgeballs to eliminate opponents.
* Collect food items to regain health (max 3 HP).
* Survive as long as possible!

# Features 🚀

## Required Features

### User Input:
* Left (←) - Move left
* Right (→) - Move right
* Spacebar - Start the game
* D - Throw a dodgeball

### Game Over Condition:
* Player loses 1 HP when hit by a dodgeball.
* Game ends when HP reaches 0.

### Screen & Graphics:
* Game window: 800x600
* Character and dodgeballs use gamebox shapes and animations.

## Optional Features

### Health System:
* Start with 3 HP.
* Lose HP when hit; game ends at 0 HP.
* Gain HP by hitting food items with a dodgeball.

### Dynamic Gameplay:
* Dodgeballs increase in speed at higher levels.
* More enemies spawn as the game progresses.
* Enemies also throw balls at the player.

### Sprite Animation:
* Dodgeballs have randomized colors.
* Food items cycle between different sprites.

## Installation & Setup 🛠 

### Install Dependencies
Make sure you have Python installed, then install pygame and gamebox:
```
pip install pygame gamebox
```

### Run the Game 2️
```
python game.py
```

## How to Play 🕹️ 
* Move using left (←) and right (→) arrow keys.
* Press D to throw a dodgeball at your enemies.
* Dodge incoming dodgeballs from enemies.
* Collect food items (hit them with a dodgeball) to restore HP.
* Survive as long as possible and clear levels by eliminating all enemies.

