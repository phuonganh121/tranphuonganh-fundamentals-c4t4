from random import randint 

numb = randint(0,100)

mood = input ("How are you feeling today? ")
if numb < 30:
    print("I'm sad")
elif numb < 60:
    print("I'm Okay")
else:
    print("Oh yeah!")
