loop=True
wrong_count = 0
while loop:

    username = input("username? ")
    password = input("Password? ")
    if username != 'c4e':
        print("No such user")
        wrong_count += 1
    elif password != 'codethechange':
        print("wrong password")
        wrong_count += 1
    else:
        print("Welcome!!!")
        loop =  False
    if wrong_count>3:
        loop =  False
