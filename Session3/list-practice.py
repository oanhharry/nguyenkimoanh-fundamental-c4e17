menu=["pho","com rang", "my xao"]
print(*menu)
menu.append("hu tieu")
print("After append")
print(*menu)

# for i in range (len(menu)):
#     print(menu[i])
#
# #foreach
# for item in menu:
#     print(item)

#for enum
name = "Oanh"
age = 25
status = "Single"
address =  "Hoang van thai"

#str format
message = "{0},{1} tuoi, tinh trang quan he: {2}, song o: {3}".format(name, age, status, address)
print(message)
# print(name+ ","+ str(age)+ "tuoi", status + address)

for i,item in enumerate(menu):
    message = "{0}. {1}".format(i+1, item)
    print(i+1,".",item)
