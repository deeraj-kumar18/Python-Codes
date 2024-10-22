'''
Problem: Generate a Fibonacci Triangle

You are given an integer `n`. Your task is to generate a Fibonacci Triangle of height `n`. In a
Fibonacci Triangle, each row contains Fibonacci numbers in sequence, starting from 0.

Write a function `fibonacci_triangle(n)` that returns a list of lists representing the Fibonacci Triangle
of height `n`.

Input Format:
- An integer `n` (1 <= n <= 20), representing the height of the triangle.

Output Format:
- A list of lists, where each inner list represents a row of the Fibonacci Triangle.

Example:

Input:
n = 4

Output:
[
[0],
[1, 1],
[2, 3, 5],
[8, 13, 21, 34]
]

Explanation:
- The first row contains the first Fibonacci number: [0]
- The second row contains two Fibonacci numbers: [1, 1]
- The third row contains three Fibonacci numbers: [2, 3, 5]
- The fourth row contains four Fibonacci numbers: [8, 13, 21, 34]
'''