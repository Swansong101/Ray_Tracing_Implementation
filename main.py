import time
import turtle
import math
import random
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up colors
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the scr
screen_width, screen_height = 700, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Glow in the Dark Maze - Player Registration")

# Set up fonts
font_path = r"C:\Users\HP LAPTOP\glowinthedarkkk\FontsFree-Net-SLC_.ttf"
font = pygame.font.Font(font_path, 24)
small_font = pygame.font.Font(font_path, 18)

# Create a dictionary to store user input
user_info = {"name": "", "age": ""}


def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def display_registration_form():
    name_input = ""
    age_input = ""
    active_field = "name"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if active_field == "name":
                        active_field = "age"
                    elif active_field == "age":
                        user_info["name"] = name_input
                        user_info["age"] = age_input
                        return
                elif event.key == pygame.K_BACKSPACE:
                    if active_field == "name" and name_input:
                        name_input = name_input[:-1]
                    elif active_field == "age" and age_input:
                        age_input = age_input[:-1]
                else:
                    if event.unicode.isalnum() or event.unicode.isspace():
                        if active_field == "name" and len(name_input) < 15:
                            name_input += event.unicode
                        elif active_field == "age" and len(age_input) < 2:
                            age_input += event.unicode

        screen.fill(BLACK)

        # Calculate center of the scr
        center_x, center_y = screen_width // 2, screen_height // 2

        draw_text("Glow in the Dark Maze - Player Registration", font, GREEN, center_x, 50)

        draw_text("Name:", font, WHITE, center_x - 150, center_y - 50)
        draw_text(name_input, font, WHITE, center_x, center_y - 50)

        draw_text("Age:", font, WHITE, center_x - 150, center_y)
        draw_text(age_input, font, WHITE, center_x, center_y)

        draw_text("Press Enter to move to the next field", small_font, WHITE, center_x - 150, center_y + 100)

        pygame.display.flip()


# Display registration form
display_registration_form()

# Now you can access user_info["name"] and user_info["age"] in your game code
print("Player Name:", user_info["name"])
print("Player Age:", user_info["age"])


# Function to display the splash scr with a countdown
def display_splash_screen():
    splash_screen = turtle.Screen()
    splash_screen.bgcolor("black")
    splash_screen.title("Maze Game Splash Screen")
    splash_screen.setup(700, 700)

    # Create a turtle for the splash scr
    splash_pen = turtle.Turtle()
    splash_pen.speed(0)
    splash_pen.color("green")
    splash_pen.penup()
    splash_pen.hideturtle()

    # Display the splash scr text and maze picture
    splash_pen.goto(0, 100)
    splash_pen.write("Glow in the Dark Maze Game", align="center", font=("Courier", 24, "normal"))

    # Add maze picture at the center
    turtle.addshape("sodapdf-converted.gif")
    splash_pen.shape("sodapdf-converted.gif")
    splash_pen.goto(0, -50)
    splash_pen.stamp()

    # Display a countdown message
    splash_pen.color("white")
    splash_pen.goto(0, -200)

    for i in range(5, 0, -1):
        splash_pen.clear()
        splash_pen.write(f"Game starting in {i}...", align="center", font=("Courier", 16, "normal"))
        turtle.update()
        time.sleep(1)


# Function to set up the maze
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("wall.gif")
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))


# Characters available for selection
characters = [
    {"name": "Character 1", "picture": "pennywise - v2.gif"},
    {"name": "Character 2", "picture": "pennywise - v2.gif"},
    {"name": "Character 3", "picture": "pennywise - v2.gif"},
    {"name": "Character 4", "picture": "pennywise - v2.gif"},
    {"name": "Character 5", "picture": "pennywise - v2.gif"},
]

# Selected character index (default to the first character)
selected_character_index = 0


# Function to display the character selection menu
def character_selection():
    global selected_character_index

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_LEFT:
                    selected_character_index = (selected_character_index - 1) % len(characters)
                elif event.key == pygame.K_RIGHT:
                    selected_character_index = (selected_character_index + 1) % len(characters)
                elif event.key == pygame.K_RETURN:
                    # Return the selected character
                    return characters[selected_character_index]

        screen.fill(BLACK)

        # Calculate center of the scr
        center_x, center_y = screen_width // 2, screen_height // 2

        # Draw menu options
        draw_text("Character Selection", font, GREEN, center_x, 100)
        draw_text("Use Left/Right arrow keys to select", small_font, WHITE, center_x, center_y)
        draw_text("Press Enter to confirm", small_font, WHITE, center_x, center_y + 50)

        # Display the selected character picture
        selected_character = pygame.image.load(characters[selected_character_index]["picture"])
        screen.blit(selected_character, (center_x - 50, center_y + 100))

        pygame.display.flip()


