
text = input("Enter the data: ").lower()

letter_count = {}

for letter in text:
    if(letter!=" "):
        letter_count[letter] = letter_count.get(letter, 0) + 1

letter_count_array= list(letter_count.items())
keys = list(letter_count.keys())
keys.sort()

for k in keys:
    print(k,":", letter_count[k])
