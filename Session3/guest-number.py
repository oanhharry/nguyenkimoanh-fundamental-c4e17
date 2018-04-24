from random import randint
n = randint(1,100)
wrong_count = 0

loop = True
while loop:
    m = int(input("Gues my number: "))
    if m>n:
        print("A little too large")
        wrong_count +=1
    elif m<n:
        print("Too small")
        wrong_count +=1
    else:
        print("Bing go")
        loop = False
    if wrong_count >8:
        loop = False
