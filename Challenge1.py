# Create a code to identify if a word is a palindrome.

def palindrome(word):
    word = word.lower()
    reverse = word[::-1]
    return word == reverse

word = input("Enter a word to check if it is a palindrome: ")
ans = palindrome(word)
if ans == True:
    print("Yes, that is a palindrome!")
else:
    print("No, that is not a palindrome!")
