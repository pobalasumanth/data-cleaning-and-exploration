#!/usr/bin/env python
# coding: utf-8

# Displaying Number of Anagrams in Words.txt and Dividing them based on the length of characters and finding the length of anagrams according to character length

# In[ ]:


all_anagrams = open('all_anagrams.txt','r')


# In[16]:


all_anagrams


# In[17]:


anaglist = all_anagrams.readlines()


# In[18]:


anaglist[:10]


# In[19]:


len(anaglist)


# In[21]:


#Grouping wordlist based on the length of characters
from collections import defaultdict
d=defaultdict(list)
for word in anaglist:
    d[len(word)].append(word)

anag_res=[d[n] for n in sorted(d, reverse=False)] 
print(result)


# In[27]:


anaglen2 = anag_res[0]
strip_list2 = [item.strip() for item in anaglen2]
strip_list2


# In[48]:


#number of anagrams of character length 2
len(strip_list2)


# In[31]:


#Characters with length 3
anaglen3 = anag_res[1]
strip_list3 = [item.strip() for item in anaglen3]
strip_list3


# 

# In[47]:


#no of chars of length 3
len(strip_list3)


# In[ ]:





# In[34]:


#Characters with length 4
anaglen4 =  anag_res[2]

strip_list4 = [item.strip() for item in anaglen4]
strip_list4


# In[36]:


#number of anagrams of character length 4

len(strip_list4)


# In[86]:


#Characters with length 5
anaglen5 =  anag_res[3]

strip_list5 = [item.strip() for item in anaglen5]
strip_list5


# In[87]:


#number of anagrams of character length 5
len(strip_list5)


# In[45]:


#Characters with length 6
anaglen6 =  anag_res[4]

strip_list6 = [item.strip() for item in anaglen6]
strip_list6


# In[46]:


#number of anagrams of character length 6
len(strip_list6)


# In[49]:


#Characters with length 7
anaglen7 =  anag_res[5]

strip_list7 = [item.strip() for item in anaglen7]
strip_list7


# In[50]:


#number of anagrams of character length 7
len(strip_list7)


# In[51]:


#Characters with length 8
anaglen8 =  anag_res[6]

strip_list8 = [item.strip() for item in anaglen8]
strip_list8


# In[52]:


#number of anagrams of character length 8
len(strip_list8)


# In[53]:


#Characters with length 9
anaglen9 = anag_res[7]

strip_list9 = [item.strip() for item in anaglen9]
strip_list9


# In[54]:


#number of anagrams of character length 9
len(strip_list9)


# In[55]:


#Characters with length 10
anaglen10 = anag_res[8]

strip_list10 = [item.strip() for item in anaglen10]
strip_list10


# In[56]:


#number of anagrams of character length 10
len(strip_list10)


# In[57]:


#Characters with length 11
anaglen11 = anag_res[9]

strip_list11 = [item.strip() for item in anaglen11]
strip_list11


# In[58]:


#number of anagrams of character length 11
len(strip_list11)


# In[59]:


#Characters with length 12
anaglen12 = anag_res[10]

strip_list12 = [item.strip() for item in anaglen12]
strip_list12


# In[60]:


#number of anagrams of character length 12
len(strip_list12)


# In[88]:


#Characters with length 13
anaglen13 = anag_res[11]

strip_list13 = [item.strip() for item in anaglen13]
strip_list13


# In[62]:


#number of anagrams of character length 13
len(strip_list13)


# In[63]:


#Characters with length 14
anaglen14 = anag_res[12]

strip_list14 = [item.strip() for item in anaglen14]
strip_list14


# In[64]:


#number of anagrams of character length 14
len(strip_list14)


# In[65]:


#Characters with length 15
anaglen15 = anag_res[13]

strip_list15 = [item.strip() for item in anaglen15]
strip_list15


# In[66]:


#number of anagrams of character length 15
len(strip_list15)


# In[70]:


#Characters with length 16
anaglen16 = anag_res[14]

strip_list16 = [item.strip() for item in anaglen16]
strip_list16


# In[71]:


#number of anagrams of character length 16
len(strip_list16)


# In[72]:


#Characters with length 17
anaglen17 = anag_res[15]

strip_list17 = [item.strip() for item in anaglen17]
strip_list17


# In[73]:


#number of anagrams of character length 17
len(strip_list17)


# In[74]:


#Characters with length 18
anaglen18 = anag_res[16]

strip_list18 = [item.strip() for item in anaglen18]
strip_list18


# In[75]:


#number of anagrams of character length 18
len(strip_list18)


# In[76]:


#Characters with length 19
anaglen19 = anag_res[17]

strip_list19 = [item.strip() for item in anaglen19]
strip_list19


# In[77]:


#number of anagrams of character length 19
len(strip_list19)


# In[78]:


#Characters with length 20
anaglen20 = anag_res[18]

strip_list20 = [item.strip() for item in anaglen20]
strip_list20


# In[81]:


#number of anagrams of character length 20
len(strip_list20)


# In[82]:


#Characters with length 21
anaglen21 = anag_res[19]

strip_list21 = [item.strip() for item in anaglen21]
strip_list21


# In[83]:


#number of anagrams of character length 21
len(strip_list21)


# In[84]:


#Characters with length 22
anaglen22 = anag_res[20]

strip_list22 = [item.strip() for item in anaglen22]
strip_list22


# In[85]:


#number of anagrams of character length 22
len(strip_list22)


# In[ ]:




