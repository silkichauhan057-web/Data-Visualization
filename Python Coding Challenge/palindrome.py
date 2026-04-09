# Input number
num = input("Enter number: ")

# Check palindrome
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# ======================
# Enter number: 22
# Palindrome  

# ---------------
# Enter number: 23
# Not Palindrome