# Zombie Survival Game

Run for your life as a zombie apocalypse breaks loose. Navigate a treacherous maze, blast away hordes of undead, manage your resources, and survive against infinite waves in this fast-paced first-person shooter.

## Features

- **3D Raycasting Engine**: Built from scratch using Python and Pygame for a retro 2.5D FPS aesthetic.
- **Wave-Based Survival**: Survive against infinite waves of enemies. Defeating all enemies triggers a new, more difficult wave with exponential enemy scaling.
- **Dynamic Mini-Map**: A real-time grid-based mini-map with a directional indicator to help you navigate the maze and track your surroundings.
- **Smart Enemy AI**: NPCs use optimized **A* pathfinding** to navigate the map and hunt down the player dynamically.
- **Loot & Resource Management**: Scavenge for dynamically respawning Health Packs and Ammo Crates. Auto-healing only recovers up to 50% of your health, making resource management critical.
- **Arsenal of Weapons**: Equip yourself with different weapons (Pistol, Shotgun, Assault Rifle). Each weapon features unique ammo capacities, fire rates, and realistic distance-based damage drop-off.
- **Multiple Enemies**: Face off against various enemy types including Male/Female Zombies, Industrial Zombies, Soldiers, CacoDemons, and CyberDemons.
- **Immersive Audio & Animations**: Fully animated enemies, weapons, environmental objects, and sound effects for shooting, enemy alerts, pain, and death animations.

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

### Running as a Standalone Executable
You can bundle the game into a standalone executable using PyInstaller:
```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --add-data "resources:resources" main.py
```
You will find the executable file in the `dist/` directory! You can also package the game for the web using `pygbag`.

## How to Play

Your objective is to survive as many waves of zombies as possible. 
- **Start of a Wave:** You will spawn at a completely random location in the maze. Use your mini-map (top-left) to get your bearings.
- **Combat:** Aim carefully! Damage drops off over distance depending on your weapon. Shotguns are devastating up close but weak from afar, while Assault Rifles excel at long range.
- **Resources:** Watch your ammo counter (bottom-right). When you run low on health or ammo, explore the maze to find Health Packs (Red Cross) and Ammo Crates (Yellow/Green crates). These respawn every 30 seconds.
- **Healing:** If you take damage, find cover! Your health will slowly regenerate, but it caps out at 50%. You must find a Health Pack to restore yourself to 100%.
- **Wave Transition:** Once all enemies in a wave are defeated, you have a 5-second breather before the next, harder wave begins.

## Controls

- **W / A / S / D**: Move around
- **Mouse**: Look around
- **Left Click**: Shoot
- **1, 2, 3**: Switch weapons (1: Shotgun, 2: Pistol, 3: Assault Rifle)
- **Escape**: Quit the game

## Architecture & Code Structure

- `main.py`: Core game loop and state management
- `raycasting.py`: 3D rendering engine
- `player.py`: Player movement, collision, health mechanics, and random spawning
- `npc.py`: Enemy logic, AI states, and damage drop-off logic
- `weapon.py`: Weapon capacities, fire rates, and distance factors
- `pathfinding.py`: A* algorithm for optimized enemy navigation
- `object_renderer.py`: Handles rendering of the UI, mini-map, weapon stats, sky, and map elements
- `object_handler.py`: Manages wave logic, enemy scaling, and item respawning
- `items.py`: Definitions for Health and Ammo pickups

## License
ISC
