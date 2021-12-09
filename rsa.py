# generate Public key for encryption

# two prime numbers
p1 = 17
p2 = 11
# rsa modulus
product = p1 * p2
# must lie between 1 and the product
exponent = 3
# totient of n
totient = (p1 - 1) * (p2 - 1)

# Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mul_inverse(e, r):
    for i in range(r):
        if ((e * i) % r == 1):
            return i


d = mul_inverse(exponent, totient)

# Public key is (exponent, product) and private key is (d,product)


public = (exponent, product)
private = (d, product)
print("Private Key is:", private)
print("Public Key is:", public)


def encrypt(prk, plaintext):
    # Unpack the key into it's components
    key, n = prk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    ciphertext = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return ciphertext


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    text = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(text)


en_message=input("Enter message: ")
print(encrypt(private, en_message))
ciphertext = encrypt(private, en_message)

print('Decrypted text: ' ,decrypt(public,ciphertext ))