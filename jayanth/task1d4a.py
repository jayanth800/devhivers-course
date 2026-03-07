#factorial
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

print("Factorial of 5:", factorial(5))
print("Factorial of 7:", factorial(7))