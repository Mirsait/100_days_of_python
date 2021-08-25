import turtle as t
import random
from typing import Tuple

screen = t.Screen()
screen.bgcolor("darkgray")
WIDTH = 600
t.setup(width=WIDTH, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles_list = []
choice = screen.textinput(title="the turtle race",
                          prompt="Enter a color of your player: ")

tim = t.Turtle()
tim.hideturtle()
tim.speed(10)
tim.shape('square')
tim.turtlesize(0.5)


def dashed_xline(tim, y):
    tim.penup()
    start_x = - WIDTH / 2
    tim.setpos(start_x, y)
    while start_x < WIDTH/2:
        tim.pendown()
        tim.forward(15)
        tim.penup()
        tim.forward(15)
        start_x += 30


positions_y = [30 * i - 75 for i in range(7)]


def finish_line():
    tim.penup()
    start_y = positions_y[6] - 15
    tim.setpos(WIDTH/2 - 10, start_y)
    tim.right(90)
    while start_y > positions_y[0]:
        tim.stamp()
        tim.right(90)
        tim.forward(10)
        tim.left(90)
        tim.forward(10)
        tim.stamp()
        tim.left(90)
        tim.forward(10)
        tim.right(90)
        tim.forward(10)
        tim.stamp()
        start_y -= 20


for pos in positions_y:
    dashed_xline(tim, pos - 15)

finish_line()

for i in range(6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-WIDTH/2+20, y=positions_y[i])
    turtles_list.append(new_turtle)


is_race_on = False
if choice:
    is_race_on = True

while is_race_on:
    for current_turtle in turtles_list:
        if current_turtle.xcor() > WIDTH / 2:
            if current_turtle.pencolor() == choice:
                print(f"You won. Your {choice} turtle came first.")
            else:
                win_color = current_turtle.pencolor()
                print(f"The winner is {win_color} turtle")
            is_race_on = False
        random_distance = random.randint(0, 10)
        current_turtle.forward(random_distance)

t.exitonclick()
