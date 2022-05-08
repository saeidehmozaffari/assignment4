#!/usr/bin/env python
# coding: utf-8

# In[11]:


def MultiplicationTable(n,m):
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(i*j,end=' ')
            if j==5:
                print()
    
num1=int(input('enter number of n:'))
num2=int(input('enter number of m:'))

MultiplicationTable(num1,num2)


# In[ ]:




