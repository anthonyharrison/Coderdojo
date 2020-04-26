# Coderdojo Virtual #2

import random

def choose_ball(max):
	return str(random.randint(1, max))
	
def show_balls(balls):
	for i in balls:
		print (i, end = " ")	

def draw_lottery(no_of_balls, max_number):
	balls = []
	balls_drawn = 0
	print ("\nDrawing balls....")
	while balls_drawn < no_of_balls:
		ball = choose_ball(max_number)
		if ball not in balls:
			balls.append(ball)
			#print (ball + " drawn")
			balls_drawn = balls_drawn + 1
		#else:
		#	print (ball + " already drawn")

	show_balls(balls)
	print("\nAnd now sorted in ascending order")
	balls.sort()
	show_balls(balls)
		
	return balls

def check_balls(balls, my_balls):
	# Return number of matching balls
	count = 0
	for i in my_balls:
		#print (i, end =" ")	
		# Is the ball in the drawn set?
		if i in balls:
			count = count + 1
	return count

# Main

no_of_balls = int(input("How many balls? "))
max_number = int(input("Largest number? "))

my_choice = []
for i in range(no_of_balls):
	valid_ball = False
	while not valid_ball:
		ball = input("Choose ball " + str(i+1) + " > ")
		# Check ball is in valid range
		if int(ball) in range (1, max_number+1):
			valid_ball = True
	my_choice.append(ball)

# Sort into ascending order
my_choice.sort()
print("\nMy choice...")
show_balls(my_choice)

balls = draw_lottery (no_of_balls, max_number)
result = check_balls(balls, my_choice)

# Have we won?
if result == no_of_balls:
	print ("\n\n\n!!!!!!WINNER!!!!!!\n\n\n")
elif result == 0:
	print ("\n\nUnfortunately you had no matching balls")
elif result == 1:
	print ("\n\nYou had 1 matching ball")
else:
	print ("\n\nYou had " + str(result) + " matching balls")

#End

