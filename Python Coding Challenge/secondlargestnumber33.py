# Find second largest element

nums = list(map(int, input("Enter numbers: ").split()))

largest = second = -999999

for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("Second Largest =", second)