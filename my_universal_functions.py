#!/usr/bin/env python
# coding: utf-8

# In[1]:


def checIfNotNumeric(L):    
    for x in L:
        if not(isinstance(x,(int,float))):
            return False
    return True 

def myAddUniversal(*args):
    s=0
    for i in range(len(args)):
        s+=args[i]
    return s
myName="Python Course"


# In[ ]:




