from string_package import manipulate
def count_characters(s):
    return len(s)

def count_words(s):
    return len(s.split())

def average_word_length(s):
    trimmed = manipulate.remove_punctuation(s)
    words = trimmed.split()
    return sum(len(word) for word in words) / len(words)
