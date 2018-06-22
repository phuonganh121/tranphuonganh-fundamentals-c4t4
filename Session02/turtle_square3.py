from turtle import * 

for i in range (20):
    for _ in range (4):
        forward (50+i*10)
        left (90)
    right (40)
    forward (10)

mainloop ()