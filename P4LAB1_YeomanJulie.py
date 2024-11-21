import turtle

# Create and set up the turtle
t = turtle.Turtle()
t.pensize(3)

# Draw a square using a for loop
for i in range(4):
    t.forward(100)  # Move forward 100 units
    t.right(90)     # Turn right 90 degrees

# Move the turtle to a new position for the triangle
t.penup()          # Lift the pen up
t.goto(50, 50)     # Move to new position
t.pendown()        # Put the pen down

# Draw a triangle using a for loop
for i in range(3):
    t.forward(100)  # Move forward 100 units
    t.left(120)     # Turn left 120 degrees

# Keep the window open
turtle.done()
