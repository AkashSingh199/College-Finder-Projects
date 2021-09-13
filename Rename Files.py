#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os

def renamer():
    i = 0 # initiate/iterate over files or lists
    path = "D:\\25.02.2019 Sadi Photo Boy Said\\"
    for filename in os.listdir(path):
        names = f"Shadi {i}.jpg"
        src = path + filename
        dest = path + names
        
        os.rename(src,dest)
        i = i + 1
    
if __name__ == "__main__":
    renamer()


# In[2]:





# In[ ]:




