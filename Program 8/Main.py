# Author: Jacob Sprouse
# Assignment Title: Program 8
# Assignment Description: Caesar Cipher
# Due Date: 05/04/2023
# Date Created: 05/03/2023
# Date Last Modified: 05/04/2023

# ********************************************************
# Description: shift characters                          *
# return: string                                         *
# precondition: characters and shift are valid           *
# postcondition: returns the shifted characters          *
#                                                        *
# ********************************************************


def crypt_characters(characters, shift):
    result = ''
    for c in list(characters):
        result += chr(ord(c) + shift)
    return result


bad_file = False
invalid_input = False
shift_value = 3
contents = ''

# Input
file_name = input("Please Enter A File Name: ")
print(file_name)

cryption_style = input("Please Enter A Command (encrypt or decrypt): ")
print(cryption_style)

# Input check
if (cryption_style != 'encrypt') and (cryption_style != 'decrypt'):
    invalid_input = True

try:
    file = open(file_name)
except OSError:
    bad_file = True

if cryption_style == 'decrypt':
    shift_value = -3

# Process
if(not bad_file) and (not invalid_input):
    file_contents = file.read()
    contents = crypt_characters(file_contents, shift_value)
    file.close()

# Output
if invalid_input:
    print("Error: Bad Command.")

if bad_file:
    print("Error: File did NOT open.")

if (not bad_file) and (not invalid_input):
    print(contents)

