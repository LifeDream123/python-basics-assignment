#Task 1: Create a Dictionary of Student Marks

data={'Alice':30,'sakish':70,'nutrelle':40,'priwish':60}
print(data)

name=input("Enter the student's name: ")

if name in data:
    print(name+"'s marks : ",data[name])
else:
    print("student not found in data")


#Task 2: Demonstrate List Slicing 

mylist=[1,2,3,4,5,6,7,8,9,10]
print("Origina list :",mylist)
extrat_list=mylist[:5]
reverse_list=extrat_list[::-1]
print("Exytracted First Five Elements:",extrat_list)
print("Reversed of Extracted First Five Element:",reverse_list)




