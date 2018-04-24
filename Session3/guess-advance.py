from random import randint

n = randint(0,100)
print("Now think of a number from 0 to 100, then press Enter")
print("All you have to do is to answer my guess")

loop = True
while loop:
    answer = input("Is n your number? ")
    if answer == "s":
        print("small than i think")
    elif answer == "l":
        print("large than I think")
    else:
        print("Bing go")
        loop =  False
