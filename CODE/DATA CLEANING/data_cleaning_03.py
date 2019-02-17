#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import re
import pandas as pd


# In[3]:


#how to rename columns and/or skip rows that we don't want to consider
#loading our data
olympics_df = pd.read_csv('Datasets/olympics.csv')
olympics_df.head() #not very friendly right?
#olympics_df.add(Tag)


# In[4]:


#the first line are the headers so, not very data-useful
olympics_df = pd.read_csv('Datasets/olympics.csv', header=1) 
olympics_df.head() #still weird, but this is closer to what we want - now we "have" headers


# In[5]:


#let's try to make some sense of the headers now
#creating a dictionary K,V
new_names =  {'Unnamed: 0': 'Country',
              '? Summer': 'Summer Olympics',
              '01 !': 'Gold',
              '02 !': 'Silver',
              '03 !': 'Bronze',
              '? Winter': 'Winter Olympics',
              '01 !.1': 'Gold.1',
              '02 !.1': 'Silver.1',
              '03 !.1': 'Bronze.1',
              '? Games': '# Games',
              '01 !.2': 'Gold.2',
              '02 !.2': 'Silver.2',
              '03 !.2': 'Bronze.2',
             }


# In[6]:


olympics_df.rename(columns=new_names, inplace=True)#our new names
olympics_df.head() #now ti looks like a dataset


# In[7]:


'''
Exercise
1. Create a new attribute called 'Tag' and it should contain the letters between (*) from  'Country'
2. Alter the values of 'Country' so it just contains the actual names of the countries
3. Create a new dataframe only containing only the following attributes: 'Tag', 'summer olympics' and 'winter olympics'.
 3.1. In addition, it should also contain 'combined Total', which has to be calculated using the sum of 'summmer olympics' and 'winter olympics'
'''


# In[8]:


country_df = olympics_df['Country']
#country_df
country_df[0]


# In[9]:


#for i in range(0,len(country_df)):
 #   print(country_df[i].strip())


# In[10]:


#Extracting Country Names
cname = []
for i in range(0,len(country_df)):
    cname.append(country_df[i].split(" ")[0])
cname


# In[11]:


olympics_df['Country'] = cname
olympics_df.head()


# In[12]:


#Creating Tags
a =[]
for i in range(0,len(country_df)):
    a.append(re.findall('\((.*?)\)',country_df[i]))
a
ccode= []
for j in range(0,147):
    ccode.append(country_df[j][:3].upper())
ccode


# In[13]:


'''data = ['ccode']
tag_df = pd.DataFrame(data)
tag_df'''
tag = pd.Series(ccode)
#tag
olympics_df['Tag'] = tag.values
olympics_df.head()


# In[14]:


#3rd Question Creating new dataframe with existing columns
data_extract = olympics_df[['Tag', 'Summer Olympics', 'Winter Olympics']]
extracted_df = pd.DataFrame(data_extract)
extracted_df.head()


# In[15]:


#creating combined column and adding to data frame
Combined_Total = olympics_df['Summer Olympics'] + olympics_df['Winter Olympics']
extracted_df['Combined_Total'] = olympics_df['Summer Olympics'] + olympics_df['Winter Olympics']
extracted_df.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




