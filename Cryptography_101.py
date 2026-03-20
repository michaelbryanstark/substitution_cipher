# Cryptography 101

# T and F => F
# T and T => T
# F or T => T
# T or F => T

# Not reverses results, even not, samer result; odd not, opposite

import string
import random
chars = ["A", "B", "C", "D"]
key = 42
print(f"chars: {chars}")
# output→ chars: ['A', 'B', 'C']
print(f"key: {key}")
# output→ key: 42

letters = ["a", "b", "c", "d"]
print(letters.index("c"))

cards = ["A♠", "K♠", "Q♠", "J♠", "10♠"]
# This part of code create lists as strings
print("Before shuffle:", cards)
random.shuffle(cards)
# This part of code randomizes the card string
print("After shuffle:", cards)


chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
print(chars)


# This last code can help with the lab ^

# Exam Terms
# Brute force
# Vigenère Cipher
# N U Q A I J
