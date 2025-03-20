#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # Object Oriented Programming
# ## Homework Assignment
# 
# #### Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

# In[3]:


class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        print(((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2) **0.5)
     
    
    def slope(self):
        print(((self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[1])))
        


# In[ ]:





# In[4]:


# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)


# In[5]:


li.distance()


# In[3]:


li.distance()


# In[6]:


li.slope()


# ________
# #### Problem 2

# Fill in the class 

# In[11]:


class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
       
        
    def volume(self):
        return 3.14 * self.radius ** 2 * self.height
        
    
    def surface_area(self):
        pass


# In[13]:


# EXAMPLE OUTPUT
c = Cylinder(2,3)


# In[14]:


c.volume()


# In[8]:


c.surface_area()

