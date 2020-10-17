import sys

def solve(text, key_word, algorithm):
    #add keyword to itself until it reaches the length of the text
    #note to self: change everything to uppercase later
    #note to self: do we have to account for one-letter keys too?? (autokey method?)
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'' " "'''

    for letter in text:
        if letter in punc:
            text = text.replace(letter, "")

    key = key_word
    count = 0
    while (len(key) < len(text)):
        key = key + key_word[count]
        if (count == len(key_word) - 1):
            count = 0
        else:
            count += 1
    str = ""
    for i in range(len(text)):
        str += shift_letter(text[i], key[i], algorithm)
    print(str.upper())

def shift_letter(letter, key_letter, algorithm):
    letter = letter.lower()
    key_letter = key_letter.lower()
    alpha_index = {"a": 0, "b": 1, "c": 2,
    "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18,
                "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

    letter_index = alpha_index[letter]
    #print(letter_index)
    key_letter_index = alpha_index[key_letter]
    #print(key_letter_index)
    shift_index = 0
    if (algorithm == "decode"):
        shift_index = letter_index - key_letter_index
        if (shift_index < 0):
            shift_index = shift_index % 26
    else:
        shift_index = letter_index + key_letter_index
        if (shift_index > 25):
            shift_index = shift_index % 26
    alpha_keys = list(alpha_index.keys())
    return alpha_keys[shift_index]

if __name__ == "__main__":
    algorithm = sys.argv[1]
    print(algorithm)
    text = sys.argv[2]
    print(text)
    key_word = sys.argv[3]
    print(key_word)
    solve(text, key_word, algorithm)
