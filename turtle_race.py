import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)

game_start = False
bet_on = t.textinput(title= "Make your bet",prompt="Who do you bet on? Red, Green, Yellow, Orange or Purple: ")

if bet_on:
    game_start = True


colors = ["red", "orange", "yellow", "green", "purple"]
random.shuffle(colors)
y_position = [-150, -75, 0, 75, 150]
turtle_list = []

for i in range(len(colors)):
    turtle = t.Turtle(shape="turtle")
    turtle.penup() 
    turtle.color(colors[i])
    turtle.goto(-230, y_position[i])
    turtle_list.append(turtle)

while game_start:
    
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            game_start = False
            winner = turtle.pencolor()
            if winner == bet_on:
                print(f"You have won! The {winner} turtle is the winner!")
            else:
                print(f"Sorry you have lost! The {winner} turtle is the winner!")
            break
        distance = random.randint(1,10)
        turtle.forward(distance)



screen.exitonclick()