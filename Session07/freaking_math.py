from random import * 
import eval


x = randint(1,10)
y = randint (1,10)
operations = ["+", "-", "*", "/"]
op = choice(operations)
res = eval.calc(x, y, op)

error = [-1]*15 + [0]*70 + [1]*15
a = choice(error)

display_res = res + a

print ("{0} {1} {2} = {3}".format(x, op, y, display_res))

guess = input("(Y/N)?").lower()

if a == 0:
    if guess == "y":
        print ("Yay")
    else: 
        print ("Wrong")
else: 
    if guess == "y":
        print ("Wrong")
    else: 
        print ("Yay")