# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=59
""" 
 
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
 
"""


from time import time
from collections import Counter
from string import ascii_lowercase


DEBUG = False

def dprint(*args):
    if DEBUG:
        print(*args)

def decrypt(ciphertext, keylength, english_text_file):
    """
    Decrypts ciphertext where a keyword of lenght 'keylength' has been XOR'ed to
    the plaintext. (Vigenère cipher)
    """    
    keys = [[] for i in range(0, keylength)]
    
    # DIVIDE INTO SUBSTRINGS BASED ON KEYLENGTH
    substrings = prepare_for_letter_frequency(ciphertext, 3)
    
    # FREQUENCY ANALYSIS OF SUBSTRINGS OF CIPHERTEXT
    counted = [Counter(substrings[i]) for i in range(0, keylength)]
    
    
    #--------------------------------------------------------------------------
    #------------- IF I REMOVE THIS PART, IT DOESN'T WORK...-------------------
    #--------------------------------------------------------------------------
    for index in range(0,len(substrings)):
        for i in range(0,len(substrings[index])):
            substrings[index][i] = substrings[index][i] ^ 69
    
    counted_again = [Counter(substrings[i]) for i in range(0, keylength)]
    #--------------------------------------------------------------------------
    
    
    for index in range(0,len(counted)):
        dprint('Substring', index + 1)
        for entry in counted[index].most_common(10):
            number, count = entry
            count = count / len(substrings[index])
            dprint(number, count)
            if count > 0.15:
                keys[index].append(number)
        dprint()
    
            
    #--------------------------------------------------------------------------
    #------------- IF I REMOVE THIS PART, IT DOESN'T WORK...-------------------
    #--------------------------------------------------------------------------
        dprint('Substring', index + 1, '^ 69')
        for entry in counted_again[index].most_common(10):
            number, count = entry
            count = count / len(substrings[index])
            dprint(number, count)
            if count > 0.15:
                keys[index].append(number)
    #--------------------------------------------------------------------------


    # FREQUENCY ANALYSIS OF OTHER TEXT FOR COMPARISON
    with open(english_text_file) as file:
        lines = [l for l in file]

    file_text = ''.join(lines)
    file_text = [char.lower() for char in file_text if char.lower() in ascii_lowercase]
    comparison = Counter(file_text)

    dprint('English text frequency')
    for entry in comparison.most_common(1):
        number, count = entry
        count = count / len(file_text)
        dprint(ord(number), count)

    # COMPUTE KEYWORD    
    for index in range(0, keylength):
        number = keys[index][0]
        dprint(number)
        keys[index] = number ^ 101
    
    dprint(keys)
    
    # GET PLAINTEXT BY XOR'ING KEYWORD TO CIPHERTEXT SUBSTRINGS
    plaintext = []
    position_index = 0
    substring_index = 0    
        
    while position_index < len(substrings[substring_index]):
        
        plaintext.append(substrings[substring_index][position_index] ^ keys[substring_index])
        
        substring_index += 1
        
        if substring_index == 3:
            substring_index = 0
            position_index += 1
    
    return plaintext
    

def prepare_for_letter_frequency(ciphertext, keylength):
    """
    Divides ciphertext into 'keylength' number of substrings, which each will 
    have same letter frequency as english text.
    """
    substrings = [[] for i in range(0, keylength)]
    
    for index,character in enumerate(ciphertext):
        substrings[index % keylength].append(character)
    
    return substrings


start_time = time()

keylength = 3
english_text_file = 'p059_english_text.txt'

# READ CIPHERTEXT FROM FILE INTO ARRAY
ciphertext = []
with open('p059_cipher.txt') as file:
    for line in file:
        ciphertext = [int(character) for character in line.strip().split(',')]

# DECRYPT CIPHERTEXT
plaintext = decrypt(ciphertext, keylength, english_text_file)
print('Sum of ASCII values in plaintext:',sum(plaintext))

print('Time:', time() - start_time)