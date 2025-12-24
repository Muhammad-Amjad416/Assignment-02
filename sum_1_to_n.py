# Function to calculate sum from 1 to n using recursion
def sum_numbers(n):
    # Base case: sum of 0 is 0
    if n == 0:
        return 0

    # Recursive case: add n to sum of previous numbers
    return n + sum_numbers(n - 1)


# Driver code
n = int(input("Enter a number: "))
result = sum_numbers(n)
print("Sum from 1 to", n, "is:", result)
