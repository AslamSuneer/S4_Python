import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle instance
artist = turtle.Turtle()

# Set the speed and thickness of the pen
artist.speed(10)
artist.pensize(2)

# Function to draw a square
def draw_square(size, color):
    artist.color(color)
    artist.begin_fill()
    for _ in range(4):
        artist.forward(size)
        artist.right(90)
    artist.end_fill()

# Function to draw a circle
def draw_circle(radius, color):
    artist.color(color)
    artist.begin_fill()
    artist.circle(radius)
    artist.end_fill()

# Function to draw the design
def draw_design():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for i in range(36):
        draw_square(100, colors[i % 6])
        artist.right(10)
    for i in range(18):
        draw_circle(100, colors[i % 6])
        artist.right(20)

# Move the turtle to the starting position
artist.penup()
artist.goto(-150, -150)
artist.pendown()

# Draw the design
draw_design()

# Hide the turtle and display the result
artist.hideturtle()

# Keep the window open until closed by user
turtle.done()
