# library for hashing
import hashlib
import random
import string

# Ask user for input to be hashed
plain_text = input("Enter your plain text: " )

# For salting random characters are added to the password
# before they are hashed

salt = plain_text.join((random.choice(string.ascii_letters) for x in range(5)))


# Return sha256 hash of the salt
# it is encoded in ascii to produce all character set
# Hexdigest produces the hashed output in hexadecimal
print(hashlib.sha256(salt.encode('ascii')).hexdigest())