# Count unique elements

nums = list(map(int, input("Enter numbers: ").split()))

unique = []

for i in nums:
    if i not in unique:
        unique.append(i)

print("Unique count =", len(unique))