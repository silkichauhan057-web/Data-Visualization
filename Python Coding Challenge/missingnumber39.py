# Find missing number in sequence

nums = list(map(int, input("Enter numbers: ").split()))

n = max(nums)

expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

print("Missing number =", expected_sum - actual_sum)