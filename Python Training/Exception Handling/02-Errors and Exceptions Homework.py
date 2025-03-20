#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # Errors and Exceptions Homework

# ### Problem 1
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks.

# In[1]:


for i in ['a','b','c']:
    try:
        print(i**2)
    except :
        print("unsupported operand types")


# ### Problem 2
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks. Then use a <code>finally</code> block to print 'All Done.'

# In[3]:


x = 5
y = 0
try:
    z = x/y
except:
    print("ZerorDivisionError")
finally:
    print("All Done")


# ### Problem 3
# Write a function that asks for an integer and prints the square of it. Use a <code>while</code> loop with a <code>try</code>, <code>except</code>, <code>else</code> block to account for incorrect inputs.

# In[8]:


def ask():
    while(1):
        try:
            a = int(input("Enter int number"))   
        except:
            print("You must input a integer")
            continue
        else: 
            print("Correct int", a*a)
            break
        finally:
            print("Done")
            


# In[9]:


ask()


# # Great Job!
