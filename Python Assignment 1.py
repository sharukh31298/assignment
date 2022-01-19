#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
for i in range(2000,3201):
    if ((i%5!=0) & (i%7==0)):
        print(i)


# In[2]:


#2
first=input("fisrt name: ")


# In[3]:


last= input("last name: ")


# In[9]:


Name =first+" "+ last


# In[35]:


Name[::-1]


# In[37]:


x=[]
for i in Name:
    x.append(i)
x.reverse()
x


# In[ ]:


#3
diameter = 12
radius = diameter/2

import numpy as np
y=np.square(radius)
x=np.pi

Volume = 4/3 * x *y
Volume

