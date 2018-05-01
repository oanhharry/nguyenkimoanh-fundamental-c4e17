from turtle import *
for j in range(3,8):
    if j%2!=0:
        color("blue")
    else:
        color("red")
    for i in range(j):
        forward(100)
        left(int(360/j))
mainloop()
