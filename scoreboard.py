from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,270)
        self.color('white')
        self.hideturtle()
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 25, 'normal'))

    def add_point(self):
        self.score += 1
        self.undo()
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 25, 'normal'))