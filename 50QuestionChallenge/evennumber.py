
n = int(input("Enter value of N: "))

print("Even numbers are:")

for i in range(1, n+1):
    if i % 2 == 0:
        print(i, end=" ")

# ------------------------output
# Enter value of N: 50
# Even numbers are:
# 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 