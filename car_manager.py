import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []


    def add_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_wid=1,stretch_len=2)
        car.color(random.choice(COLORS))
        car.goto(300, random.randint(-260, 260))
        self.cars.append(car)

    def movecar(self,level):
        print(level)
        for car in self.cars:
            car.setx(car.xcor()-(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (level-1))))

