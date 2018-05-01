# person= ["Quan",22, "Single","Hanoi", 2, 11]
# print(person)

#dictionary
# person = {
#     "name": "Quan"
# }
#
# print(person)

person = {
"name": "Quan",
"age": 40,
}
# print(person)
#truy cap dictionary
# print(person["age"])
# person["age"]= 22
# print(person)
#
# if "home" in person:
#     print(person["home"])
# else:
#     print("'home'is not exist")

#update
# person["age"]= 22
# print(person)
#
# #create
# person["home"]= "Hanoi"
# print(person)
#
# #delete
# del person["name"]
# print(person)
#
# print(*person.key())
# print(*person.value())

for key, value in person.items():
    print(key,":", value)
