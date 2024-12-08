MIN_PASSWORD_LENGTH = 8

def validate_password(the_password):
    # Validate the password
    # A password must contain letters, numbers and be more than 8 characters long
    valid_password = True
    letter_found = False
    number_found = False
    for char in the_password:
        #print ("The character is", char)
        if char.isalpha():
            # valid
            letter_found = True
        elif char.isnumeric():
            # valid
            number_found = True
        else:
            # invalid
            valid_password = False
    # Check both letters and numbers found
    if letter_found and number_found:
        # valid
        pass
    else:
        valid_password = False
    # Check length of the_password
    if len(the_password) > MIN_PASSWORD_LENGTH:
        # valid
        pass
    else:
        # invalid
        valid_password = False
    return valid_password

print ("Hello Codedojo")
name = input("What is your first name?")
# Check that the name is valid. Only allow alphabetic characters.
if name.isalpha():
    # Valid name
    print (f"Hello {name.capitalize()}, I hope you have a great day.")
else:
    print ("That isn't a valid name.")

# Password entry
password = input("Please enter your password.")
if validate_password(password):
    print (f"{password} is valid.")
else:
    print("That is not a valid password.")
