def vote_rec(n):
    if n == 0:
        return
    
    age = int(input("Enter age: "))
    
    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")
    
    vote_rec(n-1)

n = int(input("Enter number of persons: "))
vote_rec(n)