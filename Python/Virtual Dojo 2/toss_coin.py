# Coderdojo Virtual #2

import random

def toss_coin(count):
	HEADS = 0
	TAILS = 1
	heads = 0
	tails = 0
	
	for i in range (count):
		choice = random.randint(0,1)
		if choice == HEADS:
			heads = heads + 1
		else:
			tails = tails + 1
	return heads, tails

def coins():	
	count = input ("How many times to toss coin> ")
	heads, tails = toss_coin (int(count))

	print ("Total:" + str(heads + tails))
	print ("Heads:" + str(heads))
	print ("Tails:" + str(tails))

# Main

coins()

#End