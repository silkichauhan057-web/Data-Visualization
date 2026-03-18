n = int(input("Enter number of customers: "))

for i in range(n):
    print("\nCustomer", i+1)
    price = float(input("Enter price: "))
    discount = float(input("Enter discount %: "))

    final = price - (price * discount / 100)
    print("Final Price:", final)