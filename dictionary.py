#Task 1: Create a Dictionary of Student Marks

data={'Alice':30,'sakish':70,'nutrelle':40,'priwish':60}
print(data)

name=input("Enter the student's name: ")

if name in data:
    print(name+"'s marks : ",data[name])
else:
    print("student not found in data")