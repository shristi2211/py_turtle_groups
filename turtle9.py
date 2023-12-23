from turtle import*

title("Python Turtle Art")
bgcolor("black")
speed(0)
pensize(3)

for i in range(9):
    color("yellow") 
    left(60)
    circle(-18, 200)
    color("yellow", "orange")
    r = 100
    for j in range(12):
        begin_fill()
        circle(r-10*j, 1000)
        end_fill()  
    left(180)  
    penup()
    goto(0,0)
    pendown()
    hideturtle()

done()
