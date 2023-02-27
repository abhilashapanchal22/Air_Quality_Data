#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd
import numpy as py
import matplotlib as plt
import seaborn as se


# In[7]:


data_air = pd.read_csv(r"C:\Users\shash\Desktop\DA\project\air-quality-data.csv")


# In[8]:


data_air.info()


# In[9]:


data_air.head()


# In[ ]:


#converting timestamp column to datetime object


# In[26]:


data_air["Timestamp"] = pd.to_datetime(data_air["Timestamp"])


# In[28]:


data_air.info()


# In[51]:


data_air["Timestamp"].dt.year


# In[ ]:


#separating year from datetime 


# In[31]:


data_air["Year"] = data_air["Timestamp"].dt.year


# In[32]:


data_air.info()


# In[ ]:


#finding the average of timestamp and PM2.5


# In[40]:


year_avg = data_air.groupby("Year")["PM2.5"].mean()


# In[41]:


year_avg


# In[ ]:


#plot


# In[42]:


year_avg.plot(kind = "line", figsize = (15,5))


# In[ ]:


#showing average pollution monthwise through area plot


# In[43]:


data_air.head()


# In[45]:


data_air["Timestamp"] = pd.to_datetime(data_air["Timestamp"])


# In[53]:


data_air["Month"] = data_air["Timestamp"].dt.month


# In[54]:


data_air["Timestamp"].dt.month


# In[56]:


data_air.info()


# In[77]:


month_avg = data_air.groupby("Month")["PM2.5"].mean()


# In[78]:


month_avg


# In[79]:


month_avg.plot(kind = "area", figsize = (12,5))


# In[ ]:


# hourwise average pollution with bar graph


# In[80]:


data_air.head()


# In[82]:


data_air["Timestamp"] = pd.to_datetime(data_air["Timestamp"])


# In[87]:


data_air["Hour"] = data_air["Timestamp"].dt.hour


# In[88]:


data_air["Timestamp"].dt.hour


# In[89]:


data_air.head()


# In[90]:


data_air.groupby("Hour")["PM2.5"].mean()


# In[91]:


hour_avg = data_air.groupby("Hour")["PM2.5"].mean()


# In[92]:


hour_avg


# In[93]:


hour_avg.plot(kind = "bar", figsize = (12,5))


# In[ ]:


#months where the airquality is very unhealthy


# In[94]:


data_air.head()


# In[96]:


x = data_air[(data_air["PM2.5"] >= 150.5) & (data_air["PM2.5"] <= 250.4)]


# In[97]:


x


# In[98]:


x.value_counts("Month")


# In[ ]:


#month in which the air quality is good/fresh


# In[101]:


y = data_air[(data_air["PM2.5"] <= 12.0)]


# In[102]:


y


# In[104]:


y.value_counts("Month")


# In[ ]:


# how many times AQI's recorded moderate


# In[108]:


z = data_air[(data_air["Year"] == 2018) & (data_air["PM2.5"] >= 12.1) & (data_air["PM2.5"] <= 35.4)]


# In[109]:


z


# In[111]:


z.Year.unique()


# In[113]:


z["PM2.5"]


# In[ ]:


# weather condition in the of january and july


# In[115]:


data_air[data_air["Month"] == 1]["PM2.5"].mean()               # unhealthy air


# In[117]:


data_air[data_air["Month"] == 7]["PM2.5"].mean()


# In[ ]:




