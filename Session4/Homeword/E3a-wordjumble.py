word = "table"
charactor = list(word)

#lay random cac ky tu trong tu
from random import choice
#option1:
# for i in range (int(len(charactor))):
#     c = choice(charactor)
#     print(c, end=" ")
#     charactor.remove(c)
#option2
loop = True
while loop:
    c = choice(charactor)
    print(c, end=" ")
    charactor.remove(c)
    if charactor ==[]:
        loop = False
#cho user doan tu
loop = True
while loop:
    guess = input("Your answer: ")
    guess = guess.lower()
    if guess==word:
        print("Hura")
        loop = False
    else:
        print(":(")
