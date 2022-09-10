#!/usr/bin/env python
# coding: utf-8

# ***************************************************************************************************************************
# 1

# In[1]:


import pandas as pd
import numpy as np
data={'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']}


# In[2]:


df=pd.DataFrame(data)
df


# In[3]:


df.loc[1,['FlightNumber']]=df.loc[0,['FlightNumber']]+10
df.loc[3,['FlightNumber']]=df.loc[1,['FlightNumber']]+20
df['FlightNumber'].astype('int64').dtypes


# In[4]:


df


# ***************************************************************************************************************************
# 2

# In[5]:


df['From_To']=df['From_To'].astype('str')
d=[]
for i in df['From_To']:
    d.append(i.split('_'))


# In[6]:


df1=pd.DataFrame(d,columns=['From','To'])
df1


# ***************************************************************************************************************************
# 3

# In[7]:


from1=[]
for i in df1['From']:
    from1.append(i.capitalize())
df1['From']=from1
to1=[]
for i in df1['To']:
    to1.append(i.capitalize())
df1['To']=to1


# In[8]:


df1


# In[9]:


df


# ***************************************************************************************************************************
# 4

# In[10]:


df['From']=df1['From']
df['To']=df1['To']
df.drop('From_To',axis=1,inplace=True)
df


# ***************************************************************************************************************************
# 5

# In[11]:


x=[i for i in df['RecentDelays']]
z=[]
for i in x:
    if len(i)==2:
        i.append(np.nan)
    elif len(i)==1:
        i.append(np.nan)
        i.append(np.nan)
    elif len(i)==0:
        i.append(np.nan)
        i.append(np.nan)
        i.append(np.nan)
    z.append(i)
df[['delay_1','delay_2','delay_3']]=z
df


# In[12]:


df.drop('RecentDelays',axis=1,inplace=True)


# In[13]:


df


# In[ ]:




