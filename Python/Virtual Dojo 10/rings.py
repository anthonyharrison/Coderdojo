#!/bin/python3

from processing import *

# Global variables
factor = 0 
inc = 1

def setup():
  size(750, 500)
  frameRate(10)

def draw():
  global factor, inc

  background(255)
  red = color(255, 0, 0)
  green = color(0, 255, 0)
  blue = color(0, 0, 255)
  yellow = color(255, 255, 0)
  black = color(0, 0, 0)
  ring_size = 175
  
  colours = [blue, black, red, yellow, green]
  
  # Olympic rings
  positions = [ [-150,0], [200, 0], [200,0], [-300, 100], [200,0]]
  # Neighbouring rings
  #positions = [ [-200,0], [100, 0], [100,0], [100, 0], [100,0]]
  
  # Calculate scaling
  yscale = (10 - factor)/10 
  xscale = 1.0 
 
  index = 0
  for colour in colours:
    translate(positions[index][0], positions[index][1])
    drawCircle(colour, xscale, yscale, ring_size)
    index += 1
  # Adjust scaling
  factor = factor + inc
  if factor >= 10:
    inc = -inc
  elif factor <= 0:
    inc = -inc

def drawCircle(colour, x, y, radius):
  # Draw circle
  # x, y = 1 => a circle
  # x or y < 1 will create elipse
  # x = y and < 1 will scale circle
  stroke(colour)
  # Line thickness proportion to x scaling
  strokeWeight(10 * x)
  noFill()
  arc(width/2, height/2, radius * x, radius * y, 0, 2 * PI)
  
run()