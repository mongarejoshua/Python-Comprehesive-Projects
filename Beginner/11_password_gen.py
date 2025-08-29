import random
import string

all_chars = string.ascii_letters + string.digits + string.punctuation

password = ''
for i in all_chars:
    password += random.choice(all_chars)
    
print(password) 