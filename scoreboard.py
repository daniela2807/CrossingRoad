from turtle import Turtle

FONT = ("Courier", 14, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.level = 1
        super().__init__()
        self.penup()
        #self.high_score = 0
        self.hideturtle()
        self.sety(260)
        #self.write(f"Level = {self.level}", True, align="right",font = FONT)

    def updatescore(self):
        self.clear()
        self.write(f"Level = {self.level} , High score: {self.high_score}", True, align="right", font=FONT)

    def reset(self):
        if self.high_score < self.level:
            self.high_score = self.level
        with open("data.txt",mode="w") as file:
            file.write(str(self.high_score))
        self.level=1
        self.updatescore()

    def incrase_score(self):
        self.level += 1
        self.updatescore()

    """def gameover(self):
        self.goto(0,0)
        self.clear()
        self.write(f"GAME OVER", True, align="center", font=FONT)"""

