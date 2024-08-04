#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')


# In[4]:


soup


# In[5]:


soup.find_all('table')


# In[21]:


table = soup.find_all('table')[1]


# In[ ]:


## <table class="wikitable sortable jquery-tablesorter"> 


# In[22]:


soup.find('table', class_ = 'wikitable sortable')


# In[26]:


world_titles= table.find_all('th')


# In[27]:


world_titles


# ### Lets perform list comprehension by removing the labels from the list and just fetching the titles

# In[62]:


World_table_titles = [title.text.strip() for title in world_titles]


# In[63]:


World_table_titles


# In[64]:


import pandas as pd


# In[65]:


df = pd.DataFrame (columns = World_table_titles)
df


# In[66]:


column_data = table.find_all('tr')


# In[67]:


column_data


# In[68]:


for row in column_data[1:]:
   row_data = row.find_all('td')
   individual_rows = [data.text.strip() for data in row_data]
   
   Length = len(df)
   df.loc[Length] = individual_rows


# In[69]:


df


# In[73]:


df.to_csv (r'H:\Temp\BootCamp\Web_scraping_projects\United_States_Company_revenue.csv', index = False)


# In[ ]:





# In[ ]:




