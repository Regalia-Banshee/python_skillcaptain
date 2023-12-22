import re

def check_password_strength(password):
    strength=0

    # Criteria for password strength
    length_regex = re.compile(r'.{8,}')  # At least 8 characters
    uppercase_regex = re.compile(r'[A-Z]')  # At least one uppercase letter
    lowercase_regex = re.compile(r'[a-z]')  # At least one lowercase letter
    digit_regex = re.compile(r'\d')  # At least one digit
    special_char_regex = re.compile(r'[^A-Za-z0-9]')  # At least one special character

    # Check each criterion using regular expressions
    if length_regex.search(password):
        strength += 1
    if uppercase_regex.search(password):
        strength += 1
    if lowercase_regex.search(password):
        strength += 1
    if digit_regex.search(password):
        strength+= 1
    if special_char_regex.search(password):
        strength+= 1

    return strength

# Main program
user_password = input("Enter your password: ")
password_strength= check_password_strength(user_password)

# Providing feedback based on the password strength

if password_strength== 5:
    print("Your password is strong.")
elif password_strength >= 3:
    print("Your password is of medium strength.")

else:
    print("Your password is weak.")