def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

test_values = [5, 6, 7]

for num in test_values:
    print(f"{num}! = {factorial(num)}")
