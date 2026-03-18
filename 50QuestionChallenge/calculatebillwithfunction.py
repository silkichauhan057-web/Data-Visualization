def discount(price, per):
    return price - (price * per / 100)

p = float(input("Enter price: "))
d = float(input("Enter discount %: "))

print("Final Price:", discount(p, d))
# -----------------------output
# Enter price: 5000
# Enter discount %: 20
# Final Price: 4000.0