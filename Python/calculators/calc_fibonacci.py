# --- Fibonacci Calculator --- #

""" 
A Fibonacci sequence is a series of numbers where each number is the sum of the two numbers before it. The sequence can be described mathematically as: 
    xn= xn-1 + xn-2

Example:
    The first 10 numbers in the Fibonacci sequence are: 
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34 
    The sequence can theoretically continue to infinity 
"""
def fibonacci_loop(n):
    sequence = [0, 1]

    if n < 1:
        raise TypeError("'n' must be greater or equal to '1'.")
    
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

print('--- Fibonacci Calculator ---')
n = int(input('Type a value: '))
fibonacci_sequence = fibonacci_loop(n)
print(f'Fibonacci sequence up to {n}: {fibonacci_sequence}')
