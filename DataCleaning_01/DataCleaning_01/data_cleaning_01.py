#!/usr/bin/env python
# coding: utf-8

# In[83]:


#import libraries
import pandas as pd
import numpy as np


# In[84]:


#data overview
df = pd.read_csv('Datasets/BL-Flickr-Images-Book.csv') #data is under Datasets and put into a dataframe
df.head()#show the first 5 rows


# In[85]:


#too much information!
#let's remove some attributes that we will not use for now
#list of attributes we want to drop
to_drop = ["Edition Statement",'Corporate Author','Corporate Contributors',
           'Former owner','Engraver','Contributors','Issuance type','Shelfmarks']
df.drop(to_drop, inplace=True, axis=1) #https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop.html
#df.drop(columns=to_drop, inplace=True)
df.head() # a little better now


# In[86]:


#after removing attributes that are not interesting
df['Identifier'].is_unique #we know that attribute identifier is unique, so let's use it intead of index


# In[87]:


df = df.set_index('Identifier') #new index
#df.set_index('Identifier', inplace=True) would change the object directly


# In[88]:


df.head()


# In[89]:


#it allows us to do label-based indexing, which is the labeling of a row or record without regard to its position
df.loc[206]
#to access it by position df.iloc[0]
#https://pandas.pydata.org/pandas-docs/stable/indexing.html


# In[90]:


#we will be cleaning Date of Publication and Place of Publication
#let's examine what kind of data we have in our columns
df.get_dtype_counts()


# In[91]:


#starting from identifier 1905, show the next 10 items for attribute (col) 'date of publication'
df.loc[1905:, 'Date of Publication'].head(10)


# In[92]:


'''Several issues here
1. Remove the extra dates in square brackets, wherever present: 1879 [1878]
2. Convert date ranges to their "start date", wherever present: 1860-63; 1839, 38-54
3. Completely remove the dates we are not certain about and replace them with NumPy’s NaN: [1897?]
4. Convert the string nan to NumPy’s NaN value
'''


# In[93]:


#lets use some regular expressions to get rid of undisered values
regex = r'^(\d{4})' #we just want 4 consecutive digits - this is just a search pattern filter
extr = df['Date of Publication'].str.extract(regex, expand=False) #extracting from 'date of publication'
extr.head() #new dates


# In[94]:


df['Date of Publication'] = pd.to_numeric(extr) #we will transform an object into number
df['Date of Publication'].dtype


# In[95]:


#how much information was lost in the cleaning process - not so bad it seems
df['Date of Publication'].isnull().sum() / len(df) #all null values of the total number of records in the df


# In[96]:


#Let's look at other another attribute
df['Place of Publication'].head(10)


# In[97]:


#strings can be problem, let's apply some rules to them
df.loc[4157862]


# In[98]:


df.loc[4159587] #look ate 'place of publication' - it seems we have noisy data


# In[99]:


pub = df['Place of Publication'] #get the 'place of publication feature'
london = pub.str.contains('London')  #values that contain 'London'
london[:5] #some records do begin with 'London'


# In[100]:


#what about Oxford
oxford = pub.str.contains('Oxford')
oxford.head()


# In[101]:


#this works like an if-else for everythin with london or oxford we will get rid of '-'
df['Place of Publication'] = np.where(london, 'London',
                                      np.where(oxford, 'Oxford',
                                               pub.str.replace('-', ' '))) #replace '-' by ' ' (space)
df['Place of Publication'].head() #examine


# In[102]:


#how the original data look like now?
df.head() #much better


# In[103]:


'''
Exercises
1. Normalize 'Publisher' and 'Title' features so they only contain alphanumeric chars (i.e. remove &, "," and other non-letter symbols)
 1.1. Missing values should be marked as 'UNK'
2. On the clean 'Date of Publication' create a new feature that will categorize them as 'old' or 'modern'
 2.1. Indicate the threshold you used for this task
3. Normalize the 'Cost' attribute rounding it up (or down)
 3.1. Create a new feature called 'Cost-Category' based on the 'Cost' attribute distribution, where
 3.2. c < 0.25 - 'cheap';  0.25 <= c < 0.75 - 'average'; c >= 0.75 'expensive'. The thresholds for 'c' are based on
 the distribution of the cost values normalized
'''


# In[104]:


def clean_title(title):
    
    if title == 'nan':
        return 'NaN'
    
    if title[0] == '[':
        title = title[1: title.find(']')]
        
    if 'by' in title:
        title = title[:title.find('by')]
    elif 'By' in title:
        title = title[:title.find('By')]
        
    if '[' in title:
        title = title[:title.find('[')]

    title = title[:-2]
        
    title = list(map(str.capitalize, title.split()))
    return ' '.join(title)
    
df['Title'] = df['Title'].apply(clean_title)
df.head()


# In[105]:


#Clean Publisher
from functools import reduce

def clean_publisher(Publisher):
    
    Publisher = str(Publisher)
    
    if Publisher == 'nan':
        return 'NaN'
    
    Publisher = Publisher.split('&')

    if len(Publisher) == 1:
        name = filter(lambda x: x.isalpha(), Publisher[0])
        return reduce(lambda x, y: x + y, name)
    
    last_name, first_name = Publisher[1], Publisher[0]

    first_name = first_name[:first_name.find('-')] if '-' in first_name else first_name
    
    if first_name.endswith(('.', '.|')):
        parts = first_name.split('.')
        
        if len(parts) > 1:
            first_occurence = first_name.find('.')
            final_occurence = first_name.find('.', first_occurence + 1)
            first_name = first_name[:final_occurence]
        else:
            first_name = first_name[:first_name.find('.')]
    
    last_name = last_name.capitalize()
    
    return f'{last_name} {first_name}'


df['Publisher'] = df['Publisher'].apply(clean_publisher)
df.head()


# In[107]:


df['Publisher'].fillna("UNK", inplace = True) 
df['Publisher']


# In[108]:


unwanted_characters = ['[', ',', '-']

def clean_dates(dop):
    dop = str(dop)
    if dop.startswith('[') or dop == 'nan':
        return 'NaN'
    for character in unwanted_characters:
        if character in dop:
            character_index = dop.find(character)
            dop = dop[:character_index]
    return dop

df['Date of Publication'] = df['Date of Publication'].apply(clean_dates)
df.head()


# In[109]:


df['Date of Publication'] = df['Date of Publication'].astype(float)
df


# In[ ]:



