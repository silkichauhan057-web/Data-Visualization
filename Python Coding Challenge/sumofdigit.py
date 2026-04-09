# Input number
num = input("Enter number: ")

# Sum of digits
total = 0
for digit in num:
    total += int(digit)

# Output
print("Sum =", total)