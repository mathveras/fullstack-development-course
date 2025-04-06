# --- Factorial Calculator --- #

""" 
A factorial, denoted by an exclamation mark (!), is a mathematical function that multiplies a given positive integer by all the positive integers less than it. 

Example: 
    The factorial of 5 (written as 5!) is calculated as:
        5! = 5 * 4 * 3 * 2 * 1 = 120

The factorial of 0 is defined to be 1. Factorials are commonly used in permutations, combinations, and other areas of mathematics and computer science.
"""
print("--- Factorial Calculator ---")
number = int(input("Enter a number: "))

result = 1
count = 1

while count <= number:
    result *= count
    print(result)
    count += 1
print(f"The factorial of {number} is equal to: {result}")
