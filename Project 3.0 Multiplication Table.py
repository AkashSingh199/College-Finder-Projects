#!/usr/bin/env python
# coding: utf-8

# # Project 3 - Multiplication Tables

# In[3]:


#Using For Loop


# In[8]:


print("."*20,"Multiplication Table","."*20)
Number = int(input("Enter a Number : "))
print("Multiplication Table of {}".format(Number))

for i in range(1,13):
    print(Number,"x",i,"=",Number*i)


# In[2]:


#Using While


# In[9]:


print("."*20,"Multiplication Table","."*20)
number = int(input("Enter the Number : "))
print("Multiplication Table of {}".format(number))
i=1
while (i<=12):
    print(number,"x",i,"=",number*i)
    
    i=i + 1

