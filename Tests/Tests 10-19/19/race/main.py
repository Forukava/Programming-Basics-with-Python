import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
position_y = [120, 70, 20, -30, -80, -130]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=position_y[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 222:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You've won! The {wining_color} turtle is the winner!")
            else:
                print(f"You've lost! The {wining_color} turtle is the winner!")

        rand_distance = random.randint(0, 5)
        turtle.forward(rand_distance)

screen.exitonclick()