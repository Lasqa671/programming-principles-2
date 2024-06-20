"""
Write a Python function that checks whether a 
word or phrase is palindrome or not. 
Note: A palindrome is word, phrase, or 
sequence that reads the same backward as 
forward, e.g., madam
"""
def is_palindrome(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    length = len(cleaned_word)

    for i in range(length // 2):
        if cleaned_word[i] != cleaned_word[length - 1 - i]:
            return False
    return True

user_input = input()

if is_palindrome(user_input):
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")