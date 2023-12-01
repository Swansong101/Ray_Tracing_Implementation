# Glow in the Dark Mini Game 
This project features the use of python language and provided libraries to create a mini game where the sprite navigates through a dark maze.

## Functionalities

- Player registration with name and age input.
- Character selection from a list of available characters.
- Multiple levels with varying mazes and challenges.
- Collection of treasures to earn points.
- Avoidance of enemies to prevent collisions.
- Progression to the next level upon reaching the exit door.
- Game over when colliding with enemies or collecting all treasures.
- Sound effects for game events.

## How to Play

1. Clone the project to your local machine:

    ```bash
    git clone https://github.com/your-username/glow-in-the-dark-maze.git
    ```

2. Navigate to the project directory:

    ```bash
    cd glow-in-the-dark-maze
    ```

3. Run `main.py` to start the game.
4. Register your name and age.
5. Select a character.
6. Navigate through the maze using arrow keys.
7. Collect treasures and avoid enemies.
8. Reach the exit door to progress to the next level.
9. Game over conditions: Colliding with enemies or collecting all treasures.

## Levels

The game currently has three levels with increasing difficulty. Each level introduces new challenges and maze layouts.
## Snapshots 
<img width="960" alt="Screenshot 2023-12-01 144621" src="https://github.com/alexwafula/glowinthedark/assets/91899603/7a56af62-1d6d-4918-ba01-febed1eb59b6">
<img width="960" alt="Screenshot 2023-12-01 144636" src="https://github.com/alexwafula/glowinthedark/assets/91899603/b14097a7-0592-45cc-bf9f-700caac657a5">

## Dependencies

### Python 3.x
 Download Python 3.x from the [official Python website](https://www.python.org/downloads/). Choose the version that matches
  your operating system. Follow the installation instructions provided on the website for your specific operating system.

   - For Windows, make sure to check the option that says "Add Python to PATH" during installation.
   - For macOS, you may need to adjust your `PATH` environment variable after installation.
   - For Linux, Python is often pre-installed. If not, use your package manager to install it.

   Ensure that Python is successfully installed by opening a terminal or command prompt and typing:

   ```bash
   python --version
   ```

### Pygame
You can install Pygame using pip, the Python package installer. Open a terminal or command prompt and run the following command:
```bash
pip install pygame
```

### Turtle graphics
Turtle graphics is included in the Python standard library, so there's no separate installation needed. You can use it directly in your Python scripts.

### Turtle sound libraries
We used mixer from the pygame library and the code used is
```bash
import pygame
pygame.init()
pygame.mixer.init()
```

## Credits

- **Game Development:**
  - [Ruby Mbete](https://github.com/r-mbete)
  - [Alex Wafula](https://github.com/alexwafula)
  - [Charis Orony](https://github.com/quantumfelonies)
  - [Nicole Owens](https://github.com/Swansong101)
  - [Peter Kimutai](https://github.com/KimutaiPeter)
  

- **Sound Effects:**
  - [Peter Kimutai](https://github.com/KimutaiPeter)
  - [Charis Orony](https://github.com/quantumfelonies)
    
## License

This project is licensed under the [LICENSE NAME] - see the [LICENSE.md](LICENSE.md) file for details.
