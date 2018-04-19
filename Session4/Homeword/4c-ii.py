n=int(input("Enter a number: "))
number = list(range(1,n+1))
print(*number)

for j in range(n-1):
    for i in range(n):
        number[i]=number[i]+i+1
    print(*number)
