# Input list
nums = list(map(int, input("Enter numbers: ").split()))

# Count numbers greater than 50
count = 0
for i in nums:
    if i > 50:
        count += 1

# Output
print("Count =", count)