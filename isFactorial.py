#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math
def isFactorial(n):
    flag=0
    for i in range(n):
        if math.factorial(i)==n:
            flag=1
            break
    if flag==1:
        print('Yes is factorial')
    else:
        print('No is not factorial')
        
number=int(input('enter a number:'))
isFactorial(number)


# In[ ]:




