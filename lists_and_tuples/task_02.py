import random 
import string

all_characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)

random_pass = random.choices(all_letters, k=8)
password = ''.join(random_pass)

print("Generated password:", password)
