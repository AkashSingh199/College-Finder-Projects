#!/usr/bin/env python
# coding: utf-8

# # College Finder Student Portfolio Project

# In[1]:


print("Student Information")
print("...........................")
Name = str(input("Enter your Name : "))
School_Name = str(input("School Name : "))
Standard = int(input("Enter your Standard : "))
Division  = str(input("Division : "))
Rollnumber = int(input("Roll no. : "))
English_Marks = int(input("English Marks : "))
Maths_Marks = int(input("Maths Marks : "))
Accountancy_Marks = int(input("Accountancy Marks : "))
Percentage = ((English_Marks + Maths_Marks + Accountancy_Marks)/300)*100
print("Percentage",Percentage)

