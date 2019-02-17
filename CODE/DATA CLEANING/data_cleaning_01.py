#!/usr/bin/env python
# coding: utf-8

# In[17]:


#import libraries
import pandas as pd
import numpy as np


# In[18]:


#data overview
df = pd.read_csv('Datasets/BL-Flickr-Images-Book.csv') #data is under Datasets and put into a dataframe
df.head()#show the first 5 rows


# In[19]:


#too much information!
#let's remove some attributes that we will not use for now
#list of attributes we want to drop
to_drop = ["Edition Statement",'Corporate Author','Corporate Contributors',
           'Former owner','Engraver','Contributors','Issuance type','Shelfmarks']
df.drop(to_drop, inplace=True, axis=1) #https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop.html
#df.drop(columns=to_drop, inplace=True)
df.head() # a little better now


# In[20]:


#after removing attributes that are not interesting
df['Identifier'].is_unique #we know that attribute identifier is unique, so let's use it intead of index


# In[21]:


df = df.set_index('Identifier') #new index
#df.set_index('Identifier', inplace=True) would change the object directly


# In[22]:


df.head()


# In[23]:


#it allows us to do label-based indexing, which is the labeling of a row or record without regard to its position
df.loc[206]
#to access it by position df.iloc[0]
#https://pandas.pydata.org/pandas-docs/stable/indexing.html


# In[24]:


#we will be cleaning Date of Publication and Place of Publication
#let's examine what kind of data we have in our columns
df.get_dtype_counts()


# In[25]:


#starting from identifier 1905, show the next 10 items for attribute (col) 'date of publication'
df.loc[1905:, 'Date of Publication'].head(10)


# In[26]:


'''Several issues here
1. Remove the extra dates in square brackets, wherever present: 1879 [1878]
2. Convert date ranges to their "start date", wherever present: 1860-63; 1839, 38-54
3. Completely remove the dates we are not certain about and replace them with NumPy’s NaN: [1897?]
4. Convert the string nan to NumPy’s NaN value
'''


# In[27]:


#lets use some regular expressions to get rid of undisered values
regex = r'^(\d{4})' #we just want 4 consecutive digits - this is just a search pattern filter
extr = df['Date of Publication'].str.extract(regex, expand=False) #extracting from 'date of publication'
extr.head() #new dates


# In[28]:


df['Date of Publication'] = pd.to_numeric(extr) #we will transform an object into number
df['Date of Publication'].dtype


# In[29]:


#how much information was lost in the cleaning process - not so bad it seems
df['Date of Publication'].isnull().sum() / len(df) #all null values of the total number of records in the df


# In[30]:


#Let's look at other another attribute
df['Place of Publication'].head(10)


# In[31]:


#strings can be problem, let's apply some rules to them
df.loc[4157862]


# In[32]:


df.loc[4159587] #look ate 'place of publication' - it seems we have noisy data


# In[33]:


pub = df['Place of Publication'] #get the 'place of publication feature'
london = pub.str.contains('London')  #values that contain 'London'
london[:5] #some records do begin with 'London'


# In[34]:


#what about Oxford
oxford = pub.str.contains('Oxford')
oxford.head()


# In[35]:


#this works like an if-else for everythin with london or oxford we will get rid of '-'
df['Place of Publication'] = np.where(london, 'London',
                                      np.where(oxford, 'Oxford',
                                               pub.str.replace('-', ' '))) #replace '-' by ' ' (space)
df['Place of Publication'].head() #examine


# In[36]:


#how the original data look like now?
df.head() #much better


# In[37]:


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


# In[38]:


#clean title
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


# In[39]:


#CLEAN PUBLISHER
import numpy as npy
import pandas as pds
df = pds.read_csv('Datasets/BL-Flickr-Images-Book.csv')
df.Publisher = df.Publisher.str.replace('[^A-Za-z0-9]+', ' ')
import numpy as npy
df.Publisher = df.Publisher.replace(np.nan, 'UNK', regex=True)
df.Publisher[:10]


# In[40]:


#Clean DOP
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
df.head(4)
#df['Date of Publication'].head(10)


# In[41]:


xtype = df['Date of Publication']
xtype.head(4)


# In[42]:


import numpy as np
doparray = np.array(xtype)


# In[43]:


cat = []
for i in range(0,len(doparray)):
    if doparray[i]> '1750':
        cat.append('Modern')
    elif doparray[i]< '1750':
        cat.append('Old')
    else:
        cat.append('NaN')
len(cat)


# In[61]:


df['Publication Catogery'] = cat
df['Publication Catogery'].head(10)


# In[45]:


#Taking the cost values into an array to scale
from sklearn import preprocessing
import numpy as np
df = pd.read_csv('Datasets/BL-Flickr-Images-Book.csv', sep=',')
x_array = np.array(df['Cost'])


# In[46]:


x_array


# 

# In[47]:


#Rounding the Cost attributes
df['Cost'] = round(df['Cost'])


# In[48]:


#Reshaping the array to (-1,1) because its not an 2D array
from numpy import array
test2d = df['Cost'].values.reshape(-1,1)
test2d


# In[49]:


#Using the MinMaxScaler() Function for rescaling the weight
from sklearn.preprocessing import MinMaxScaler
import numpy as np
np.set_printoptions(threshold=np.nan)
weights = x_array
scaler = MinMaxScaler()
rescaled_weight = scaler.fit_transform(test2d)
rescaled_weight


# In[50]:


costcatogery = []


# In[51]:


#Creating the new attribute defining the catogery of cost as "CHEAP, AVERAGE, EXPENSIVE"
for i in range(0,len(rescaled_weight)):
    if rescaled_weight[i] < 0.25:
        costcatogery.append('Cheap')
    elif rescaled_weight[i] > 0.25 and rescaled_weight[i] < 0.75:
        costcatogery.append('average')
    else:
        costcatogery.append('expensive')


# In[58]:


len(costcatogery)


# In[53]:


df['CostCatogery'] = costcatogery


# In[54]:


costcatogery


# In[55]:


df.head(5)


# In[62]:


df[['Identifier','Place of Publication','Date of Publication','Publisher','Title','Author','Cost','Publication Catogery','CostCatogery']]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




