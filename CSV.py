#!/usr/bin/env python
# coding: utf-8

# In[1]:


l=()
print(l)


# In[2]:


print(type(l))


# In[5]:


l=[]
print(type(l))


# In[6]:


p=[1,2,3,4,5,6,6,6,6,6,7,8,8,9,9]
p[:4]


# In[7]:


p[-1]


# In[8]:


p[-5]


# In[9]:


p.append(45)


# In[10]:


print(p)


# In[11]:


p.insert(4,456)
print(p)


# In[12]:


p.remove(6)
print(p)


# In[14]:


p.remove(45)
print(p)


# In[15]:


p.pop()
print(p)


# In[17]:


p.pop(0)
print(p)


# In[19]:


k=[12,45,456,789,123,456]
del k[2]


# In[20]:


print(k)


# In[21]:


i=k.copy()
print(i)


# In[22]:


j=i+k
print(j)


# In[24]:


num=[12,45,789,89,75]
num2=[14,78,98,56,58,14]
num.extend(num2)


# In[25]:


print(num)


# In[27]:


num.count(num)


# In[28]:


print(len(num))


# In[29]:


num.reverse()
print(num)


# In[30]:


num.sort()


# In[31]:


print(num)


# In[32]:


num.sort(reverse= True)


# In[33]:


print(num)


# In[34]:


g=[1,2,3,2,5]
g.remove(2)
print(g)


# In[ ]:




