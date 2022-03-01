#!/usr/bin/env python
# coding: utf-8

# In[2]:


def worldCovidGraph():    
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.impute import SimpleImputer
    df =pd.read_csv('D:\sayadur\Data Science\covid_19_data\covid_19_data.csv')
    df.rename(columns={'ObservationDate':'Date','Province/State':'Province','Country/Region':'Country'},inplace=True)
    df['Date']=pd.to_datetime(df['Date'])
    df.drop(['SNo','Last Update'],axis=1,inplace=True)
    df4=df.groupby(['Date'])[['Date','Confirmed','Deaths','Recovered']].sum().reset_index()
    C=df4
    plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
    plt.scatter(np.arange(0,len(C)),C['Recovered'],color='green',label='Recovered')
    plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths') 
    plt.title('World')
    plt.xlabel('Days since the first suspect')
    plt.ylabel('Number of case')
    plt.legend()
    plt.show()
    return True

def countryCovidGraph():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.impute import SimpleImputer
    df =pd.read_csv('D:\sayadur\Data Science\covid_19_data\covid_19_data.csv')
    df.rename(columns={'ObservationDate':'Date','Province/State':'Province','Country/Region':'Country'},inplace=True)
    df['Date']=pd.to_datetime(df['Date'])
    df.drop(['SNo','Last Update'],axis=1,inplace=True)
    df3=df.groupby(['Country','Date'])[['Country','Date','Confirmed','Deaths','Recovered']].sum().reset_index()
    df4=df.groupby(['Date'])[['Date','Confirmed','Deaths','Recovered']].sum().reset_index()
    countries=df3['Country'].unique()
    for idx in range(0,len(countries)):
        C=df3[df3['Country']==countries[idx]].reset_index()
        plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
        plt.scatter(np.arange(0,len(C)),C['Recovered'],color='green',label='Recovered')
        plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths') 
        plt.title(countries[idx])
        plt.xlabel('Days since the first suspect')
        plt.ylabel('Number of case')
        plt.legend()
        plt.show()
    return True    


# In[3]:


worldCovidGraph()


# In[ ]:




