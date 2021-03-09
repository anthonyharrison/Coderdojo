#!/bin/python3

import turtle
import random

def square(t, size):
  t.begin_fill()
  for i in range(4):
    t.forward(size)
    t.right(90)
  t.end_fill()

def parallelogram (t, size):
  t.begin_fill()
  for i in range(2):
    t.forward(size)
    t.right(60)
    t.forward(size)
    t.right(120)
  t.end_fill()

def flower (t, leaves, size, colour):
  for i in range(leaves):
    t.color(colour)
    parallelogram (t, size)
    t.right(360/leaves)

def flower2 (t, leaves, size, colour):
  for i in range(leaves):
    t.color(colour)
    square (t, size)
    t.right(360/leaves)

def branch(t):
  for i in range(3):
    for j in range(3):
      t.forward(30)
      t.backward(30)
      t.right(45)
    t.left(90)
    t.backward(30)
    t.left(45)
  t.right(90)
  t.forward(90)

def circle (t, size, colour):
  t.home()
  t.color(colour)
  #t.fillcolor(colour)
  t.right(90)
  t.forward(size)
  t.right(270)
  t.begin_fill()
  t.circle(size)
  t.end_fill()

# Main
colours = ["red", "orange", "yellow", "green", "blue", "purple", "white", ]
    
elsa = turtle.Turtle()
turtle.Screen().bgcolor("grey")
elsa.speed(500)

flower2(elsa, 12, 100, random.choice(colours))
elsa.right(45)
flower(elsa, 16, 50, random.choice(colours))

elsa.home()
# Snowflake
elsa.penup()
elsa.forward(90)
elsa.left(45)
elsa.pendown()
elsa.color(random.choice(colours))
for i in range(8):
  branch(elsa)
  elsa.left(45)

circle(elsa, 40, "yellow")
circle(elsa, 25, "green")
