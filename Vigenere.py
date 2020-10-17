def solve(text, key_word, algorithm):
    #add keyword to itself until it reaches the length of the text
    #note to self: change everything to uppercase later
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

solve("HOTDOGSTAND", "boar", "encode")

'''
print("HOTDOGSTAND")
shift_letter("I", "B", "decode")
shift_letter("C", "O", "decode")
shift_letter("T", "A", "decode")
shift_letter("U", "R", "decode")
shift_letter("P", "B", "decode")
shift_letter("U", "O", "decode")
shift_letter("S", "A", "decode")
shift_letter("K", "R", "decode")
shift_letter("B", "B", "decode")
shift_letter("B", "O", "decode")
shift_letter("D", "A", "decode")

print("ICTUPUSKBBD")
shift_letter("H", "B", "encode")
shift_letter("O", "O", "encode")
shift_letter("T", "A", "encode")
shift_letter("D", "R", "encode")
shift_letter("O", "B", "encode")
shift_letter("G", "O", "encode")
shift_letter("S", "A", "encode")
shift_letter("T", "R", "encode")
shift_letter("A", "B", "encode")
shift_letter("N", "O", "encode")
shift_letter("D", "A", "encode")
'''
