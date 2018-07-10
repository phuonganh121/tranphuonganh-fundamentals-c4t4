string = input("Enter a string: ").lower()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

letter_count = {}

for character in string:
    if character in alphabet: 
        if character in letter_count:
            letter_count[character] = letter_count[character] + 1
        else:
            letter_count[character] = 1

keys = letter_count.keys()
for character in keys:
    print(character, letter_count[character])
