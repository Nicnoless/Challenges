# Create a program that generates a random password of a specified length. You can use
# uppercase letters, lowercase letters, numbers, and special characters to create a strong password.

import random
import string

def generate_password(length):
    all_char = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(all_char) for _ in range(length))
    return password

length = 12
password = generate_password(length)
print("Generated password is:", password)