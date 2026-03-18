discount = lambda price, per: price - (price * per / 100)

p = float(input("Enter price: "))
d = float(input("Enter discount %: "))

print("Final Price:", discount(p, d))