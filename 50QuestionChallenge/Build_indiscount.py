price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))

final = price - (price * discount / 100)
print("Final Price:", final)