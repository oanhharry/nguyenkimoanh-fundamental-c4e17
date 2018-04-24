px = 1
py = 1
bx = 2
by = 2

loop= True
while loop:
    for y in range(4):
        for x in range(4):
            if x==px and y==py:
                print("P ", end=" ")
            elif x==bx and y==by:
                print("B ", end=" ")
            elif x==1 and y==3:
                print("G ", end=" ")
            else:
                print("_ ", end=" ")
        print()
    #input command
    go= input("Command a/d/w/s: ").upper()
    next_px = px
    next_py = py

    if go == "A":
        next_px -=1
        # if next_px <0:
        #     pass
        # else:
        #     px = next_px
    elif go== "D":
        next_px +=1
    elif go== "W":
        next_py -=1
    else:
        next_py +=1

    if 0 <= next_px <4:
        px = next_px
    if 0<= next_py <4:
        py = next_py
