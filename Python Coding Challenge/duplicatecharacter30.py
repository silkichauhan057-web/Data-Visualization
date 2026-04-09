# Find duplicate characters

text = input("Enter string: ")

duplicates = set()

for ch in text:
    if text.count(ch) > 1:
        duplicates.add(ch)

print("Duplicates:", *duplicates)