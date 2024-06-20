"""
Write a function that accepts string 
from user and print all permutations of 
that string.
"""
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
user_input = input()
result = reverse_words(user_input)
print(result)