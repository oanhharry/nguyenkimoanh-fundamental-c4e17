
favs=[input("Your favorites are: ")]
print("Here your favorite:", *favs)
add=input("Name one thing you want to add? ")
favs.append(add)
print("Tada:",*favs, sep=", ")
