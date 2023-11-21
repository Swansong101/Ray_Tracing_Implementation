import time
import turtle
import math
import random


# Function to display the splash screen with a countdown
def display_splash_screen():
    splash_screen = turtle.Screen()
    splash_screen.bgcolor("black")
    splash_screen.title("Maze Game Splash Screen")
    splash_screen.setup(700, 700)

    # Create a turtle for the splash screen
    splash_pen = turtle.Turtle()
    splash_pen.speed(0)
    splash_pen.color("green")
    splash_pen.penup()
    splash_pen.hideturtle()

    # Display the splash screen text and maze image
    splash_pen.goto(0, 100)
    splash_pen.write("Glow in the Dark Maze Game", align="center", font=("Courier", 24, "normal"))

    # Add maze image at the center
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


# Call the function to display the splash screen
display_splash_screen()

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Glow In The Dark")
wn.setup(700,700)
wn.tracer(0)

#Register shapes
images = ["player_right.gif","player_right.gif","treasure.gif","wall.gif",
          "pennywise - v2.gif"]
for image in images:
    turtle.register_shape(image)

# Declare reflectors as a global variable
reflectors = []

#Create path
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
        #Calculate the space to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        #Check if the space has a wall
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
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
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
        self.direction = random.choice(["up","down","left","right"])

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

            #Check if player is close
            #If so, go in that direction
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        #Calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        else:
            #Choose a different direction
            self.direction = random.choice(["up","down","left","right"])
        #Set timer to move to next time
        turtle.ontimer(self.move, t=random.randint(100,300))

    def is_close(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()



#Create levels list
level = [""]

#Define first level
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

#Add a treasure list
treasures = []
#Add enemies list
enemies = []
#Add maze to mazes list
level.append(level_1)

#Create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Get the character at each x,y coordinate
            character = level[y][x]
            #Calculate the screen x,y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            #Check if it an X
            if character =="X":
                pen.goto(screen_x, screen_y)
                pen.shape("wall.gif")
                pen.stamp()
                #Add coordinates to wall list
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



#Create class instances
pen = Pen()
player = Player()

#Create wall coordinates
walls = []

#Set up the level
setup_maze(level[1])
print (walls)

#Keyboard Binding
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up," Up")
turtle.onkey(player.go_down,"Down")

#Turn off screen updates
wn.tracer(0)

#Start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)


#Main game loop
while True:
    #Iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print ("Player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)
    #Iterate through enemy list to see if the player collides
    for enemy in enemies:
        if player.is_collision(enemy):
            print("Player Dies!")

    #Update screen
    wn.update()