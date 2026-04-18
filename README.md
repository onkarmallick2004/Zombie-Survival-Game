# Zombie-Survival-Game

Run for your life as a zombie apocalypse breaks loose. Navigate a treacherous maze, blast away hordes of undead, and survive against all odds in this fast-paced first-person shooter.

## Features

- **3D Raycasting Engine**: Built from scratch using Python and Pygame for a retro 2.5D FPS aesthetic.
- **Multiple Enemies**: Face off against various enemy types including Male/Female Zombies, Industrial Zombies, Soldiers, CacoDemons, and CyberDemons.
- **Arsenal of Weapons**: Equip yourself with different weapons such as a Pistol, Shotgun, and Assault Rifle to survive the horde.
- **Smart Enemy AI**: NPCs use Breadth-First Search (BFS) pathfinding to navigate the map and hunt down the player.
- **Animated Sprites**: Fully animated enemies, weapons, and environmental objects.
- **Immersive Audio**: Sound effects for shooting, enemy alerts, pain, and death animations.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/onkarmallick2004/Zombie-Survival-Game.git
   cd Zombie-Survival-Game
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Make sure you have Python 3 installed)*

3. Run the game:
   ```bash
   python main.py
   ```
   *Alternatively, if you use npm, you can run `npm start`.*

## Controls
- **W/A/S/D**: Move around
- **Mouse**: Look around
- **Left Click**: Shoot

## Architecture & Code Structure
- `main.py`: Core game loop and state management
- `raycasting.py`: 3D rendering engine
- `player.py`: Player movement, collision, and health
- `npc.py`: Enemy logic, AI states, and animations
- `weapon.py`: Weapon behavior and firing animations
- `pathfinding.py`: BFS algorithm for enemy navigation
- `object_renderer.py`: Handles rendering of the UI, sky, and map elements

## License
ISC
