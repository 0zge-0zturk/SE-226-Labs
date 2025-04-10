from string_package import reverse_string,remove_punctuation,count_words,capitalize_words,count_characters,average_word_length

sentence = input("Enter a sentence: ")

print(reverse_string(sentence))
print(capitalize_words(sentence))

print(remove_punctuation(sentence))
print(count_words(sentence))
print(count_characters(sentence))

print((average_word_length(sentence)))
