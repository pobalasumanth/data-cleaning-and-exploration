#!/usr/bin/env python
# coding: utf-8

# #contains the group of lists where each length of characters are stored in different sublists

# In[3]:


word = open('words.txt','r') #open the file 'words.txt'


# In[4]:


word


# In[5]:


wordlist = word.readlines()#read the lines in word


# In[6]:


wordlist[:10] #show the first 10 items


# In[7]:


len(wordlist) #size of our data


# In[8]:


'Aaron\n'.strip() #strip unwanted characteres


# In[9]:


'Aaron'.lower() #lowercase it


# In[10]:


wordclean = [word.strip().lower() for word in wordlist]
#for each word in our wordlist let's strip '\n' and lowercase ir


# In[11]:


wordclean[:10]


# In[12]:


wordunique = list(set(wordclean))#lets create a list of the set of our wordlist
#in other words a wordlist of unique words


# In[13]:


wordunique


# In[14]:


wordunique.sort()#ascending order


# In[15]:


wordunique[:10]


# In[16]:


wordclean = [word.strip().lower() for word in open('words.txt','r')] #we can do this in one-shot


# In[17]:


wordclean[:10]


# In[18]:


wordclean = sorted(list(set([word.strip().lower() for word in open('words.txt','r')])))


# In[19]:


wordclean[:10]


# In[20]:


sorted('lives') #sort the letters


# In[21]:


sorted('lives') == sorted('elvis')


# In[22]:


sorted('love') == sorted('hate')


# In[23]:


def signature(word):#returns a sorted word by its letters
    return ''.join(sorted(word))


# In[24]:


signature('lives')


# In[25]:


'/'.join(['a','b','c'])


# In[26]:


def anagram(word):#given a word wich has the same order that one of the words in our word-clean list return it
    return [w for w in wordclean if signature(w) == signature(word)]


# In[27]:


anagram('dictionary')#example


# In[28]:


get_ipython().run_line_magic('timeit', "anagram('dictionary')")


# In[29]:


words_bysig = {}

for word in wordclean:
    words_bysig[signature(word)].append(word) #it seems a problem...can you guess it?


# In[30]:


import collections


# In[31]:


words_bysig = collections.defaultdict(list)

for word in wordclean:
    words_bysig[signature(word)].append(word)


# In[32]:


words_bysig


# In[33]:


def anagram_fast(word):
    return words_bysig[signature(word)]


# In[34]:


anagram_fast('dictionary')


# In[35]:


anagrams_all = {word: anagram_fast(word) for word in wordclean if len(anagram_fast(word)) > 1}
#if th word exists in our word-clean list and it's greater (lenght) than 1 return it's anagram 


# In[36]:


len(anagrams_all)


# In[37]:


get_ipython().run_line_magic('timeit', 'anagrams_all = {word: anagram_fast(word) for word in wordclean if len(anagram_fast(word)) > 1}')


# In[38]:


#Grouping wordlist based on the length of characters
from collections import defaultdict
d=defaultdict(list)
for word in wordlist:
    d[len(word)].append(word)

result=[d[n] for n in sorted(d, reverse=False)] 
print(result)


# In[39]:


result[0]


# In[40]:


#creating the list for length 1
len1 = result[0]
strip_list1 = [item.strip() for item in len1]
strip_list1


# In[42]:


len2 = result[1]
len2
strip_list2 = [item.strip() for item in len2]
strip_list2


# In[43]:


len3 =  result[2]
len3
strip_list3 = [item.strip() for item in len3]
strip_list3


# In[44]:


x = 'tetraiodophenolphthalein'
len(x)


# In[45]:


len4 =  result[3]
len4
strip_list4 = [item.strip() for item in len4]
strip_list4


# In[46]:


len5 =  result[4]
len5
strip_list5 = [item.strip() for item in len5]
strip_list5


# In[47]:


len6 =  result[5]

strip_list6 = [item.strip() for item in len6]
strip_list6


# In[48]:


len7 =  result[6]
len7
strip_list7 = [item.strip() for item in len7]
strip_list7


# In[49]:


len7 =  result[6]
len7
strip_list7 = [item.strip() for item in len7]
strip_list7



# In[50]:


len7 =  result[6]
len7
strip_list7 = [item.strip() for item in len7]
strip_list7


# In[51]:


len8 =  result[7]
len8
strip_list8 = [item.strip() for item in len8]
strip_list8


# In[52]:


len9 =  result[8]
len9
strip_list9 = [item.strip() for item in len9]
strip_list9


# In[53]:


len10 =  result[9]
len10
strip_list10 = [item.strip() for item in len10]
strip_list10


# In[54]:


len11 =  result[10]
len11
strip_list11 = [item.strip() for item in len11]
strip_list11


# In[55]:


len12 =  result[11]
len12
strip_list12 = [item.strip() for item in len12]
strip_list12


# In[2]:


len13 =  result[12]
len13
strip_list13 = [item.strip() for item in len13]
strip_list13


# In[57]:


len14 =  result[13]
len14
strip_list14 = [item.strip() for item in len14]
strip_list14


# In[58]:


len15 =  result[14]
len15
strip_list15 = [item.strip() for item in len15]
strip_list15


# In[59]:


len16 =  result[15]
len16
strip_list16 = [item.strip() for item in len16]
strip_list16


# In[60]:



len17 =  result[16]
len17
strip_list17 = [item.strip() for item in len17]
strip_list17


# In[61]:


len18 =  result[17]
len18
strip_list18 = [item.strip() for item in len18]
strip_list18


# In[62]:


len19 =  result[18]
len19
strip_list19 = [item.strip() for item in len19]
strip_list19


# In[63]:


len20 =  result[19]
len20
strip_list20 = [item.strip() for item in len20]
strip_list20


# In[64]:


len21 =  result[20]
len21
strip_list21 = [item.strip() for item in len21]
strip_list21


# In[65]:


len22 =  result[21]
len22
strip_list22 = [item.strip() for item in len22]
strip_list22


# In[66]:


len23 =  result[22]
len23
strip_list23 = [item.strip() for item in len23]
strip_list23


# In[91]:


len24 =  result[23]
len24

strip_list24 = [item.strip() for item in len24]
len(strip_list24)
strip_list24


# In[ ]:





# In[ ]:





# In[ ]:




