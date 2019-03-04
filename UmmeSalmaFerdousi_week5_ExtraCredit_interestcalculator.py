#!/usr/bin/env python
# coding: utf-8

# In[2]:


def interest(p,n,r,i_type):
    if i_type=='si':
        return p*n*r/100
    if i_type=='ci':
        return p*(pow((1+r/100),n)) -p



# In[ ]:




