#!/usr/bin/env python
# coding: utf-8

# a=30
# b=45
# if a>=b:
#  retrun a
# else 
# retrun b

# In[36]:


a=30
b=45
def maximum(a,b):
    
    if a >= b:
        return a
    else:
        return b
        
print(maximum(a,b))        


# In[37]:


a=45
b=35
maximum=max(a,b)
print(maximum)


# In[40]:


a=-188.4
b=-100.5
print(a if a >= b else b)


# In[42]:


a=145
b=188
print(id(a))
print(id(b))


# In[44]:


a=18763
b=216338
addition=(a+b)
print(addition)


# In[ ]:




