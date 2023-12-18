#!/usr/bin/env python
# coding: utf-8

# In[1]:


#string functions
#capitalize(converts first character to upper case)
message="hello and welcome to code"
x=message.capitalize()
print(x)


# In[3]:


#casefold(converts string to lower case)
message="HELLO AND WELCOME TO CODE"
x=message.casefold()
print(x)


# In[5]:


#center (returns a centered string)
fruit = 'mango'
x = fruit.center(30)
print(x)


# In[1]:


#count(returns the number of times a specified value occurs in string)
msg='I love music,listening to music is my hobbie'
x=msg.count('music')
print(x)


# In[2]:


#encode(returns an encoded version of string)
text='My name is kalyani'
x=text.encode()
print(x)


# In[3]:


#endswith (returns true if the string ends with the specified value )
text='Hello,welcome to my world.'
x=text.endswith('.')
print(x)


# In[5]:


#find(searches the string for specified value)
text='Hello, welcome to my world.'
x=text.find('welcome')
print(x)


# In[6]:


#index(searches string for specified value)
text='hello, welcome to my world.'
x=text.index('welcome')
print(x)


# In[7]:


#isalnum(returns true if all characters in string are alphanumeric)
text = 'Company12'
x=text.isalnum()
print(x)


# In[8]:


#isdigit(returns True if all characters in string are digits)
text='89076'
x=text.isdigit()
print(x)


# In[9]:


#islower(returns true if all characters are in lowercase)
text='HELLO WORLD'
x=text.islower()
print(x)


# In[10]:


#isupper(returns true if all characters are in upper)
text ='hello world'
x=text.isupper()
print(x)


# In[11]:


#rsplit(splits the string at specified separator)
text='appple,mango,cherry'
x=text.rsplit(',')
print(x)


# In[ ]:




