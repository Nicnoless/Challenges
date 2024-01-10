# Create a program that counts the frequency of each character in a given string and then
# prints the characters along with their frequencies.

def count_char_freq(user_input):
    frequency = {}
    for char in user_input:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    for char, freq in frequency.items():
        print(f"Character '{char}' appears {freq} time(s) in the input.")

user_input = input("Enter a word or phrase to count how many each character is used: ")
count_char_freq(user_input)