#!/usr/bin/env python
# coding: utf-8

# # Real Calculator

# In[ ]:


# Without watching the Video


# In[9]:


number1 = int(input("Enter your number:  "))
operation = str(input("+,-,/,*:  "))
number2 = int(input("Enter your number: "))

print("."*20)

if operation=="+":
    add = number1 + number2
    print("Addtion of {number1} and {number2} is".format(number1=number1,number2=number2),add)
    
elif operation=="-":
    subs = number1 - number2
    print("Substraction of {number1} and {number2} is".format(number1=number1,number2=number2),subs)

elif operation=="/":
    divd = number1/number2
    print("Division of {number1} and {number2} is".format(number1=number1,number2=number2),divd)
    
elif operation=="*":
    multi = number1 * number2
    print("Multipication of {number1} and {number2} is".format(number1=number1,number2=number2),multi)
        


# In[ ]:


# After watching the Video


# In[10]:


def add(a,b):
    addtion = a + b
    print("Addition of {a} and {b} is".format(a=number1,b=number2),addtion)
    
def substract(a,b):
    subs = a - b
    print("Substract of {a} and {b} is".format(a=number1,b=number2),subs)
    
def multiply(a,b):
    multi = a * b
    print("Multiplication of {a} and {b} is".format(a=number1,b=number2),multi)
    
def divide(a,b):
    divide = a / b
    print("Division of {a} and {b} is".format(a=number1,b=number2),divide)
    
number1,operator,number2 = map(str, input("Enter your equation: ").split())
number1 = int(number1)
number2 = int(number2)

print("."*30)

if operator == "+":
    add(number1,number2)
    
elif operator == "-":
    subtract(number1,number2)
    
elif operator == "*":
    multiply(number1,number2)
    
elif operator == "/":
    divide(number1,number2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# 

