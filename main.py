from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('pong')

screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, 'z')
screen.onkey(l_paddle.go_down, 's')

screen.onkey(r_paddle.go_up, 'p')
screen.onkey(r_paddle.go_down, 'm')


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:

        ball.bounce_x()

    # right detection
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    # left detection
    if ball.xcor() < -390:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
