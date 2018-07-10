from turtle import * 

speed (5)

for i in range (4):
    forward (200)
    left (90)

penup ()
forward (30)
pendown ()

color ("blue")
begin_fill ()
for j in range (2):
    forward (50)
    left (90)
    forward (100)
    left (90)
end_fill()

penup ()
forward (170)
left (90)
forward (170)
left (90)
forward (20)


color ("yellow")
begin_fill ()
for x in range (4):
    forward (50)
    left (90)
end_fill ()

right (180)
forward (20)
left (90)
forward (30)

color ("red")
begin_fill ()
left (60)
forward (115)
left (60)
forward (115)
left (150)
forward (200)
end_fill()




mainloop ()