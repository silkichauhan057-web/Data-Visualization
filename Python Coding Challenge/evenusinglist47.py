# Even numbers using list comprehension

def get_even(nums):
    return [i for i in nums if i % 2 == 0]

nums = list(map(int, input("Enter numbers: ").split()))
print(get_even(nums))