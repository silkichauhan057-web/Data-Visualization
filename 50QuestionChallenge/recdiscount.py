def discount_rec(n):
    if n == 0:
        return
    
    price = float(input("Enter price: "))
    per = float(input("Enter discount %: "))
    
    final = price - (price * per / 100)
    print("Final Price:", final)
    
    discount_rec(n-1)

n = int(input("Enter number of customers: "))
discount_rec(n)