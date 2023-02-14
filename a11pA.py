# Write a program that uses the Vigenère cipher to encrypt and decrypt messages.
# Your program will prompt the user to either encrypt or decrypt a message, the
# message itself, and the encryption key.  It will then print out the encrypted
# message if the user selected encryption or the decrypted (plaintext) message
# if the user selected decryption.
#
# Please refer to the assignment document via Canvas for a full explanation of
# the problem.
#
# You are required to create 4 functions to solve this problem:
#
# read_vigenere_table(): one parameter, the name of the file that contains the
#   cipher table; returns the table as a dictionary of dictionaries.
#   - This function will open the file (with all normal error checking), and
#     read the contents.
#   - It will create a new dictionary and return it.
#   - Each line from the file will add a new key, value pair to the dictionary
#     where the key is the first character and the value is itself a dictionary.
#     As you parse each character on the line, you will add new entries to that
#     inner dictionary.
#   - Don't forget that you can enumerate() strings just like lists; for
#     example, a string with all of the letters in the alphabet in it (see
#     above).
#   - Note that the instructor's solution for this function is 15 lines,
#     including all of the file I/O handling, etc.
#
# extend_key(): two parameters: the message being encrypted/decrypted and the
#   key; returns a new version of the key where the original key is repeated
#   such that the new version is at least as long as the message itself.
#   - Don't overthink this one.  Just keep adding the key to itself until it's
#     long enough.
#   - The instructor's solution is 5 lines.
#
# encrypt(): three parameters: the plaintext message, the key, and the cipher
#   table (dictionary); returns the encrypted message.
#   - Use the table as above to turn every letter into its encrypted equivalent.
#   - Skip over any characters that aren't uppercase characters, putting them
#     into the encrypted message unchanged.  string.ascii_uppercase can help
#     with this check.
#   - The instructor's solution is 10 lines.
#
# decrypt(): three parameters: the encrypted message, the key, and the cipher
#   table (dictionary); returns the plaintext message.
#   - Use the table as above to turn every letter back into its plaintext
#     equivalent.
#   - Skip over any characters that aren't uppercase characters, putting them
#     into the plaintext message unchanged.  string.ascii_uppercase can help
#     with this check.
#   - This is slightly harder than encrypt() because you have to iterate through
#     the inner dictionary to find the encrypted character (the value in the
#     inner dictionary) and get the associated column value (the key in the
#     inner dictionary).
#   - The instructor's solution is 13 lines.
#
# The main program will call read_vigenere_table(), then prompt the user to
# either encrypt or decrypt.  If encrypting, get the plaintext message and the
# key, use extend_key() to ensure the key is long enough, then call encrypt()
# and print the result.  If decrypting, get the encrypted message and the key,
# use extend_key() to ensure the key is long enough, then call decrypt() and
# print the result.  In all cases, the messages and keys should be converted to
# all uppercase characters.
#
# Always, be sure to take this problem one step at a time.  Test your code early
# and often.  One of the challenges here is understanding the process, so be
# sure you have a handle on what you are trying to do before jumping into the
# code.  You'll have to write read_vigenere_table() before you can do any
# encrypting/decrypting, but you can print out the dictionary as you create it
# to convince yourself it's correct.  Write and test encrypt() before worrying
# about decrypt().
#
# Your input and output messages must conform to the following examples:
#
# Do you want to encrypt or decrypt? um
# Invalid answer!
#
# Do you want to encrypt or decrypt? encrypt
# Enter the message to be encrypted: computer science is awesome!
# Enter the key: pickle
# RWOZFXTZ UMTICKG SD ELMUYXI!
#
# Do you want to encrypt or decrypt? decrypt
# Enter the message to be decrypted: RWOZFXTZ UMTICKG SD ELMUYXI!
# Enter the key: pickle
# COMPUTER SCIENCE IS AWESOME!
#
# Note the order of inputs, capitalization of messages, spacing, etc.


import sys
import string

def read_vigenere_table(file):
    cipher_dict = {}
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    x = 0
    try:
        with open(file) as in_file:
            for line in in_file:
                line = line.strip()
                cipher_dict[alphabet[x]] = {}
                smaller_dict = cipher_dict[alphabet[x]]
                y = 0
                for char in line:
                    smaller_dict[alphabet[y]] = char
                    y+=1
                x += 1
    except IOError:
        print("Couldn't open cipher_table.txt!")
        sys.exit()
    return cipher_dict

def extend_key(key, message):
    original_key = key
    while len(key) <= len(message):
        key += original_key
    return key

def encrypt(message, key, cipher_dict):
    encrypted_mssg = "null"
    for char_k, char_m in zip(key, message):
        if char_m in string.ascii_uppercase:
            if encrypted_mssg == "null":
                encrypted_mssg = cipher_dict[char_k][char_m].strip()
            else:
                encrypted_mssg += cipher_dict[char_k][char_m].strip()
        else:
            if encrypted_mssg == "null":
                encrypted_mssg = char_m
            else:
                encrypted_mssg += char_m
    return encrypted_mssg

def decrypt(message, key, cipher_dict):
    decrypted_mssg = "null"
    for char_k, char_m in zip(key, message):
        if char_m in string.ascii_uppercase:
            if decrypted_mssg == "null":
                for key, value in cipher_dict[char_k].items():
                    if value == char_m:
                        decrypted_mssg = key.strip()           
            else:
                for key, value in cipher_dict[char_k].items():
                    if value == char_m:
                        decrypted_mssg += key.strip()
        else:
            if decrypted_mssg == "null":
                decrypted_mssg = char_m
            else:
                decrypted_mssg += char_m
    return decrypted_mssg

cipher_dict = read_vigenere_table("cipher_table.txt")

x = input("Do you want to encrypt or decrypt? ")
if x == "encrypt":
    message = input("Enter the message to be encrypted: ")
    message = message.upper()
    key = input("Enter the key: ")
    key = key.upper()
    key = extend_key(key, message)
    encrypted_mssg = encrypt(message, key, cipher_dict)
    print(encrypted_mssg)
elif x == "decrypt":
    message = input("Enter the message to be decrypted: ")
    message = message.upper()
    key = input("Enter the key: ")
    key = key.upper()
    key = extend_key(key, message)
    decrypted_mssg = decrypt(message, key, cipher_dict)
    print(decrypted_mssg)
else:
    print("Invalid answer!")
    sys.exit()
