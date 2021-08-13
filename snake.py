from turtle import Turtle

class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            new_section = Turtle('square')
            new_section.penup()
            new_section.color('white')
            new_section.setpos((i * -20), 0)
            self.body.append(new_section)

    def add_segment(self):
        self.body
        new_section = Turtle('square')
        new_section.penup()
        new_section.color('white')
        self.body.append(new_section)

    def move(self):
        for section_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[section_num - 1].xcor()
            new_y = self.body[section_num - 1].ycor()
            self.body[section_num].setpos(new_x, new_y)
        self.body[0].forward(20)
