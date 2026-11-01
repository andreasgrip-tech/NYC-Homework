#Password Check: Write a program which ask user to give a password and check if the password is strong. A strong password will have at least 8 characters, upper and lower case characters, digits, and special characters (!@#$%^&), at least one of each category. 
#first step is to ask user to give a password and then check if the password is strong or not.
password = input("Please enter a password: ")  
#check if the password is strong or not
if len(password) < 8:
    print("Password is too short.")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-+"
    
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in special_characters:
            has_special = True

    if not has_upper:
        print("Password must contain at least one uppercase letter.")
    if not has_lower:
        print("Password must contain at least one lowercase letter.")
    if not has_digit:
        print("Password must contain at least one digit.")
    if not has_special:
        print("Password must contain at least one special character.")

    if has_upper and has_lower and has_digit and has_special:
        print("Password is strong.")
#Now if password is not strong, ask user to give a new password and check again until the password is strong.
while not (has_upper and has_lower and has_digit and has_special):
    password = input("Please enter a new password: ")
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in special_characters:
            has_special = True

    if not has_upper:
        print("Password must contain at least one uppercase letter.")
    if not has_lower:
        print("Password must contain at least one lowercase letter.")
    if not has_digit:
        print("Password must contain at least one digit.")
    if not has_special:
        print("Password must contain at least one special character.")

    if has_upper and has_lower and has_digit and has_special:
        print("Password is strong.")
