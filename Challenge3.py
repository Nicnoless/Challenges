# Create a list of numbers and then return a new list with only the even numbers from the
# original list.

original = []
while True:
    user_input = input("Enter a number to add to your list or 'quit' when you're finished: ")
    if user_input == 'quit':
        break
    else:
        num = int(user_input)
        original.append(num)

print("Your list is:", original)
even_nums = [num for num in original if num % 2 == 0]
print("The even numbers in your list is:", even_nums)