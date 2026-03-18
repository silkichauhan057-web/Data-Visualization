def even_rec(i, n):
    if i > n:
        return
    
    if i % 2 == 0:
        print(i, end=" ")
    
    even_rec(i+1, n)

n = int(input("Enter N: "))
even_rec(1, n)