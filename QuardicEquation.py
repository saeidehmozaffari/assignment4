#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math

def QuardicEquation(a,b,c):
    delta=b**2-4*a*c
    if delta < 0:
        print('The equation has no answer!!!')
    elif delta==0:
        x=(-b+math.sqrt(delta))/(2*a)
        print('The root of the equation is equal to ',x)
    else:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        print('The roots of the equation is equal to ',x1,',',x2)

num1=int(input('enter number of a:'))
num2=int(input('enter number of b:'))
num3=int(input('enter number of c:'))

QuardicEquation(num1,num2,num3)


# In[ ]:




