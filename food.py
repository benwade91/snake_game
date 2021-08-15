from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.color('green')
        self.speed('fastest')
        self.goto(random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)

    def refresh(self):
        self.goto(random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)