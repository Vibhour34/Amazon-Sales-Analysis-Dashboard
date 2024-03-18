#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv("Amazon Sale Report.csv")


# In[3]:


df.shape


# In[4]:


df.head()


# In[6]:


df.tail(10)


# # Data Cleaning

# In[7]:


df.info()


# # # Remove useless columns from table

# In[8]:


df.drop(["New","PendingS"], axis=1,inplace=True)


# In[9]:


df.info()


# In[10]:


pd.isnull(df)


# In[12]:


pd.isnull(df).sum()


# # # Drop null values

# In[13]:


df.dropna(inplace=True)


# In[14]:


pd.isnull(df).sum()


# In[15]:


df.columns


# In[16]:


df.info()


# # # Column datatype changing

# In[17]:


df["ship-postal-code"] = df["ship-postal-code"].astype("int")


# In[23]:


df["Date"]=pd.to_datetime(df["Date"],format="%m-%d-%y")


# # # Column rename

# In[24]:


df.rename(columns={"Qty":"Quantity"},inplace=True)


# In[25]:


df.rename(columns={"Category":"Product Name"},inplace=True)


# In[26]:


df.info()


# In[27]:


df["Amount"].describe()


# In[28]:


df.head()


# In[29]:


df.dtypes


# In[30]:


df.head()


# In[31]:


df.to_csv('Amazon_Sales_Data.csv', index=False)


# In[ ]:





# In[ ]:




