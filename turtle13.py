from random import randint
from turtle import Screen, Turtle
COLORS = ['red', 'yellow', 'blue', 'green', 'orange', 'purple']
turtles = []
screen = Screen()
screen.setup(height=500, width=400)
x = -230
y = 150
for color in COLORS:
    turtle = Turtle(shape='turtle')
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)
    y -= 50
    turtles.append(turtle)
game_running = False
user_input = screen.textinput(title="Make your bet", prompt="Which turtle is going to win the race?..")
if user_input:
    game_running = True
while game_running:
    for turtle in turtles:
        random_num = randint(0, 10)
        turtle.forward(random_num)
        if turtle.xcor() >= 230:
            game_running = False
            print(f"The Turtle with color {turtle.pencolor()} won. ", end='')
            if turtle.pencolor() == user_input:
                print("You Won!")
            else:
                print("You Lost!")
            break
screen.exitonclick()
