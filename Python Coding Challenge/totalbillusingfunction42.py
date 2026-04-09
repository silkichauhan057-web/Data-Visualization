# Total bill using function

def total_bill(items):
    return sum(items)

items = list(map(int, input("Enter values: ").split()))
print(total_bill(items))