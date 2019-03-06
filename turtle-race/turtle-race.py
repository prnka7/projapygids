#!/bin/python3
from turtle import *
from random import randint
penup()
goto(-140,140)

speed(30)
for step in range(15):
  write(step,align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
  
ada=Turtle()
ada.color('red')
ada.shape('turtle')

bob=Turtle()
bob.color('blue')
bob.shape('turtle')

cart=Turtle()
cart.color('green')
cart.shape('turtle')

dope=Turtle()
dope.color('yellow')
dope.shape('turtle')

ada.penup()
ada.goto(-160,120)
  
bob.penup()
bob.goto(-160,80)

cart.penup()
cart.goto(-160,40)

dope.penup()
dope.goto(-160,00)

ada.pendown()
bob.pendown()
cart.pendown()
dope.pendown()

for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  cart.forward(randint(1,5))
  dope.forward(randint(1,5))