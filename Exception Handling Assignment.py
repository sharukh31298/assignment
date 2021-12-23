#!/usr/bin/env python
# coding: utf-8

# In[15]:


#function to compute 5/0

def test(a):
    try:
        x=a/0
        print(x)
    except Exception as e:
        print("Excpetion is ",e)


# In[21]:


test(5)


# In[28]:


subjects=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]


# In[31]:


for i in subjects:
    for j in verbs:
        for k in objects:
            print(i+" "+j+" "+k+".")


# In[ ]:




