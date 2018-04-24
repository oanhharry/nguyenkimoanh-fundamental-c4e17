dict = {
    "ayo":"anh yeu",
    "any": "anh nguoi yeu",
    "4u": "for you",
}

while True:
    code = input("Enter your code: ")
    if code in dict:
        print(dict[code])
    else:
        print("Not exsit")
        n = input("Do you want to ad code? ").upper()
        if n =="Y":
            choice = input("Meaning: ")
            dict[code]= choice
            print(dict[code])
        else:
            print("Not found")
