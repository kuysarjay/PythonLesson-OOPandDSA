# Recursion is a programming technique where a function calls itself in order to solve smaller instances of the same problem.
# It is usually used to solve problems that can be broken down into smaller instances of the same problem.

# Example of Recursion:
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

print(fact(5))