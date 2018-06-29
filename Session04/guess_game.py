print("Think of a number (0-100), then press Enter")
input()

print("""
All you have to do is answer my question
'c' if my guess is correct
's' if my guess is smaller than your number
'l' if my guess is larger than your number
""") 

low = 0
high = 100

guessing = True
while guessing:
    mid = (low+high)//2
    guess = input("Is {0} your number? ".format(mid)).lower() 
    if guess == "c":
        print("I knew it!")
        guessing = False
    elif guess == "s":
        low = mid
    elif guess == "l":
        high = mid 
    else:
        guessing = False 


    