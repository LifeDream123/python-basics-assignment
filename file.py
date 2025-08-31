#Task 1: Read a File and Handle Errors

try:
    filedt= open("sample.txt","r")
    readtext=filedt.read()
    print(readtext)
    filedt.close()
except FileNotFoundError:
    print("The file sample.txt was not found")




#Task2 :  Write and Append Data to a File


file1=open("output.txt","w")
data=input("Enter data to written in file : ")
file1.write(data+"\n")
print("Data written successfully to output.txt ")

file1.close()

file1=open("output.txt","a")
append_data=input("Enter data to append in file : ")
file1.write(append_data+"\n")
print("Data appended successfully to output.txt ")
file1.close()


file2=open("output.txt","r")
print("Final Content of output.txt")
print(file2.read())
file2.close()