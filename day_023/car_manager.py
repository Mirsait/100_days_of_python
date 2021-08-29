from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    """ Control cars """

    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.to_del = []

    def add_car(self, position):
        if random.randint(1, 6) == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.setheading(180)
            car.turtlesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.setposition(position)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
