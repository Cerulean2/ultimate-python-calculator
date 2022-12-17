from functools import *
import math

print("""Welcome to the ultimate calculator! With this tool, you can perform a wide range of calculations and even review your previous calculations. 
Simply choose one of the options below to get started.""")

# Menu with options for the user
def options():
    print("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Square Root
    6. Exponentiation
    7. Modulus
    \n* You can also type 'Quit' or 'History' at any time to exit the calculator or review your previous calculations, respectively.
    """)

# Calculation history
history = []

# Main loop
while True:
    # Displays the options
    options()
    try:
        # Takes input for the menu
        option = input().capitalize()
        # Addition
        if option == "1":
            while True:
                print("\nEnter your addition calculation down below, type exit to go back.")
                print("Please seperate your numbers by a comma")
                nums = input()
                if nums.capitalize() == "Exit":
                    break
                try:
                    # Splits numbers into a list
                    x = nums.split(",")
                    # Uses map to run int() on every element in this list
                    # This converts all the populated strings into intergers
                    x = list(map(float, x))
                    # Uses reduce in lambda to perform addition, passes x into lambda's arguments
                    result = reduce(lambda a, b: a + b, x)
                    # Appends the equation to the history list as a string
                    history.append(f"{' + '.join(map(str, x))} = {str(result)}")
                    # Prints result 
                    print("\nResult of added numbers: {}".format(result))
                # Error handling if the user doesn't seperate numbers by a comma
                except ValueError:
                    print("\n* Invalid input. Perhaps you entered a non-number or forgot to use commas?\n")
                    print("""
                    Example:
                    > 1,2
                    > Result of added numbers: 3
                    """)
                continue
        # Subtraction
        elif option == "2":
            while True:
                print("\nEnter your subtraction calculation down below, type exit to go back.")
                print("Please seperate your numbers by a comma")
                nums = input()
                if nums.capitalize() == "Exit":
                    break
                try:
                    x = nums.split(",")
                    x = list(map(float, x))
                    # Uses reduce in lambda to perform subtraction this time
                    result = reduce(lambda a, b: a - b, x)
                    # Appends the equation to the history list as a string
                    history.append(f"{' - '.join(map(str, x))} = {str(result)}")
                    # Prints result
                    print("\nResult of subtracted numbers: {}".format(result))
                except ValueError:
                    print("\n* Invalid input. Perhaps you entered a non-number or forgot to use commas?\n")
                    print("""
                    Example:
                    > 1,2
                    > Result of subtracted numbers: -1
                    """)
                continue
        # Multiplication
        elif option == "3":
            while True:
                print("\nEnter your multiplication calculation down below, type exit to go back.")
                print("Please seperate your numbers by a comma")
                nums = input()
                if nums.capitalize() == "Exit":
                        break
                try:
                    x = nums.split(",")
                    x = list(map(float, x))
                    # Uses reduce in lambda to perform multiplication this time
                    result = reduce(lambda a, b: a * b, x)
                    # Appends the equation to the history list as a string
                    history.append(f"{' * '.join(map(str, x))} = {str(result)}")
                    # Prints result
                    print("\nResult of multiplied numbers: {}".format(result))
                except ValueError:
                    print("\n* Please seperate your entries by a comma.\n")
                    print("""
                    Example:
                    > 2,6
                    > Result of multiplied numbers: 12
                    """)
                continue
        # Division
        elif option == "4":
            while True:
                print("\nEnter your division calculation down below, type exit to go back.")
                print("Please seperate your numbers by a comma")
                nums = input()
                if nums.capitalize() == "Exit":
                    break
                try:
                    x = nums.split(",")
                    x = list(map(float, x))
                    # Uses reduce in lambda to perform division this time
                    # In this program, we're using True Division, not floor division (//) because we whole percise decimal operations
                    # You can also wrap reduce in round() if you want to round the result, but typically calculators don't do this.
                    try:
                        result = reduce(lambda a, b: a / b, x)
                        # Appends the equation to the history list as a string
                        history.append(f"{' / '.join(map(str, x))} = {str(result)}")
                    except ZeroDivisionError:
                        print("\n* Sorry, you can't divide by zero!")
                        continue 
                    # Prints result
                    print("\nResult of divided numbers: {}".format(result))
                except ValueError:
                    print("\n* Invalid input. Perhaps you entered a non-number or forgot to use commas?\n")
                    print("""
                    Example:
                    > 1,2
                    > Result of divided numbers: 0.5
                    """)
                continue
        # Square Root
        elif option == "5":
            while True:
                print("\nEnter your square root calculation down below, type exit to go back.")
                print("Please seperate your numbers by a comma")
                num = input()
                if nums.capitalize() == "Exit":
                        break
                try:
                    x = float(num)
                    # A lambda function that calculates the floor of the square root of a number
                    square_root = lambda x: (math.sqrt(x))
                    # Call the lambda function and pass the number as an argument
                    result = square_root(x)
                    # Appends the equation to the history list as a string
                    history.append(f"√{str(x)} = {str(result)}")
                    # Prints result
                    print("\nSquare Root: {}".format(result))
                except ValueError:
                    print("\n* Invalid input. Perhaps you entered a non-number or used too many numbers?\n")
                    print("""
                    Example:
                    > 10
                    > Square Root: 3.16227766017
                    """)
                continue
        # Exponentiation 
        if option == "6":
            while True:
                print("\nEnter your exponentiation calculation down below, type exit to go back.")
                print("Please seperate your numbers by a comma")
                nums = input()
                if nums.capitalize() == "Exit":
                        break
                try:
                    # Splits numbers into a list
                    x = nums.split(",")
                    # Uses map to run int() on every element in this list
                    # This converts all the populated strings into intergers
                    x = list(map(float, x))
                    # Uses reduce in lambda to perform exponentiation, passes x into lambda's arguments
                    result = reduce(lambda a, b: a ** b, x)
                    # Appends the equation to the history list as a string
                    history.append(f"{' ** '.join(map(str, x))} = {str(result)}")
                    # Prints result 
                    print("\nResult of exponentiation: {}".format(result))
                # Error handling if the user doesn't seperate numbers by a comma
                except ValueError:
                    print("\n* Invalid input. Perhaps you entered a non-number or forgot to use commas?\n")
                    print("""
                    Example:
                    > 2,3
                    > Result of exponentiation: 8
                    """)
                continue
        # Modulus
        if option == "7":
            while True:
                print("\nEnter your modulus calculation down below, type exit to go back.")
                print("Please seperate your numbers by a comma")
                nums = input()
                if nums.capitalize() == "Exit":
                        break
                try:
                    # Splits numbers into a list
                    x = nums.split(",")
                    # Uses map to run int() on every element in this list
                    # This converts all the populated strings into intergers
                    x = list(map(float, x))
                    # Uses reduce in lambda to perform exponentiation, passes x into lambda's arguments
                    result = reduce(lambda a, b: a % b, x)
                    # Appends the equation to the history list as a string
                    history.append(f"{' % '.join(map(str, x))} = {str(result)}")
                    # Prints result 
                    print("\nResult of modulus: {}".format(result))
                # Error handling if the user doesn't seperate numbers by a comma
                except ValueError:
                    print("\n* Invalid input. Perhaps you entered a non-number or forgot to use commas?\n")
                    print("""
                    Example:
                    > 10,35
                    > Result of modulus: 1
                    """)
                continue
        # Quit 
        elif option == "Quit":
            break
        # History
        elif option == "History":
            if len(history) == 0:
                print("\n* Sorry no history found. Try performing some calculations first!")
                continue
            else:
                print("\nHistory:")
                for i, equation in enumerate(history):
                    print(f"{i+1}. {equation}")
        elif nums.capitalize() == "Exit":
            pass
        # Error handling if the user enters an option not shown in the menu 
        else:
            print("\n* Not a valid option in menu, please try again.")
    except ValueError:
        print("\n* Invalid input, please try again.")