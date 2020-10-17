'''
Zoe Piccirillo
Cybersecurity Pd. 5
October 19, 2020

Encode/decode Vigenere ciphers using a keyword

Encode: make run ARGS="encode plaintext key"
Decode: make run ARGS="decode ciphertext key"
'''
import sys

#modify the keyword so it matches the length of the text, go through the keyword & text letter by letter to encode/decode
def solve(text, key_word, algorithm):
    #note to self: do we have to account for one-letter keys too?? (autokey method?)
    #remove punctuation and whitespace from text
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'' " "'''
    for letter in text:
        if letter in punc:
            text = text.replace(letter, "")
    #add keyword to itself until it reaches the length of the text
    key = key_word
    count = 0
    while (len(key) < len(text)):
        key = key + key_word[count]
        if (count == len(key_word) - 1):
            count = 0
        else:
            count += 1
    #decode the text using the keyword, letter by letter
    str = ""
    for i in range(len(text)):
        str += shift_letter(text[i], key[i], algorithm)
    print(str.upper())

#shift individual letters based on letter & corresponding key letter
def shift_letter(letter, key_letter, algorithm):
    letter = letter.lower()
    key_letter = key_letter.lower()
    alpha_index = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, #dictionary to store letters and their indexes
                "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15,
                "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}
    letter_index = alpha_index[letter]
    key_letter_index = alpha_index[key_letter]
    shift_index = 0
    if (algorithm == "decode"): #for decoding: subtract key letter index from letter index & adjust if less than 0
        shift_index = letter_index - key_letter_index
        if (shift_index < 0):
            shift_index = shift_index % 26
    else: #for encoding: subtract key letter index from letter index & adjust if less than 0
        shift_index = letter_index + key_letter_index
        if (shift_index > 25):
            shift_index = shift_index % 26
    alpha_keys = list(alpha_index.keys()) #index of encoded/decoded letter
    return alpha_keys[shift_index] #return the encoded/decoded letter

#main method: take arguments algorith, text and key_word; solve
if __name__ == "__main__":
    algorithm = sys.argv[1]
    text = sys.argv[2]
    key_word = sys.argv[3]
    solve(text, key_word, algorithm)
