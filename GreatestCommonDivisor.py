#!/usr/bin/env python
# coding: utf-8

# In[1]:


def maghsoom_alaih(x):
    myList = []
    for i in range(1,x+1):
        if x % i == 0:
            myList.append(i)
    return myList

def GCD(x,y):
    maghsoom = []
    for i in maghsoom_alaih(x):
        for j in maghsoom_alaih(y):
            if i == j:
                maghsoom.append(i)
    print("The Greatest Common Divisor is: " , max(maghsoom))

num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))
GCD(num1,num2)


# In[ ]:




