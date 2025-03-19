#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # Object Oriented Programming Challenge
# 
# For this challenge, create a bank account class that has two attributes:
# 
# * owner
# * balance
# 
# and two methods:
# 
# * deposit
# * withdraw
# 
# As an added requirement, withdrawals may not exceed the available balance.
# 
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

# In[40]:


class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return f"Deposit Accepted, Balance: {self.balance}"

    def withdraw(self,amount):
        if self.balance - amount > 0:
            self.balance -= amount
            return f"Withdraw Accepted, Balance: {self.balance}"
        else:
            return f"Exceed the Balance now"
    
    def __str__(self):
        return f"Account Owner: {self.owner}\nAccount Balance: {self.balance}"


# In[41]:


# 1. Instantiate the class
acct1 = Account('Jose',100)


# In[33]:


# 2. Print the object
print(acct1)


# In[34]:


# 3. Show the account owner attribute
acct1.owner


# In[35]:


# 4. Show the account balance attribute
acct1.balance


# In[36]:


# 5. Make a series of deposits and withdrawals
acct1.deposit(50)


# In[37]:


acct1.withdraw(75)


# In[38]:


# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)


# In[ ]:


## Good job!

## Great
# In[ ]:




