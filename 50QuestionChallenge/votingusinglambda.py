vote = lambda age: "Eligible" if age >= 18 else "Not Eligible"

age = int(input("Enter age: "))
print(vote(age))