def check_even_odd(num):
    if num % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

num = int(input("Enter a number: "))
result = check_even_odd(num)
print(result)
