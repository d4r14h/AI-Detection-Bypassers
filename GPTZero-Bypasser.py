import random

CYRILLIC_MAP = {
    'a': '𝚊',
    'q': '𝚚',
    'u': '𝚞',
    'n': '𝚗',
    't': '𝚝',
    'm': '𝚖',
    'c': '𝚌',
    'o': '𝚘',
    'l': '𝚕 '
}

ZWJ_PROBABILITY = 0.2

def replace_letters(input_text):
    output = ""
    for char in input_text:
        output += CYRILLIC_MAP.get(char, char)
    return output

def insert_zwj(input_text):
    output = ""
    zwj = "\u200D"
    for char in input_text:
        output += char
        if random.random() < ZWJ_PROBABILITY:
            output += zwj
    return output

input_text = input("Enter the detected text: ")
cyrillic_text = replace_letters(input_text)
output_text = insert_zwj(cyrillic_text)
print("Output text: ", output_text)
