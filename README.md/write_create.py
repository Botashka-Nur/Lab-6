#Python File Write
#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content

#Example
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())


#Create a New File
#"x" - Create - will create a file, returns an error if the file exists
#"a" - Append - will create a file if the specified file does not exists
#"w" - Write - will create a file if the specified file does not exists

#Example 1
f = open("myfile.txt", "x")

#Example 2
f = open("myfile.txt", "w")


