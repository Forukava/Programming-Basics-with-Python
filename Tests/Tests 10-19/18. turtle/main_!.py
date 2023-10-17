
import random
from turtle import *


tim = Turtle()
directions = [0, 90, 180, 270]
colors = ['red', 'orange', 'yellow', 'green', 'blue',
  'purple', 'pink', 'brown', 'gray', 'gold', 'cyan', 'Gainsboro', 'gray',
  'dimgray', 'LightSlateGray','AliceBlue', 'LimeGreen', 'DarkKhaki', 'Khaki']
tim.pensize(20)
tim.speed("fastest")

for _ in range(500):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()


