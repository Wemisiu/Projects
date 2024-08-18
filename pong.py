import turtle

# Set up the screen
win = turtle.Screen()
win.title("Pong by You")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A (left)
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B (right)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = -3

# Scores
score_a = 0
score_b = 0

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Pause state
paused = False

# Function to toggle pause
def toggle_pause():
    global paused
    paused = not paused

# Functions to move paddles
def paddle_a_up():
    if not paused:
        y = paddle_a.ycor()
        if y < 250:
            y += 20
        paddle_a.sety(y)

def paddle_a_down():
    if not paused:
        y = paddle_a.ycor()
        if y > -240:
            y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    if not paused:
        y = paddle_b.ycor()
        if y < 250:
            y += 20
        paddle_b.sety(y)

def paddle_b_down():
    if not paused:
        y = paddle_b.ycor()
        if y > -240:
            y -= 20
        paddle_b.sety(y)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")
win.onkeypress(toggle_pause, "p")  # Bind 'p' key to pause/unpause

# Function to update score display
def update_score():
    pen.clear()
    pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

# Main game loop
while True:
    win.update()

    if not paused:
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border collision (top and bottom)
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # Left and right border collision (reset ball position)
        if ball.xcor() > 390:
            score_a += 1
            update_score()
            ball.goto(0, 0)
            ball.dx *= -1

        if ball.xcor() < -390:
            score_b += 1
            update_score()
            ball.goto(0, 0)
            ball.dx *= -1

        # Paddle collision detection
        if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
            ball.setx(340)
            ball.dx *= -1

        if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
            ball.setx(-340)
            ball.dx *= -1
