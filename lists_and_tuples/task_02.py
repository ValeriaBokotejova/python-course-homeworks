import random 
import string

all_characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)

password = ""
for _ in range(8):
    password += random.choice(all_characters)

print("Generated password:", password)
