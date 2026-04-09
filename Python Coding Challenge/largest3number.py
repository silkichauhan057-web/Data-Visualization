a, b, c = map(int, input("Enter 3 numbers: ").split())

# Logic
if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)