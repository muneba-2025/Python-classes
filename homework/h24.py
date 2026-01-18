import random
import string

def generate_password(length=12): 
    """Generates a random password with letters, digits, and symbols."""
    letters = string.ascii_letters # a-z, A-Z
    digits = string.digits       # 0-9
    symbols = string.punctuation # !, @, #, $, etc.

    # Combine all characters 
    all_characters = letters + digits + symbols

    # Generate the password using a list comprehension and join
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

password_length = 10 
new_password = generate_password(password_length)
print(f"The random password is: {new_password}")
