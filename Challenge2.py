# Write a code to find the sum of the even numbers in a Fibonacci sequence.

def fibonacci(start, limit):
    fibonacci = []
    a, b = start, 1
    while a + b <= limit:
        a, b = b, a + b
        fibonacci.append(b)
    return fibonacci

start = int(input("Enter a number to start the sequence: "))
limit = int(input("Enter the limit: "))
print("Your sequence is:", fibonacci(start, limit))

result = fibonacci(start, limit)
even_sum = sum(num for num in result if num % 2 == 0)
print("The sum of the even numbers in your Fibonacci sequence is:", even_sum)