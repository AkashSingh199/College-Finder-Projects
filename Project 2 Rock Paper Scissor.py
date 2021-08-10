#!/usr/bin/env python
# coding: utf-8

# # Project 2.0 - Rock Paper Scissor

# In[8]:


print("Lets Play Rock Paper Scissor")
Player1_Name = str(input("Enter your name : "))
Player2_Name = str(input("Enter your name : "))

print("."*30)

Person1 = str(input("Choose Rock Paper Scissor : "))
Person2 = str(input("Choose Rock Paper Scissor : "))

print("."*30)


if (Person1 == "Rock"):
    if(Person2 == "Paper"):
        print("{Player1} is the winner".format(Player1=Player1_Name))
    elif (Person2 == "Scissor"):
        print("{Player1} is the Winner".format(Player1=Player1_Name))
    else:
        print("The match is tie")
        
elif (Person1 == "Paper"):
    if(Person2 == "Rock"):
        print("{Player2} is the Winner".format(Player2=Player2_Name))
    elif(Person2 == "Scissor"):
        print("{Player2} is the Winner".format(Player2=Player2_Name))
    else:
        print("The match is tie")
        
else:
    if (Person1 == "Scissor") and (Person2 == "Paper"):
        print("{Player2} is the winner".format(Player2=Player2_Name))
    elif (Person1 == "Scissor") and (Person2 == "Rock"):
        print("{Player2} is the Winner".format(Player2=Player2_Name))
    else:
        print("The match is tie")


        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




