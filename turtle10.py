import  turtle 
myturtle = turtle.Turtle() 
window = turtle.setup(width=500,height=600)
screen = turtle.Screen()
#to start from center of screen
screen.setworldcoordinates(-250,-250,screen.window_width() -1,screen.window_height() - 1)
colorlist = ["purple","red","orange","blue","green",'yellow'] 

def rotate():

    myturtle.clear()

    for i in range(36):       
        for _ in range(3):
            myturtle.circle(100,200)
            myturtle.color(colorlist[i%5])
            myturtle.left(99)
        myturtle.left(10)
    turtle.update()
    myturtle.left(1)
    turtle.ontimer(rotate, 60)
myturtle.left(20)
turtle.tracer(False)
rotate()
turtle.exitonclick()
