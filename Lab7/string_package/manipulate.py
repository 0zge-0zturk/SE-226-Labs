import string
def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return s.upper()

def remove_punctuation(s):
    result = s
    for char in string.punctuation:
        result = result.replace(char, '')
    return result
