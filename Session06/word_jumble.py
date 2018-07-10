from random import choice

words = ["champion", "hello", "bonjour", "ciao"]
rand_word= choice(words)

chars = list(rand_word)

while len(chars) > 0:
    rand_char = choice(chars)

    print((rand_char), end=" ")

    chars.remove(rand_char)

print ()

guessing = True
while guessing: 
    ans = input ("Your answer: ").lower()
    if ans == rand_word:
        print ("Hura")
        break
    else:
        print (":(")
