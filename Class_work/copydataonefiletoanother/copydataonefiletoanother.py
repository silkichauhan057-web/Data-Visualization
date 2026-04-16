# Program to copy data from one file to another

# Open source file in read mode
with open("source.txt", "r") as source:
    
    # Open destination file in write mode
    with open("destination.txt", "w") as destination:
        
        # Copy content
        destination.write(source.read())

print("Data copied successfully")
