for j in range(9):
    for i in range(9):
        if (i+j) %2==0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
