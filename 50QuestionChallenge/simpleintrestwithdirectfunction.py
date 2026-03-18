def simple_interest(p, r, t):
    si = (p * r * t) / 100
    print("Simple Interest:", si)

p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = float(input("Enter T: "))

simple_interest(p, r, t)