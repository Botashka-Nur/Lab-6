#Python File Open
#Example
f = open("demofile.txt", "r")
print(f.read())


#Open a file on a different location:
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())


#Read Only Parts of the File
f = open("demofile.txt", "r")
print(f.read(5))


#Read Lines
f = open("demofile.txt", "r")
print(f.readline())
#Read two lines of the file:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())


#Loop through the file line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)


#Close Files
f = open("demofile.txt", "r")
print(f.readline())
f.close()


