# Coderdojo Virtual #2

import random

def throw_dice():
	dice = random.randint(1,6)
	return str(dice)

def dice():
	no_of_dice = input("How many dice? ")

	throw = []
	for i in range(int(no_of_dice)):
		throw.append(throw_dice())

	for i in throw:
		print (i, end = " ")

# Main

dice()

#End

