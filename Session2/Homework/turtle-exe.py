from turtle import *

left(150)
shape()
color("red")
for x in range(4):
    for i in [1,2,1]:
        forward(100)
        left(i*60)

    forward(100)
    left(30)

mainloop()
