# Input number
n = int(input("Enter number: "))

# Calculate factorial
fact = 1
for i in range(1, n + 1):
    fact *= i

# Output
print("Factorial =", fact)