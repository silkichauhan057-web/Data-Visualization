year = int(input("Enter year: "))

# Logic
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# ======================
# Enter year: 2026
# Not Leap Year    