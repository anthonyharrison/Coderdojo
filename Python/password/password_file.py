MIN_PASSWORD_LENGTH = 8

PASSWORD_FILE = "passwords.txt"

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

def read_password_file():
    filehandle = open(PASSWORD_FILE, "r")
    file_data = filehandle.read()
    filehandle.close()
#     print (f"File content is {file_data}")
    return file_data

def update_password_file(username, password):
    filehandle = open(PASSWORD_FILE, "a")
    filehandle.write(f"{username},{password}\n")
    filehandle.close()
    print ("Updated password file")

def check_password(name, password):
    password_data = read_password_file()
#     print (f"Password data: {password_data}")
    password_information = f"{name},{password}\n"
    if password_information in password_data:
        return True
    return False

print ("Hello Codedojo")
valid_name = False
# WHILE VALID NAME IS NOT TRUE
while valid_name == False:
    name = input("What is your first name?")
    # Check that the name is valid. Only allow alphabetic characters.
    if name.isalpha():
        # Valid name
        print (f"Hello {name.capitalize()}, I hope you have a great day.")
        valid_name = True
    else:
        print ("That isn't a valid name.")

valid_password = False
while not valid_password:
    # Password entry
    password = input("Please enter your password.")
    if validate_password(password):
        print (f"{password} is a valid password.")
        valid_password = True
    else:
        print("That is not a valid password.")
    
update_password_file(name, password)

if check_password(name, password):
    print (f"Welcome {name}")
