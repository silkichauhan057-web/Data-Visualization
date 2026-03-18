units = int(input("Enter units: "))

bill = sum([5 for i in range(min(units, 100))]) + \
       sum([7 for i in range(max(0, min(units-100, 100)))]) + \
       sum([10 for i in range(max(0, units-200))])

print("Total Bill:", bill)