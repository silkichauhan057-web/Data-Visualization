def bill(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return (100 * 5) + (units - 100) * 7
    else:
        return (100 * 5) + (100 * 7) + (units - 200) * 10

u = int(input("Enter units: "))
print("Total Bill:", bill(u))

# ------------------------output
# Enter units: 40
# Total Bill: 200