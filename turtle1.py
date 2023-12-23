import turtle as tu
import colorsys
tu.Screen().bgcolor("black")
t=tu.Pen()
t.speed(0.01)
h=0.3
t.ht()
for i in range(180):
    c=colorsys.hsv_to_rgb(h,1,1)
    t.color(c)
    t.begin_fill()
    t.left(9)
    t.forward(i*0.3)
    t.right(45)
    t.backward(i*0.3)
    t.left(19)
    t.forward(i*0.5)
    t.end_fill()
    h+=0.005
tu.done()