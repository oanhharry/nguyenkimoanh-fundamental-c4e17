shop=["T-shirt","Sweater"]
n=input("Welcome to our shop, What do you want (C, R, U, D)? ")

if n=="R":
    print(shop)
elif n=="C":
    new=input("Enter new item: ")
    shop.append(new)
    print("Our item:",*shop)
elif n=="U":
    update=int(input("Update position? "))-1
    shop[update]=input("New item? ")
    print("Our item:", *shop)
else:
    delete=int(input("Delete position? "))-1
    del shop[delete]
    print("Our items: ",*shop)
