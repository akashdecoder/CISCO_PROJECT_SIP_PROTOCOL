#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[9]:


df = pd.read_csv('C:/Users/raksh/OneDrive/Documents/sip.csv')


# In[10]:


df.head()


# In[11]:


df.shape


# In[12]:


df[df['Protocol']=='SIP'].head()


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')
df[df['Protocol']=='SIP'].Length.hist(bins=15)


# In[ ]:




