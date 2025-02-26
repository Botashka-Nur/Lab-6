# Input and Output Functions
name = input("Enter your name: ")
print(f"Hello, {name}!")


#Type Conversion Functions
num = "10"
print(int(num) + 5)  # Output: 15


# Math and Numeric Functions
print(abs(-7))   # Output: 7
print(pow(2, 3)) # Output: 8
print(round(3.14159, 2))  # Output: 3.14


#Sequence and Collection Functions
nums = [3, 1, 4, 2]
print(sorted(nums))  # Output: [1, 2, 3, 4]

for i, val in enumerate(nums):
    print(i, val)


#Logical and Comparison Functions
values = [True, True, False]
print(all(values))  # Output: False
print(any(values))  # Output: True


# File Handling Functions
with open("example.txt", "w") as f:
    f.write("Hello, world!")


# Object and Class Functions
print(type(10))  # Output: <class 'int'>


#Miscellaneous Functions
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Output: [1, 4, 9, 16]