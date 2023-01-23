import time
from turtle import Screen
from player import Player
import keyboard
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
level = 1
screen.tracer(0)
player = Player()
score = Scoreboard()
car_manager = CarManager()
game_is_on = True
screen.listen()
screen.onkey(player.moveturtle, "Up")
loop_count = 0
score.updatescore()
while game_is_on:
    loop_count+=1
    if loop_count == 6:
        car_manager.add_car()
        loop_count = 0
    time.sleep(0.1)
    car_manager.movecar(score.level)
    if player.ycor() >= 300:
        score.incrase_score()
        player.detectfinishline()
    for car in car_manager.cars:
        if player.distance(car) < 20:
            score.reset()
            player.detectfinishline()
            #game_is_on = False
    screen.update()

screen.exitonclick()





