#!/bin/python3

# A python implementaion of Vera Molnar's 25 squares artwork (see https://digitalartmuseum.org/gallery/image/8851.html)
# Inspired by an implementaion written in Processing (see https://openprocessing.org/sketch/209391/)

import turtle

import random
import time

NUMROW=5
NUMCOL=NUMROW
SQUARES=NUMROW*NUMCOL

def square(t, size):
  DELTA = 5
  cur_pos = t.pos()
  # Generate a random offset position
  xinc = random.randrange(-DELTA, DELTA)
  yinc = random.randrange(-DELTA, DELTA)
  t.goto(cur_pos[0]+xinc,cur_pos[1]+yinc)
  t.begin_fill()
  for i in range(4):
    t.forward(size)
    t.right(90)
  t.end_fill()
  t.goto(cur_pos[0],cur_pos[1])
  
colours = ["red", "darkred"]
  
elsa = turtle.Turtle()
turtle.Screen().bgcolor("grey")
elsa.speed(1000)
elsa.hideturtle()

while (True):
  
  elsa.clear()
  cols = [0] * SQUARES
  
  # Randomly choose up to 5 squares to be a different colour
  for i in range(5):
    cols[random.randrange(0,SQUARES)] = 1

  for row in range(NUMROW):
  
    elsa.penup()
    elsa.goto(-200, (row * 80) - 120)
    elsa.pendown()
    for col in range(NUMCOL):
      #elsa.color(random.choice(colours))
      elsa.color(colours[cols[(row * NUMROW) + col]])
      square(elsa, 75)
      elsa.penup()
      elsa.forward(80)
      elsa.pendown()
      
  time.sleep(2)
