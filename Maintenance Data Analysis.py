#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv("C:/Users/Neethu Santhosh/Desktop/decoder lectures/case study/maintenance_data.csv")


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.columns


# In[7]:


df.dtypes


# In[8]:


df.head()


# In[9]:


con=["lifetime","pressureInd","moistureInd","temperatureInd"]
cat=["broken","team","provider"]


# In[10]:


df.duplicated().sum()


# In[11]:


df=df.drop_duplicates()


# In[12]:


df.shape


# In[13]:


df.isnull().sum()


# In[14]:


#univariate
#bivariate
#multivariate


# In[15]:


for i in cat:
    sns.countplot(x=i,data=df)
    plt.show()
    


# In[17]:


for i in con:
    sns.displot(df[i])
    plt.show()


# In[18]:


for i in con:
    sns.scatterplot(x=df.index, y=df[i])
    plt.show()


# In[35]:


#bivariate analysis
for i in con:
    sns.stripplot(x="broken",y=i,data=df)
    plt.show()


# In[20]:


for i in con:
    sns.scatterplot(df[i],df["lifetime"])
    plt.show()


# In[21]:


sns.heatmap(df.corr(),annot=True,cmap="coolwarm")


# In[46]:


for i in cat:
    sns.countplot(x=df[i],hue=df["broken"])
    plt.show()


# In[22]:


out=pd.crosstab(df["team"],df["broken"],margins=True)


# In[23]:


out


# In[24]:


out[1]/out["All"]


# In[25]:


out=pd.crosstab(df["provider"],df["broken"],margins=True)
out[1]/out["All"]


# In[26]:


#multicariate analysis
sns.scatterplot(x="lifetime",y="moistureInd",hue="broken",data=df)


# In[27]:


sns.scatterplot(x="lifetime",y="pressureInd",hue="broken",data=df)


# In[28]:


sns.scatterplot(x="lifetime",y="temperatureInd",hue="broken",data=df)


# In[34]:


sns.stripplot(x="provider",y="moistureInd",hue="broken",data=df)


# In[32]:


sns.stripplot(x="provider",y="temperatureInd",hue="broken",data=df)


# In[33]:


sns.stripplot(x="provider",y="pressureInd",hue="broken",data=df)


# In[ ]:




