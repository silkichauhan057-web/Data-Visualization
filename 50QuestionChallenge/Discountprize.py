
price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

# Discount amount
discount_amount = (price * discount) / 100

# Final price
final_price = price - discount_amount

print("Final price after discount:", final_price)


#-------------------------------output
# Enter price: 5000
# Enter discount percentage: 30
# Final price after discount: 3500.0