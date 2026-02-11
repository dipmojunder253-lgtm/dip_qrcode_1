print("Hello, World!")
v = 42
print(f"The answer is {v}.")
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
def add(a, b):
    return a + b
print(f"2 + 3 = {add(2, 3)}")
def multiply(a, b):
    return a * b
print(f"4 * 5 = {multiply(4, 5)}")
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b
print(f"10 / 2 = {divide(10, 2)}")
def subtract(a, b):
    return a - b
print(f"7 - 3 = {subtract(7, 3)}")
def power(base, exp):
    return base ** exp
print(f"2 ^ 3 = {power(2, 3)}")
def modulus(a, b):
    return a % b
print(f"10 % 3 = {modulus(10, 3)}")
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(f"5! = {factorial(5)}")
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
print(f"Fibonacci(6) = {fibonacci(6)}")
def is_even(n):
    return n % 2 == 0
print(f"Is 4 even? {is_even(4)}")
print(f"Is 5 even? {is_even(5)}")
def is_odd(n):
    return n % 2 != 0

print(f"Is 4 odd? {is_odd(4)}")
print(f"Is 5 odd? {is_odd(5)}") 