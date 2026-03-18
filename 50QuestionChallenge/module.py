# mymodule.py

# Q1: Discount
def discount(price, per):
    return price - (price * per / 100)

# Q2: Even/Odd
def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

# Q3: Electricity Bill
def bill(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return (100 * 5) + (units - 100) * 7
    else:
        return (100 * 5) + (100 * 7) + (units - 200) * 10

# Q4: Even Numbers List
def even_numbers(n):
    result = []
    for i in range(2, n+1, 2):
        result.append(i)
    return result

# Q5: Simple Interest
def simple_interest(p, r, t):
    return (p * r * t) / 100