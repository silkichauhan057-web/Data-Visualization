# Convert to uppercase without built-in

text = input("Enter string: ")

result = ""
for ch in text:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)