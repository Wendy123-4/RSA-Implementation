# library for hashing
import hashlib

# Ask user for input to be hashed
plain_text = input("Enter your plain text: " )

# Return sha256 hash of the text
# it is encoded in ascii to produce all character set
# Hexdigest produces the hashed output in hexadecimal
print(hashlib.sha256(plain_text.encode('ascii')).hexdigest())