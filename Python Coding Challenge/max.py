# Input list
nums = list(map(int, input("Enter numbers: ").split()))

# Find max without built-in
max_val = nums[0]

for i in nums:
    if i > max_val:
        max_val = i

# Output
print("Max =", max_val)