number = list(range(1,10))
print(*number)

for j in range(8):
    for i in range(9):
        number[i]=number[i]+i+1
    print(*number)
