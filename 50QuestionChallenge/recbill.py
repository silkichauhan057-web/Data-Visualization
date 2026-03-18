def bill_rec(n):
    if n == 0:
        return
    
    units = int(input("Enter units: "))
    
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100*5) + (units-100)*7
    else:
        bill = (100*5) + (100*7) + (units-200)*10
    
    print("Total Bill:", bill)
    
    bill_rec(n-1)

n = int(input("Enter number of users: "))
bill_rec(n)