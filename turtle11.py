from turtle import*
title("art turtle")
bgcolor("blue")
speed(0)
pensize(5)
for i in range(11):
    color("white")
    left(60)
    circle(-18,200)
    color("white","sky blue")
    r=120
    for j in range(12):
        begin_fill()
        circle(r-12*j,1500)
        end_fill()
    left(180)
    penup()
    goto(0,0)
    pendown()
    hideturtle()

done()
    
