import turtle
import time

# Create screen
sc = turtle.Screen()
sc.title("Pong")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# Ball
hit_ball = turtle.Turtle()
hit_ball.speed(4) # Adjusted speed
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# Initialize score
left_player = 0
right_player = 0

# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Player 1 : 0    Player 2 : 0", align="center", font=("Courier", 24, "normal"))

# Functions for paddle movement
def paddle1up():
    y = left_pad.ycor()
    if y < 250: # Limit movement
        y += 20
        left_pad.sety(y)

def paddle1down():
    y = left_pad.ycor()
    if y > -240:
        y -= 20
        left_pad.sety(y)

def paddle2up():
    y = right_pad.ycor()
    if y < 250: # Limit movement
        y += 20
        right_pad.sety(y)

def paddle2down():
    y = right_pad.ycor()
    if y > -240:
        y -= 20
        right_pad.sety(y)

# Keyboard bindings
sc.listen()
sc.onkeypress(paddle1up, "w")  # Changed to 'w'
sc.onkeypress(paddle1down, "s")  # Changed to 's'
sc.onkeypress(paddle2up, "Up")
sc.onkeypress(paddle2down, "Down")

# Main game loop
while True:
    sc.update
    time.sleep(0.01) # Add delay to make game smoother
    
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)
    
    # Checking borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Player 1 : {}    Player 2 : {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Player 1 : {}    Player 2 : {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

    # Paddle ball collision
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and \
            (hit_ball.ycor() < right_pad.ycor() + 50 and hit_ball.ycor() > right_pad.ycor() - 50):
        hit_ball.setx(360)
        hit_ball.dx *= -1

    if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370) and \
            (hit_ball.ycor() < left_pad.ycor() + 50 and hit_ball.ycor() > left_pad.ycor() - 50):
        hit_ball.setx(-360)
        hit_ball.dx *= -1