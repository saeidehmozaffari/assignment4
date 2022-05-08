#!/usr/bin/env python
# coding: utf-8

# In[5]:


def mazrab_moshtarak(x):
    mylist = []
    for i in range(1,100):
        mylist.append(x * i)
    return mylist

def lowestCommonDivisor(x,y):
    mazrab = []
    for i in mazrab_moshtarak(x):
        for j in mazrab_moshtarak(y):
            if i == j:
                mazrab.append(i)
    print("The lowest common divisor is " , min(mazrab))

num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))
lowestCommonDivisor(num1,num2)


# In[ ]:




