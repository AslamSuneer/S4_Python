import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle instance
artist = turtle.Turtle()

# Set the speed and thickness of the pen
artist.speed(0)  # fastest speed
artist.pensize(2)

# Function to draw a rectangle
def draw_rectangle(x, y, width, height, color):
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.color(color)
    artist.begin_fill()
    for _ in range(2):
        artist.forward(width)
        artist.right(90)
        artist.forward(height)
        artist.right(90)
    artist.end_fill()

# Function to draw a line
def draw_line(x1, y1, x2, y2, color):
    artist.penup()
    artist.goto(x1, y1)
    artist.pendown()
    artist.color(color)
    artist.goto(x2, y2)

# Draw the classroom layout
def draw_classroom():
    # Drawing the walls
    draw_rectangle(-300, -200, 600, 400, "lightblue")

    # Seating arrangement
    draw_rectangle(-250, -150, 500, 300, "white")

    # Podium
    draw_rectangle(-200, 50, 200, 50, "brown")

    # Smartboard
    draw_rectangle(50, 50, 150, 100, "green")

    # Projector
    draw_rectangle(200, 150, 50, 50, "black")

    # Camera
    draw_rectangle(250, 150, 25, 25, "red")

    # Teacher position
    draw_rectangle(-200, 100, 50, 50, "yellow")

    # Cable layout
    draw_line(-200, 150, 50, 150, "gray")  # From podium to smartboard
    draw_line(50, 150, 200, 150, "gray")   # From smartboard to projector
    draw_line(200, 150, 250, 150, "gray")  # From projector to camera

# Draw the classroom layout
draw_classroom()

# Hide the turtle and display the result
artist.hideturtle()

# Keep the window open until closed by user
turtle.done()
