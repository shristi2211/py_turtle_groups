import turtle
t = turtle.Turtle()
list1 = ["purple","red","green"]
turtle.bgcolor("black") 
for i in range(200):
    t.color(list1[i%3])
    t.pensize(3)
    t.forward(i)
    t.left(59)
turtle.done()
