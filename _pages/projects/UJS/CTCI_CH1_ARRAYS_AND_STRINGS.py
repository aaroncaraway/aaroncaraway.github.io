#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # 1.1 isUnique()

# In[20]:


# No additional data structure
def isUnique(string):
    for i,s in enumerate(string):
        for j,ss in enumerate(string):
            if i!=j:
                if string[i] == string[j]:
                    return False
    return True
            


# In[21]:


isUnique('abcde')


# In[22]:


isUnique('aaa')


# In[23]:


# with additional data structure
def isUnique(string):
    if len(string) > 128:
        return False
    
    char_set = [False for _ in range(128)]
    for s in string:
        idx = ord(s)
        if char_set[idx]:
            return False
        
        char_set[idx] = True
    return True


# In[24]:


isUnique('abc')


# In[25]:


isUnique('aaa')


# In[30]:


def isPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    letters = [0 for _ in range(128)]
    for s in str1:
        letters[ord(s)] += 1
    
    for s in str2:
        letters[ord(s)] -= 1
        if letters[ord(s)] < 0:
            return False
    
    return True
        


# In[31]:


isPermutation('tacocat', 'cattaco')


# In[33]:


isPermutation('tacocat', 'cattttt')


# In[ ]:




