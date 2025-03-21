#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # Function Practice Exercises
# 
# Problems are arranged in increasing difficulty:
# * Warmup - these can be solved using basic comparisons and methods
# * Level 1 - these may involve if/then conditional statements and simple methods
# * Level 2 - these may require iterating over sequences, usually with some kind of loop
# * Challenging - these will take some creativity to solve

# ## WARMUP SECTION:

# #### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
#     lesser_of_two_evens(2,4) --> 2
#     lesser_of_two_evens(2,5) --> 5

# In[9]:


def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a > b: return b
        else: return a
    elif a%2 != 0 or b%2 != 0:
        if a> b: return a
        else: return b
        


# In[7]:


# Check
lesser_of_two_evens(2,4)


# In[10]:


# Check
lesser_of_two_evens(2,5)


# #### ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#     animal_crackers('Levelheaded Llama') --> True
#     animal_crackers('Crazy Kangaroo') --> False

# In[13]:


def animal_crackers(text):
    splited_text = text.split(' ')
    return splited_text[0][0] == splited_text[1][0]
    


# In[14]:


# Check
animal_crackers('Levelheaded Llama')


# In[15]:


# Check
animal_crackers('Crazy Kangaroo')


# #### MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False
# 
#     makes_twenty(20,10) --> True
#     makes_twenty(12,8) --> True
#     makes_twenty(2,3) --> False

# In[18]:


def makes_twenty(n1,n2):
    return n1 == 20 or n2 == 20 or n1+n2 == 20


# In[19]:


# Check
makes_twenty(20,10)


# In[20]:


# Check
makes_twenty(2,3)


# # LEVEL 1 PROBLEMS

# #### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
#      
#     old_macdonald('macdonald') --> MacDonald
#     
# Note: `'macdonald'.capitalize()` returns `'Macdonald'`

# In[27]:


def old_macdonald(name):
    name = name.replace(name[0],name[0].upper())
    name = name.replace(name[3],name[3].upper())
    return name


# In[28]:


# Check
old_macdonald('macdonald')


# #### MASTER YODA: Given a sentence, return a sentence with the words reversed
# 
#     master_yoda('I am home') --> 'home am I'
#     master_yoda('We are ready') --> 'ready are We'
#     
# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:
# 
#     >>> "--".join(['a','b','c'])
#     >>> 'a--b--c'
# 
# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:
# 
#     >>> " ".join(['Hello','world'])
#     >>> "Hello world"

# In[40]:


def master_yoda(text):
    sp_text = text.split(' ')
    sp_text = sp_text[::-1]
    return " ".join(sp_text)


# In[41]:


# Check
master_yoda('I am home')


# In[33]:


# Check
master_yoda('We are ready')


# #### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# 
#     almost_there(90) --> True
#     almost_there(104) --> True
#     almost_there(150) --> False
#     almost_there(209) --> True
#     
# NOTE: `abs(num)` returns the absolute value of a number

# In[44]:


def almost_there(n):
    return  90 <= n <= 110 or 190 <= n <= 210
    


# In[45]:


# Check
almost_there(104)


# In[46]:


# Check
almost_there(150)


# In[47]:


# Check
almost_there(209)


# # LEVEL 2 PROBLEMS

# #### FIND 33: 
# 
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# 
#     has_33([1, 3, 3]) → True
#     has_33([1, 3, 1, 3]) → False
#     has_33([3, 1, 3]) → False

# In[48]:


def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == nums[i]:
            return True
    return False


# In[49]:


# Check
has_33([1, 3, 3])


# In[50]:


# Check
has_33([1, 3, 1, 3])


# In[51]:


# Check
has_33([3, 1, 3])


# #### PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#     paper_doll('Hello') --> 'HHHeeellllllooo'
#     paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

# In[54]:


def paper_doll(text):
    rs = ''
    temp = ''
    for char in text:
        temp = char + char + char
        rs += temp
        temp = ''
    return rs


# In[55]:


# Check
paper_doll('Hello')


# In[56]:


# Check
paper_doll('Mississippi')


# #### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#     blackjack(5,6,7) --> 18
#     blackjack(9,9,9) --> 'BUST'
#     blackjack(9,9,11) --> 19

# In[57]:


def blackjack(a,b,c):
    if a+b+c > 21:
        if a == 11 or b ==11 or c==11: return a+b+c -10
        else: return 'BUST'
    return a+b+c
        


# In[58]:


# Check
blackjack(5,6,7)


# In[59]:


# Check
blackjack(9,9,9)


# In[60]:


# Check
blackjack(9,9,11)


# #### SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
#  
#     summer_69([1, 3, 5]) --> 9
#     summer_69([4, 5, 6, 7, 8, 9]) --> 9
#     summer_69([2, 1, 6, 9, 11]) --> 14

# In[ ]:


def summer_69(arr):
    pass


# In[ ]:


# Check
summer_69([1, 3, 5])


# In[ ]:


# Check
summer_69([4, 5, 6, 7, 8, 9])


# In[ ]:


# Check
summer_69([2, 1, 6, 9, 11])


# # CHALLENGING PROBLEMS

# #### SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# 
#      spy_game([1,2,4,0,0,7,5]) --> True
#      spy_game([1,0,2,4,0,5,7]) --> True
#      spy_game([1,7,2,0,4,5,0]) --> False
# 

# In[62]:


def spy_game(nums):
    spy = [0,0,7]
    for item in nums:
        if item == spy[0]:
            spy.remove(spy[0])
            if spy == []: return True
         
    return False


# In[63]:


# Check
spy_game([1,2,4,0,0,7,5])


# In[64]:


# Check
spy_game([1,0,2,4,0,5,7])


# In[65]:


# Check
spy_game([1,7,2,0,4,5,0])


# #### COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number
#     count_primes(100) --> 25
# 
# By convention, 0 and 1 are not prime.

# In[88]:


def count_primes(num):
    count = 4
    for i in range(2,num+1,1):
        for j in range(2,10,1):
            if(i%j == 0): break
        else:
            count = count+1
    return count
                


# In[89]:


# Check
count_primes(100)


# ### Just for fun:
# #### PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
#     print_big('a')
#     
#     out:   *  
#           * *
#          *****
#          *   *
#          *   *
# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns. <br>For purposes of this exercise, it's ok if your dictionary stops at "E".

# In[ ]:


def print_big(letter):
    dic_alpha = {'a':['  *  ',]}


# In[ ]:


print_big('a')


# ## Great Job!
