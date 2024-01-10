# Create a code using the first 5 challenges.

def main():
    print("Welcome to my first program! I have 5 modules in this program that you can try out. Please enter 'palindrome', 'Fibonacci', 'list', 'count', or 'password' to get started or enter 'quit' to exit the program. Once you've completed a module, it won't be available again until you reset this program.")
    while True:
        user_input = input("Enter your command: ")
        if user_input == 'palindrome':
            import Challenge1
        elif user_input == 'Fibonacci':
            import Challenge2
        elif user_input == 'list':
            import Challenge3
        elif user_input == 'count':
            import Challenge4
        elif user_input == 'password':
            import Challenge5
        else:
            ans = input("Would you like to exit the program? Please enter 'y' or 'n': ")
            if ans == 'y':
                break

if __name__ == "__main__":
    main()
