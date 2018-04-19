numbers = [1,6,8,1,2,1,5,6]
count = 0
n = int(input("Enter a number: "))
for i in numbers:
    if i == n:
        count += 1
print(count)
