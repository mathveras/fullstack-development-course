# --- Pascal Triangle --- #

""" 
A Pascal's Triangle is a triangular array of numbers that displays the coefficients of binomial expansions. It starts with "1" at the top, and each number below is the sum of the two numbers directly above it.

Example:
          1
         1 1
        1 2 1
       1 3 3 1
      1 4 6 4 1
"""
def pascal_triangle(n):
    triangle = []
    for line in range(n):
        new_line = [1] * (line + 1)  

        if line >= 2:
            for i in range(1, line):
                new_line[i] = triangle[line-1][i-1] + triangle[line-1][i]
        triangle.append(new_line)

    for line in triangle:
        print(" ".join(map(str, line)))

print("--- Pascal's Triangle ---")
lines = int(input("Enter a number: "))
pascal_triangle(lines)
