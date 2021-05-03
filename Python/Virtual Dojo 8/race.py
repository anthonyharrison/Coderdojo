#!/bin/python3

from turtle import *
from random import randint

LINESIZE = 200
GAP = 10
FINISHLINE= 145
STARTLINE = -160

colours = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
shapes = ['turtle', 'square', 'circle', 'triangle']

def create_turtle(colour, shape, number):
  t = Turtle()
  t.color(colour)
  t.shape(shape)
  t.penup()
  t.goto(STARTLINE, 120 - number * 25)
  t.pendown()
  return t

def draw_course():
  speed(0)
  penup()
  goto (STARTLINE + 20, 140)
  for step in range(15):
    write(step+1, align="center")
    right(90)
    forward (GAP)
    # No dash, just single forward(LINESIZE)
    for dash in range (10):
      pendown()
      forward (10)
      penup()
      forward (10)
    backward(LINESIZE + GAP)
    left(90)
    forward(20)

num_turtles = int(input("How many turtles?"))
draw_course()
turtles = []
for i in range(num_turtles):
  turtles.append(create_turtle(colours[i % 6], shapes [i % 4], i))

finished = False
for turn in range(100):
  if not finished:
    for i in range(num_turtles):
      # Constant movement or random
      if i % 2 == 0:
        turtles[i].forward(3)
      else:
        turtles[i].forward(randint(1,5))
      if turtles[i].pos()[0] > FINISHLINE:
        print("Turtle", i+1,"has won!")
        # Do a twirl!
        for count in range(10):
          turtles[i].right(36)
        finished = True
        # And stop everyone moving
        break
