#Exercises 1
import os
def list_items(path):
    print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("All Items:", os.listdir(path))
path = "." 
list_items(path)


#Exercises 2
import os
def check_access(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))
path = "test.txt"  
check_access(path)


#Exercises 3
import os
def check_path(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist.")
path = "example.txt" 
check_path(path)


#Exercises 4
def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)
filename = "example.txt" 
print("Number of lines:", count_lines(filename))


#Exercises 5
def write_list_to_file(filename, lst):
    with open(filename, 'w') as file:
        file.writelines("\n".join(lst))

items = ["Mers", "Bmw", "Passat"]
write_list_to_file("fruits.txt", items)


#Exercises 6
import string
for letter in string.ascii_uppercase:  
    with open(f"{letter}.txt", 'w') as file:
        file.write(f"This is {letter}.txt")



#Exercises 7
def copy_file(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        dest.write(src.read())

copy_file("source.txt", "destination.txt")


#Exercises 8
import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File '{path}' deleted successfully.")
        else:
            print("No write permission to delete the file.")
    else:
        print("File does not exist.")

delete_file("test.txt") 








