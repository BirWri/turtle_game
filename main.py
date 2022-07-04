from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = True
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [80, 50, 20, -10, -40, -70]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print("You won!")
            else:
                print(f"You lose. The winning color was {winning_color}")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()