from turtle import *

speed (-1)


for i in range (4,9):
    for _ in range (i):
        if _ % 2 == 1: 
            color ("red")
        else: 
            color ("blue")
        forward (100)
        left (360/i)
    

mainloop ()