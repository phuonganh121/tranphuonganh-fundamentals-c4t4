from random import randint 

numb = randint(0,100)

print (numb)

count = 0 

loop = True

while loop: 
    guess = int(input("Guess my number (0-100)? "))
    if guess == numb:
        print ("Bingo")
        break
    elif guess > numb:
        print ("Too large")
    else:
        print ("Too small")
    count += 1
    if count == 7:
        print ("You lose")
        break  

