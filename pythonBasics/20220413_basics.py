# Script Begins
print("GeeksQuiz")
# Scripts Ends

# Python code for "Hello World"
# nothing else to type...see how simple is the syntax.
print("Hello World")      

# Python program to declare variables
myNumber = 3
print(myNumber)
  
myNumber2 = 4.5
print(myNumber2)
  
myNumber ="helloworld"
print(myNumber)


# Python Program to illustrate a list 
 
# creates a empty list
nums = [] 
  
# appending data in list
nums.append(21)
nums.append(40.5)
nums.append("String")
  
print(nums)

# is used for single line comment in Python
""" this is a comment """ 
#is used for multi line comments

# Python program to illustrate
# getting input from user
name = input("Enter your name: ") 
  
# user entered the name 'harssh'
print("hello", name)


# Python3 program to get input from user
  
# accepting integer from the user
# the return type of input() function is string ,
# so we need to convert the input to integer
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
  
num3 = num1 * num2
print("Product is: ", num3)


# Python program to illustrate
# selection statement
  
num1 = 34
if(num1>12):
    print("Num1 is good")
elif(num1>35):
    print("Num2 is not gooooo....")
else:
    print("Num2 is great")

"""
Structure of IFs

if(statement):
	action
elif(statement):
	action
else:
	action
"""

"""
Functions: You can think of functions like a bunch of code that is intended 
to do a particular task in the whole Python script. 
Python used the keyword ‘def’ to define a function.
"""

# Python program to illustrate
# functions
def hello():
    print("hello")
    print("hello again")
  
# calling function
hello()     


# Python program to illustrate
# a simple for loop
  
for step in range(5):    
    print(step)