from turtle import *
speed(0)
colours = ["red","blue","brown",]
color_n=len(colours)

for j in range(3,12):
    color(colours[j%color_n])
    for i in range(j):
        forward(100)
        left(int(360/j))
mainloop()
