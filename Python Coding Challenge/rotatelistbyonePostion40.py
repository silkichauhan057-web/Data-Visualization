# Rotate list by one position

nums = list(map(int, input("Enter numbers: ").split()))

rotated = [nums[-1]] + nums[:-1]

print(rotated)