# Function to display the main menu
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_1:
                    # Start the game
                    return
                elif event.key == pygame.K_2:
                    # Resume the game
                    return
                elif event.key == pygame.K_3:
                    # Character selection
                    selected_character = character_selection()
                    print("Selected Character: {}".format(selected_character["name"]))
                    # Add logic to use the selected character in the game

        screen.fill(BLACK)

        # Calculate center of the scr
        center_x, center_y = screen_width // 2, screen_height // 2

        # Draw menu options
        draw_text("Glow in the Dark Maze", font, GREEN, center_x, 100)
        draw_text("1. Start Game", small_font, WHITE, center_x, center_y)
        draw_text("2. Resume", small_font, WHITE, center_x, center_y + 50)
        draw_text("3. Character Selection", small_font, WHITE, center_x, center_y + 100)
        draw_text("4. Quit", small_font, WHITE, center_x, center_y + 150)

        pygame.display.flip()


# Display the main menu
main_menu()

# Call the function to display the splash scr
display_splash_screen()

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Glow In The Dark")
wn.setup(700, 700)
wn.tracer(0)

# Register shapes
images = ["player_right.gif", "player_right.gif", "treasure.gif", "wall.gif",
          "pennywise - v2.gif"]
for image in images:
    turtle.register_shape(image)

# Declare reflectors as a global variable
reflectors = []


# Create path
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("player_right.gif")
        self.color("white")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        # Calculate the space to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        # Calculate the space to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        # Calculate the space to move to
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        self.shape("player_right.gif")

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        # Calculate the space to move to
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        self.shape("player_right.gif")

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("treasure.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("pennywise - v2.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape("pennywise - v2.gif")
        elif self.direction == "right":
            dx = 24
            dy = 0
            self.shape("pennywise - v2.gif")
        else:
            dx = 0
            dy = 0

            # Check if player is close
            # If so, go in that direction
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        # Calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            # Choose a different direction
            self.direction = random.choice(["up", "down", "left", "right"])
        # Set timer to move to next time
        turtle.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


# Create a Door class
class Door:
    def __init__(self, position, size, picture):
        self.position = position
        self.size = size
        self.image = picture
        self.is_open = False

    def draw(self, scr):
        scr.blit(self.image, (self.position.x, self.position.y))

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def check_collision(self, player__rect):
        return player__rect.colliderect(pygame.Rect(self.position.x, self.position.y,
                                                    self.size.x, self.size.y))


# Load the door picture
door_image = pygame.image.load("door.jpg")

# Create door object
door = Door(pygame.Vector2(500, 300), pygame.Vector2(100, 200), door_image)

# Create player rectangle
player_rect = pygame.Rect(400, 350, 50, 50)

# Draw the door image onto the screen
screen.blit(door_image, (door.position.x, door.position.y))

# Create levels list
level = [""]

# Define first level
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXE          XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX       EXX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X  XXX        XXXXT XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXX",
    "X               TXXXXXXXX",
    "XXXXXXXXXXXX     XXXXX  X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXXE                    X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX        T     X",
    "XX   XXXXX              X",
    "XX  TXXXXXXXXXXXXX  XXXXX",
    "XX    XXXXXXXXXXXX  XXXXX",
    "XX           XXX      T X",
    "XXXE                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

# Add a treasure list
treasures = []
# Add enemies list
enemies = []
# Add maze to mazes list
level.append(level_1)


# Create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # Get the character at each x,y coordinate
            character = level[y][x]
            # Calculate the scr x,y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            # Check if it an X
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("wall.gif")
                pen.stamp()
                # Add coordinates to wall list
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

            if character == "E":
                # Check if it an X
                if character == "X":
                    pen.goto(screen_x, screen_y)
                    pen.shape("wall.gif")
                    pen.stamp()
                    # Add coordinates to wall list
                    walls.append((screen_x, screen_y))

                if character == "P":
                    player.goto(screen_x, screen_y)

                if character == "T":
                    treasures.append(Treasure(screen_x, screen_y))

                if character == "E":
                    enemies.append(Enemy(screen_x, screen_y))


# Create class instances
pen = Pen()
player = Player()

# Create wall coordinates
walls = []

# Set up the level
setup_maze(level[1])
print(walls)

# Keyboard Binding
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, " Up")
turtle.onkey(player.go_down, "Down")

# Turn off scr updates
wn.tracer(0)

# Start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

# Main game loop
while True:

    # Iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)
    # Iterate through enemy list to see if the player collides
    for enemy in enemies:
        if player.is_collision(enemy):
            print("Player Dies!")

            # Loop for door
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    # Fill the screen with black
                    screen.fill((0, 0, 0))

                    # Draw the door image onto the screen
                    screen.blit(door_image, (100, 200))

                    # Update the display
                    pygame.display.flip()
                # Check for keyboard input to open or close the door
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_o:
                        door.open()
                    if event.key == pygame.K_c:
                        door.close()

                        # Check for collision between player and door
                        if door.check_collision(player_rect):
                            if door.is_open:
                                # Player can pass through the open door
                                print("Player passed through the door")
                            else:
                                # Player cannot pass through the closed door
                                print("Player cannot pass through the closed door")

    # Update scr
    wn.update()
