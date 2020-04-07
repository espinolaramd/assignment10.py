#Diego Espinola
#04.05.2020
#is a continuation of assignment 9

#I removed the method strips spaces.
def is_word_palindrome(word):
    word = word.lower()

    if len(word)<1:
        return True

    elif word[0] != word[-1]:
        return False

    else:
        return is_word_palindrome(word[1:-1])

#I add this to the program. This will remove all punctuation.
line = str(input("Type a word to check if it is palindrome \n>"))
word = ""

if not line.isalpha():
    for char in line:
        if char.isalpha():
            word += char
is_word_palindrome(word)
if is_word_palindrome(word) == True:
    print(f"{word} is palindrome")
else:
    print(f"{word} is not palindrome")
while is_word_palindrome(word) == True or is_word_palindrome(word) == False:
    word = str(input("Type a word to check if it is palindrome \n>"))
    is_word_palindrome(word)
    if is_word_palindrome(word) == True:
        print(f"{word} is palindrome")
    else:
        print(f"{word} is not palindrome")
