from turtle import *
print("giorgi abuladze")

#we want to pant a house

#step 1:     draw a square
speed(5)
width(7)
color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing a door

forward (70)
begin_fill()
color("yellow")
left(90)
forward(120)      #height of the door
right(90)
forward(60)       #width of the door
right(90)
forward (120)      #height of the door
end_fill()
#
penup()
goto(200, 200)
pendown()
#
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#windows1 left

penup()
goto(0, 170)
pendown()
color ("silver")

begin_fill()
right(240)
forward(50)
right(90)
forward(80)
right(90)
forward(50)
end_fill()

#windows2 right

penup()
goto(200, 170)
begin_fill()
pendown()
forward(50)
left(90)
forward(80)
left(90)
forward(50)
end_fill()
#

exitonclick()


