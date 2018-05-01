names=["book","film","code","phone"]
print(*names)
n=int(input("Position you want to update: "))
names[n]=input("Your replacing: ")
print(*names)
