#!/usr/bin/env python
# coding: utf-8

# In[2]:


#libraries
import numpy as np
import pandas as pd


# In[3]:


#another messier example
university_towns = []
#readinf the content of file and append it to university_town list
with open('Datasets/university_towns.txt') as file:
    for line in file:
        if '[edit]' in line:
            # Remember this `state` until the next is found
            state = line
        else:
            # Otherwise, we have a city; keep `state` as last-seen
            university_towns.append((state, line)) #basically building our table
#let's check how it looks like
university_towns[:5] # a mess


# In[23]:


#let's use pandas to wrap this in a more usable format
#from our original vector let's put some names for the columns
towns_df = pd.DataFrame(university_towns,columns=['State', 'RegionName']) 
towns_df.head() # now we are talking - kind of...
#towns_df['RegionName'] = towns_df['RegionName'].astype(str)


# In[5]:


#again strings are a problem for us
#this functions will help us to extract the city-state of our region name
def get_citystate(item):
    if ' (' in item:
        return item[:item.find(' (')]
    elif '[' in item:
        return item[:item.find('[')]
    else:
        return item
#create another function to retrieve the University Name and add a new atribute to towns_df


# In[26]:


#we need to apply our function
#apply map takes our function and apply to the attributes in the dataframe
towns_df =  towns_df.applymap(get_citystate)
extractdf = towns_df
#can you think about the drawbacks of using this methodology?


# In[44]:


#Extracting the Region Position with function
def get_posi(item):
    if '[' in item:
        tmp = item[item.find('['):]
        posi = tmp[:tmp.find(']')]
        posi = posi[1:]
        return posi
    else:
        posi = "NA"
        return posi


positions = []
for item in towns_df.RegionName:
    new =  get_posi(item)
    #print(new)
    positions.append((new))

positions=np.array(positions)
extractdf['RegionPositon']= positions
#towns_df = towns_df.applymap (get_posi)
towns_df.head()


# In[50]:


#Extracting the university name

def get_univname(item):
    if '(' in item:
        temp = item[item.find('('):]
        clg = temp[:temp.find(')')]
        clg = clg[1:]
        return clg
    else:
        clg = "NA"
        return clg


colg = []
for item in towns_df.RegionName:
    nw =  get_univname(item)
    #print(nw)
    colg.append((nw))

colg=np.array(col)
extractdf['University Name']= colg
#towns_df = towns_df.applymap (get_position)
extractdf.head()
#del extractdf['UNIVNAME']


# In[52]:


extractdf.head(10)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




