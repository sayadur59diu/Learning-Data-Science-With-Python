#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This function is used to find the trigonometric value of theta
def fun_theta_value(x,y): # here x=sin,cos,tan,sini,cosi,tani and y=integer number. example fun_theta_converter('sin',4)
    import numpy as np
    if isinstance(y,int):
        if x=='sin':
            values=np.sin(y)
        elif x=='cos':
            values=np.cos(y)
        elif x=='tan':
            values=np.tan(y)
        elif x=='sini':
            values=np.arcsin(y)
        elif x=='cosi':
            values=np.arccos(y)
        elif x=='tani':
            values=np.arctan(y)
        else:
            values='Undefined function'
        
    else:
        values='Wrong values you have entered!'
    
    return values
#fun_theta_converter('tani',56)


# In[ ]:




