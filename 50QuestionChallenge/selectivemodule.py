# mymodule.py

def discount(price, per):
    return price - (price * per / 100)

def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def bill(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return (100 * 5) + (units - 100) * 7
    else:
        return (100 * 5) + (100 * 7) + (units - 200) * 10

def even_numbers(n):
    return [i for i in range(2, n+1, 2)]

def simple_interest(p, r, t):
    return (p * r * t) / 100