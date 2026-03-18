def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

# Input
p = float(input("Enter Principal (P): "))
r = float(input("Enter Rate (R): "))
t = float(input("Enter Time (T): "))

# Function call
result = simple_interest(p, r, t)

print("Simple Interest:", result)


# ---------------------output
# Enter Principal (P): 5000
# Enter Rate (R): 3
# Enter Time (T): 50
# Simple Interest: 7500.0