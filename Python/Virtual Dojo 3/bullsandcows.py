# A version of the classic Bulls and Cows game
#
import random

# Key constants
MAX_GUESS = 10
SIZE = 4
MIN_NUM = 0
MAX_NUM = 5

def generate_code():
    secret = []
    for i in range(SIZE):
        # Generate a random digit
        code = random.randint(MIN_NUM,MAX_NUM)
        secret.append(str(code))
    return secret

def check_guess (code, guess):
    result = ""
    bull = 0
    cow = 0
    win = False
    # Validate length of guess
    if len(guess) > SIZE:
        # Too many digits
        result = "Pig"
    else:
        for i in range (len(guess)):
            if guess[i] == code [i]:
                # A valid digit in correct position
                bull = bull + 1
                result = result + "Bull "
            elif guess[i] in code:
                # A valid digit, but not in correct position
                cow = cow + 1
                result = result + "Cow "
        # Now check result
        if bull == SIZE:
            # All digits found
            result = "Farmer"
            win = True
        elif bull == 0 and cow == 0:
            # No digits found
            result = "Chicken"
    print ("[RESULT]",result)
    return win

def introduce_game():
    print ("Welcome to Bulls and Cows")
    print ("Try and guess my secret", SIZE,"digit code containing the digits",MIN_NUM,"to",MAX_NUM)
    print ("I know it is hard, but I will try and give you some help.")
    print ("If I say:")
    print ("BULL    You have a valid digit in the correct position")
    print ("COW     You have a valid digit but in the wrong position")
    print ("CHICKEN You have no valid digits")
    print ("FARMER  You have all valid digits in the correct position")
    print ("")
    print ("Good luck!")
         
# Game

game_end = False

while not game_end:

    introduce_game()

    code = generate_code()
    count = 0
    win = False
    while count < MAX_GUESS and not win:
        count = count + 1
        print ("Guess #",count)
        guess = input("Enter your guess ")
        win = check_guess(code,guess)
    # Game over...
    if win:
        print ("Well done")
    else:
        print ("Never mind, try again")
        print ("My secret code was",code)

    # Play again?
    again = input("Do you want to play again (Y/N)? ")
    if again.upper() == "N":
        game_end = True

print ("Thanks for playing. Have a nice day")
    
        


