import string
import random

plaintext = input(str("Enter a word to be encrypted \n==>"))
chars = list(' ' + string.ascii_letters + string.digits + string.punctuation)


def key(chars):
    shuffled_letters = chars.copy()  # creates a copy of all the characters in the list
    random.shuffle(shuffled_letters)  # shuffles all the characters
    return shuffled_letters


def encrypt(plaintext, key, chars):
    # indexes the characters, loops and replaces plaintext chars with key chars generated randomly
    encryption = [key[chars.index(i)] for i in plaintext]
    return ''.join(encryption)  # joins the list back into a string


new_key = key(chars)  # call the key function to create a new key
# call the encrypt function to create cipher of plaintextS
cipher = encrypt(plaintext, new_key, chars)

print(cipher)


# Substitution method Encryption Python

# Create a python code that does the substitution method encryption. It should be able to take user input of plaintext and output a ciphertext. Submission via email (welhalabi@lagcc.cuny.edu).

# Hint:
# Use for loop to index characters of ASCII, string, and numbers.

# You should be able to take all what we learned and combine everything.

# Use both import string and random to access more options.
