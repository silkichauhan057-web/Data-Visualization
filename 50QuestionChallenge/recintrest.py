def si_rec(n):
    if n == 0:
        return
    
    p = float(input("Enter P: "))
    r = float(input("Enter R: "))
    t = float(input("Enter T: "))
    
    si = (p * r * t) / 100
    print("Simple Interest:", si)
    
    si_rec(n-1)

n = int(input("Enter number of persons: "))
si_rec(n)