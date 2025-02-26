#Exercise 1
from functools import reduce
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)
nums = [2, 3, 4, 5]
result = multiply_list(nums)
print(result)


#Exercise 2
def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower
text = "Hello World!"
upper_count, lower_count = count_case(text)
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)


#Exercise 3
def is_palindrome(s):
    return s == s[::-1]
word = "madam"
print(is_palindrome(word))


#Exercise 4
import time
import math
def delayed_sqrt(num, delay):
    time.sleep(delay / 1000) 
    return math.sqrt(num)
num = 25100
delay = 2123 
result = delayed_sqrt(num, delay)
print(f"Square root of {num} after {delay} milliseconds is {result}")


#Exercise 5
def all_true(tup):
    return all(tup)
t = (True, True, True)
print( all_true(t))



