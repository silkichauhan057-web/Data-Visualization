n = int(input("Enter number of persons: "))

for i in range(n):
    age = int(input("Enter age: "))
    
    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")