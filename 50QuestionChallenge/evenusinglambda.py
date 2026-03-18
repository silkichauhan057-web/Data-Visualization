even_list = lambda n: [i for i in range(2, n+1, 2)]

n = int(input("Enter N: "))
print("Even Numbers:", even_list(n))