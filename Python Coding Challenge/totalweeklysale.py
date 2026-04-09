# Input list of weekly sales
sales = list(map(int, input("Enter 7 days sales: ").split()))

# Calculate total
total = sum(sales)

# Output
print("Total Sales =", total)