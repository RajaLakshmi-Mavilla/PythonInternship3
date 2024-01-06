import string
import random

characters = string.ascii_letters + string.digits + string.punctuation

# Enter password in the range of 6 to 15
length = int(input("Enter the length of the password: "))

if 6 <= length <= 15:
    password = ''.join(random.choices(characters, k=length))
    print("Your password is:", password)
else:
    print("Enter a valid length between 6 and 15.")