# Program to extract students with marks > 75

with open("student.txt", "r") as source:
    with open("output.txt", "w") as destination:
        
        for line in source:
            data = line.split()   # split into name, marks, city
            
            name = data[0]
            marks = int(data[1])
            city = data[2]
            
            # Check condition
            if marks > 75:
                destination.write(line)

print("Data extracted successfully")