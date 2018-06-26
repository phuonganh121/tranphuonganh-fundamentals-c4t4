from turtle import *

speed (-1)

for i in range (3,8):
    if i == 3: color ("red")
    if i == 4: color ("blue")
    if i == 5: color ("brown")
    if i == 6: color ("yellow")
    if i == 7: color ("gray")
    for _ in range (i):
        forward (100)
        left (360/i)
    

mainloop ()