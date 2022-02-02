from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pk's Pong Game")
screen.tracer(0)  # This is to turn off the animation but when we do this, we have to manually update the screen

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.go_up,"Up")  # When passing functions as arguments don't use parenthesis
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"z")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # The shorter the sleep speed is the faster is the movement
    screen.update()  # This is associated with the tracer function we have to update the screen manually
    ball.move()

    # Detecting the collisions with respect to walls
    if ball.ycor() > 280 or ball.ycor() < -280:  # As our screen height is 600 we take suitable values to make it bounce
        # The ball needs to bounce
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if R paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if L paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()