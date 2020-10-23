#!/usr/bin/env python
# coding: utf-8

# In[267]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns 


# In[268]:


corona_data = pd.read_csv("Corona_data_Jan_to_Aug_2020.csv")


# In[269]:


corona_data.T


# In[301]:


corona_data.describe


# In[302]:


corona_data.info()


# In[344]:


corona_data.isnull().sum()


# In[ ]:


# As we can see that there is no null value in the data set that means data is error free.


# In[270]:


corona_data.columns


# In[271]:


corona_data = corona_data[['Date', 'Name of State / UT',
       'Total Confirmed cases', 'Death', 'Cured/Discharged/Migrated',
       'New cases', 'New deaths', 'New recovered']]


# In[ ]:


# Dropping of unnecessary column.


# In[272]:


corona_data.columns = ['Date', 'State/Ut','Total_Confirmed_cases','overall_Death_cases','Total_Cured/Discharged/Migrated',
       'New cases','New deaths','New recovered']


# In[ ]:


# Renaming of columns.


# In[273]:


c_data = corona_data


# In[274]:


c_data.head()


# In[275]:


c_data.tail()


# In[276]:


unique_provinces = c_data['State/Ut'][c_data.Total_Confirmed_cases >0 ].unique()


# In[277]:


unique_provinces


# In[278]:


province_confirmed_cases = []
for i in unique_provinces:
    province_confirmed_cases.append(c_data[c_data.Total_Confirmed_cases > 0 ][c_data['State/Ut'] == i].Total_Confirmed_cases.sum())


# In[ ]:


# Below,we can clearly see the number of confirmed cases present in different states of India in between the month of jan to early Aug.


# In[279]:


for i in range(len(unique_provinces)):
    print (f'{unique_provinces[i]}: {province_confirmed_cases[i]} cases')


# In[ ]:


# For better visualization of situation,we have pie chart below.


# In[280]:


plt.figure(figsize=(15,15))
plt.pie(province_confirmed_cases)
plt.legend(unique_provinces,)
plt.show()


# In[281]:


import datetime 

c_data['Date'] = pd.to_datetime(c_data['Date']) 
c_data['date'] = [datetime.datetime.date(d) for d in c_data ['Date']]
c_data['Time'] = [datetime.datetime.time(d) for d in c_data['Date']]


# In[282]:


c_data['date'] = c_data['date'].astype(str)
day = c_data["date"].values
day = [my_str.split("-")[2] for my_str in day]
c_data["date"] = day


# In[283]:


c_data =c_data.drop(['Date'], axis=1)


# In[284]:


c_data.head()


# In[285]:


unique_dates = c_data['date'].unique()
unique_dates = np.flipud(unique_dates) 

unique_dates


# In[286]:


india_cases = []

for i in unique_dates:
    india_cases.append(c_data[c_data['date']==i].Total_Confirmed_cases.sum())

plt.figure(figsize=(15, 10));
plt.plot(unique_dates, india_cases);
plt.title('No of Coronavirus Cases Over Days', size=15);
plt.xlabel('Days', size=15)
plt.ylabel('No of Cases', size=15);
plt.show();


# In[334]:


world = c_data.groupby("State/Ut")['Total_Confirmed_cases','overall_Death_cases','Total_Cured/Discharged/Migrated'].sum().reset_index()
world.head(40)


# In[345]:


#   We can easily calculate the percentage of recoveries and deaths with the help of above data. Which shows number of recoveries,death and confirmed cases.


# In[317]:


c_data['State/Ut'].unique().shape


# In[346]:


top = world.sort_values(by=['Total_Confirmed_cases'], ascending=False).head(40)
### Generate a Barplot
plt.figure(figsize=(20,30))
plot = sns.barplot(top['Total_Confirmed_cases'], top['State/Ut'])
for i,(value,name) in enumerate(zip(top['Total_Confirmed_cases'],top['State/Ut'])):
    plot.text(value,i-0.05,f'{value:,.0f}',size=10)
plt.show()


# In[305]:


# Plotting the states with the maximum number of confirmed cases in the given data set.


# In[342]:


top_20 = world.sort_values(by=['Total_Confirmed_cases'], ascending=False).head(20)
### Generate a Barplot
plt.figure(figsize=(10,10))
confirmed = sns.barplot(top_20['Total_Confirmed_cases'], top_20['State/Ut'], color = 'red', label='Total Confirmed cases')
recovered = sns.barplot(top_20['Total_Cured/Discharged/Migrated'], top_20['State/Ut'], color = 'green', label='Total Recovered')
### Add Texts for Barplots
for i,(value,name) in enumerate(zip(top_20['Total_Confirmed_cases'],top_20['State/Ut'])):
    confirmed.text(value,i-0.05,f'{value:,.0f}',size=9)
for i,(value,name) in enumerate(zip(top_20['Total_Cured/Discharged/Migrated'],top_20['State/Ut'])):
    recovered.text(value,i-0.05,f'{value:,.0f}',size=9)
plt.legend(loc=4)
plt.show()


# In[ ]:


#  Above graph shows the graphical visualization of the number of recoveries with respect to total cases of the top 20 states.


# In[343]:


top_20 = world.sort_values(by=['Total_Confirmed_cases'], ascending=False).tail(20)
### Generate a Barplot
plt.figure(figsize=(10,10))
confirmed = sns.barplot(top_20['Total_Confirmed_cases'], top_20['State/Ut'], color = 'red', label='Total Confirmed cases')
recovered = sns.barplot(top_20['Total_Cured/Discharged/Migrated'], top_20['State/Ut'], color = 'green', label='Total Recovered')
### Add Texts for Barplots
for i,(value,name) in enumerate(zip(top_20['Total_Confirmed_cases'],top_20['State/Ut'])):
    confirmed.text(value,i-0.05,f'{value:,.0f}',size=9)
for i,(value,name) in enumerate(zip(top_20['Total_Cured/Discharged/Migrated'],top_20['State/Ut'])):
    recovered.text(value,i-0.05,f'{value:,.0f}',size=9)
plt.legend(loc=4)
plt.show()


# In[ ]:


#   #  Above graph shows the graphical visualization of the total number of recoveries wrt total cases of the lower 20 states.


# In[347]:


# Hence,this is all about corona analysis.

#      AKHIL BHALL


# In[ ]:




