# Frequency using dictionary

nums = list(map(int, input("Enter numbers: ").split()))

freq = {}
for i in nums:
    freq[i] = freq.get(i, 0) + 1

print(freq)