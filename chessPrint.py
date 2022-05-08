#!/usr/bin/env python
# coding: utf-8

# In[12]:


def chess(n,m):
    for i in range(n):
        for j in range(m):
            if (i+j)%2==0:
                print('*',end='')
            else:
                print('#',end='')
        print('')

num1=int(input('enter number of n:'))
num2=int(input('enter number of m:'))
chess(num1,num2)


# In[ ]:




