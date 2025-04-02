# loops are used to repeat a block of code multiple times.
# there are two primary types of loops = [1] while loops and for loops.
# nesting is putting a block of code inside another block of code..reseach on nesting??

# for loop is used to iterate over a sequence (list, tuples,dict,string or range).

# syntax:
# for variable in sequence:
   # statements


# fruits = ['a','b','c']
# for fruit in fruits:
#     print(fruit)

# text = 'python'
# for char in text:
#     print(char)

## functions and parametersp;

# parameter allows function to call an input.
# function is a block of code that calls a specific design
# why do we need function??

# reduce code duplication.
# organazational of code/data.
# easy for you to debug the code.

# syntax..??
# def ..function_name(parameters)
  # function body..(print)
#function must rerturn a value.

# function without a parameter...
# def greet():
#     print('hello,welcome to uncommon!')
# greet()

# function with one parameter
    
# def greet(name):
#     print(f'hello,{name}!')
# greet('blessing')
# greet('kusiwani')

#function with multiple parameters and operators
    
# def add(a,b):
#     return a + b
# result = add(2,3)
# print(result)

# def add(a = 2, b = 3):
#     return a + b
# result = add()
# print(result)


# for even in range(1,51):
#     if even % 5 == 0:
#         continue
#     print(even)

# for even in range(1,21,):
#     if even % 2 == 0:
#      continue
#     print(even)

# arguments are assigned in their order

# def power(base,exponent):
#     return base ** exponent
# print (power(2,3))


# key word argument...
# default arguments

# def greet(name='guest'):
#     print(f'hello, {name}!')
# greet()

# def multiply(a,b):
#     return a*b
# result =multiply(5,7)
# print(result)

# print(multiply(5,7))

# nested functions

# def outer():
#     print('this is outer function')
#     def inner():
#         print('this is inner function')
#     inner()
# outer()

# def outer():
#     print('this is outer fuction')
#     def inner():
#         print('this is inner function')
#     outer() 
#     inner()
# outer()

# def global_function():
#     print('this is a global function')
# global_function()

# def another_function():
#     global_function()
# another_function()


