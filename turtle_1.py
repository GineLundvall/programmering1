from turtle import *       

speed(10)
forward(20)     #Uppgift 1
write(0)
forward(20)
write(1)
forward(20)
write(2)
forward(20)
write(3)
forward(20)
write(4)
forward(20)
write(5)
forward(20)
left(90)

for step in range(5):        #Uppgift 2 
    forward(20)
    write(step)
    right(45)
    

for step in range(6):       #Uppgift 3
    forward(20)
    write(step)


goto(-140,140)      #Uppgift 4

for step in range(6):
    forward(20)
    write(step)

penup()         #Uppgift 5
goto(-100,100)

for step in range(6):
    forward(20)
    write(step)

for step in range(6):       #Uppgift 6
    write(step)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

right(45)
penup()
goto(300,-260)
pendown()
for step in range(31):       #Extra/challenge uppgift
    write(step)
    right(90)
    forward(10)
    pendown()
    forward(550)
    penup()
    backward(560)
    left(90)
    forward(20)


 

exitonclick()







