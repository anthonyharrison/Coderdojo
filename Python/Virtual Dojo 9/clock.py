#!/bin/python3

from processing import *

def setup():
  size(500, 500)
  #background(255)
  #frameRate(1)

def draw():
  background(255)
  red = color(255, 0, 0)
  green = color(0, 255, 0)
  blue = color(0, 0, 255)
  drawCircle(red, second(), 60.0, 400)
  drawCircle(blue, minute(), 60.0, 375)  
  drawCircle(green, hour(), 24.0, 350)  
  drawTime() 

def drawCircle(colour, n, max, radius):
  # Draw partial circle
  end =(n/max)*2*PI-PI/2
  stroke(colour)
  strokeWeight(10)
  noFill()
  arc(width/2, height/2, radius, radius, -PI/2, end)

def drawTime():
  theText=nf(hour(), 2)+":"+nf(minute(), 2)+":"+nf(second(), 2)
  textSize(75)
  fill(0)
  tWidth = textWidth(theText) * 0.5
  tAscent = textAscent() * 0.375
  # draw text offset from the centre of the screen
  text(theText, width/2 - tWidth, height/2 + tAscent )

run()