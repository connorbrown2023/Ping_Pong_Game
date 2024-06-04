from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")

L_paddle = Paddle(-350, 0)
R_paddle = Paddle(350, 0)

pong = Ball()



screen.listen()

screen.onkey(R_paddle.go_up, "Up")
screen.onkey(R_paddle.go_down, "Down")

screen.onkey(L_paddle.go_up, "w")
screen.onkey(L_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    pong.move()

    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y()

    if pong.distance(R_paddle) < 50 and pong.xcor() > 320 or pong.distance(L_paddle) < 50 and pong.xcor() > -320:
        pong.bounce_x()



screen.exitonclick()
