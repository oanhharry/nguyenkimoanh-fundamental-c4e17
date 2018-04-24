
m=int(input("Enter a number: "))
n=int(input("Row: "))

for i in range(n):
    for j in range(m):
        if i<=j:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
