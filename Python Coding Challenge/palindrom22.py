# Check palindrome string

text = input("Enter string: ")

if text == text[::-1]:
    print("Yes")
else:
    print("No")