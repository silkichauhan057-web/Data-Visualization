def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

x = int(input("Enter number: "))
print(even_odd(x))