# --- Ternary Operator --- #

""" 
A ternary operator is a shorthand way of writing an if-else statement in Python.
It allows you to assign a value to a variable based on a condition in a single line of code.

The syntax is as follows:
    variable = value_if_true if condition else value_if_false
"""
print("--- Ternary Operators ---")

# Example 1: Checking age majority
print("\n>>> Check Age Majority <<<")
age = int(input("Enter your age: "))
majority = True if age >= 18 else False
print(f"{age} is an adult.\n" if majority else f"{age} is a minor.\n")

# Example 2: Checking if a number is even or odd
print(">>> Check Even or Odd Number <<<")
number = int(input("Enter a number: "))
is_even = True if number % 2 == 0 else False
print(f"{number} is an even number.\n" if is_even else f"{number} is an odd number.\n")

# Example 3: Uppercase or lowercase.
print(">>> Uppercase or Lowercase <<<")
text = str(input("Enter a text: "))
text_case = "uppercase." if  text.isupper() else "lowercase."
print(f"The text '{text}' is {text_case}\n")

# Example 4: Check the amount of characters.
print(">>> Test Your Precision <<<")
text = str(input("Enter a text with 100 characters: "))
text_count = len(text)
has_hundred = True if (text_count) == 100 else False
has_more = True if (text_count) > 100 else False
if has_hundred:
    print(f"The text '{text}' is FLAWLESS! Exactly {text_count} characters. 🥳 ")
elif has_more:
    print(f"I said 100! The text '{text}' has {text_count} characters. 😠")
else:
    print(f"Are you lazy to type? The text '{text}' has {text_count} characters. 🙄")
