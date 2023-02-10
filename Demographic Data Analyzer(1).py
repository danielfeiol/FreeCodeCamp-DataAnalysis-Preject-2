#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[ ]:


# Read data from file


# In[2]:


df = pd.read_csv("C:/Users/dfeil/Downloads/adult.data.csv")


# In[3]:


df.head


# In[ ]:


# How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.


# In[4]:


pd.Series(df.race).value_counts()


# In[ ]:


# What is the average age of men?


# In[5]:


sum_males =df.loc[df["sex"] == "Male"]


# In[24]:


sum_males.mean(numeric_only=True)[0]


# In[ ]:


# What is the percentage of people who have a Bachelor's degree?


# In[7]:


pd.Series(df.education == "Bachelors").mean().round(decimals =4)*100


# In[ ]:


# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?


# In[8]:


pd.Series(((df.education == "Bachelors") | (df.education == "Masters" )| (df.education == "Doctorate")) & (df.salary == ">50K")).mean().round(decimals =4)*100


# In[ ]:


# What percentage of people without advanced education make more than 50K?


# In[9]:


pd.Series(((df.education != "Bachelors") | (df.education != "Masters" )| (df.education != "Doctorate")) & (df.salary == ">50K")).mean().round(decimals =4)*100


# In[ ]:


# What is the minimum number of hours a person works per week (hours-per-week feature)?


# In[10]:


pd.Series(df.columns)[12]


# In[11]:


min_work = pd.Series(df["hours-per-week"]).min()
min_work


# In[ ]:


# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?


# In[12]:


pd.Series(min_work & pd.Series(df.salary == ">50K")).mean().round(decimals =4)*100


# In[13]:


# What country has the highest percentage of people that earn >50K and what is that percentage?


# In[14]:


richest_country=df[(df.salary == ">50K")]
number_high = richest_country["native-country"].value_counts()


# In[15]:


jobs_sum = df["native-country"].value_counts()


# In[16]:


percentage = jobs_sum/number_high


# In[22]:


result = pd.DataFrame({"land": percentage.index, "percentage": percentage.values})
result = result.sort_values("percentage", ascending=False)
result.round(decimals=2).head(3)


# In[18]:


# Identify the most popular occupation for those who earn >50K in India.


# In[19]:


india_jobs=df[(df["native-country"] == "India") & (df.salary == ">50K")]


# In[20]:


india_jobs["occupation"].value_counts()

