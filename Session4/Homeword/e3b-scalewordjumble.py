list_word = ["oanh","phone","book","lamp"]
from random import choice

loop = True
while loop:
    word = choice(list_word)
    charactor = list(word)
    list_word.remove(word)

    #lay random cac ky tu trong tu
    from random import choice
    loop1 = True
    while loop1:
        c = choice(charactor)
        print(c, end=" ")
        charactor.remove(c)
        if charactor ==[]:
            loop1 = False
    #cho user doan tu
    loop2 = True
    while loop2:
        guess = input("Your answer: ")
        guess = guess.lower()
        if guess==word:
            print("Hura")
            loop2 = False
        else:
            print(":(")
    if list_word==[]:
        loop2 = False
        print("List word is empty")
