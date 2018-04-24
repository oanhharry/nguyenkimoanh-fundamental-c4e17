from turtle import *
color("red")
right(150)
for i in range(4):
    for i in range(2):
        for i in range(1,3):
            forward(100)
            right(60*i)
    left(90)

mainloop()
