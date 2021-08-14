from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_on = True

while game_on:
    screen.update()
    time.sleep(0.15)

    snake.move()

    if snake.body[0].distance(food) < 10:
        snake.add_segment()
        food.refresh()





screen.exitonclick()