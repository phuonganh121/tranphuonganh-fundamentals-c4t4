from turtle import *

speed (-1)
shape ("turtle")


left (90)
forward (210)
right (90)
for i in range (40):
    for _ in range (2):
        forward (210 - i*5)
        right (90)



mainloop ()