# Count occurrence of a character

text = input("Enter string: ")
ch = input("Enter character: ")

count = 0
for i in text:
    if i == ch:
        count += 1

print("Count =", count)