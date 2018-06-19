
# coding: utf-8

# In[3]:


import urllib.request
import urllib.error


# In[4]:


from bs4 import BeautifulSoup


# In[28]:


wiki = "https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=600ca544-31f5-4bd8-ae38-ea4014c93bab&pf_rd_r=ACT8TC2YA82E1GWHC1W8&pf_rd_s=right-4&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_india_tr_rhs_1"


# In[29]:


page = urllib.request.urlopen(wiki)


# In[30]:


soup = BeautifulSoup(page)


# In[31]:


print(soup.prettify())


# In[32]:


print(soup.title.string)


# In[60]:


all_tables=soup.find_all('table')
right_table=soup.find('table', class_='chart full-width')
right_table


# In[90]:


i=1
serial=[]
name=[]
for column in right_table.findAll("td", class_='titleColumn'):
    print(i,column.find('a').string)
    serial.append(i)
    name.append(column.find('a').string)
    i=i+1


# In[105]:


import pandas as pd
d ={'Movie Name':name}
df=pd.DataFrame(data=d)


# In[106]:


df


# In[108]:


df.to_csv()


# In[107]:


df.to_csv('hindi_movie_list.csv')

