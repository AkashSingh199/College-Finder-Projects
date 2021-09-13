#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df=pd.read_csv(r'E:\Collage finder\Finance Project/Ecommerce Purchases.csv')


# In[ ]:





# # TOP 10 ROWS 

# In[4]:


df.head(10)


# In[ ]:





# # Last 10 rows of the Data

# In[5]:


df.tail(10)


# In[ ]:





# # Check the data type of the column named "CC Security Code"

# In[8]:


df['CC Security Code'].dtype


# In[ ]:





# # Check if any column contains null values

# In[10]:


df.isnull().sum()


# In[ ]:





# #  Check the number of Rows and Columns in the DataSet

# In[13]:


df.shape


# In[ ]:





# # Check the Highest "Purchase Price" in the DataSet

# In[ ]:





# In[15]:


df['Purchase Price'].describe()


# In[ ]:





# # Display the Lowest "Purchase Price" in the DataSet

# In[ ]:





# In[16]:


df['Purchase Price'].min()


# In[ ]:





# # What is the Average Purchase Price so far?

# In[17]:


df['Purchase Price'].mean()


# In[ ]:





# # How many customers have French as their primary language?

# In[ ]:





# In[29]:


len(df[df['Language']=='fr'].value_counts())


# In[35]:


language=df['Language'].value_counts().reset_index()
language.columns=['Language','No. of Customers']


# In[38]:


import plotly.express as px


# In[42]:


px.bar(data_frame=language,x='Language',y='No. of Customers',template='plotly_dark',color='Language')


# In[ ]:





# # How many of our customers are any kind of Engineer?

# In[ ]:





# In[45]:


len(df[df['Job'].str.contains('engineer',case=False)])


# In[ ]:





# # What is the Email address of the person having IP Address: 24.140.33.94

# In[ ]:





# In[47]:


df[df['IP Address']=='24.140.33.94']['Email']


# In[ ]:





# # How many people have Mastercard as thier credit card provider and made a purchase above 50?

# In[ ]:





# In[51]:


len(df[(df['CC Provider']=='Mastercard') & (df['Purchase Price'] > 50)])


# In[ ]:





# # Find the Email of the person with credit card number: 869968197049750

# In[56]:


df[df['Credit Card']==869968197049750]['Email']


# # How many people use credit cards during the Morning time

# In[60]:


len(df[df['AM or PM']=='AM'])


# # How many people use credit cards during the Night time

# In[61]:


len(df[df['AM or PM']=='PM'])


# In[ ]:





# # Number of people that are having a credit card that will expire in 2020. Also find their Email

# In[ ]:


df[df[]]


# In[73]:


def dates(x):
    return x.split('-')[0]


# In[76]:


df['Expire date']=df['CC Exp Date'].apply(dates)


# In[86]:


df[df['Expire date']=='20']['Email'].head()


# In[ ]:





# # Show the Top 5 email providers

# In[65]:


df["Email"].apply(lambda x: x.split('@')[1]).value_counts().head()


# In[ ]:





# # Print the Top 5 companies having the highest purchase prices

# In[87]:


df[['Company','Purchase Price']].nlargest(5,'Purchase Price').head()


# In[ ]:




