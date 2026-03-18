bill = lambda u: u*5 if u<=100 else (100*5 + (u-100)*7 if u<=200 else (100*5 + 100*7 + (u-200)*10))

units = int(input("Enter units: "))
print("Total Bill:", bill(units))