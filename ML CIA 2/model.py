#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
heart_df=pd.read_csv(r"C:\Users\niran\Downloads\framingham.csv")
heart_df.drop(['education'],axis=1,inplace=True)
heart_df.rename(columns={'male':'Sex_male'},inplace=True)
heart_df.dropna(axis=0,inplace=True)

new_features=heart_df[['age','Sex_male','cigsPerDay','totChol','sysBP','glucose','TenYearCHD']]
x=new_features.iloc[:,:-1]
y=new_features.iloc[:,-1]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20,random_state=5)

from sklearn.linear_model import LogisticRegression
logreg=LogisticRegression()
logreg.fit(x_train,y_train)
y_pred=logreg.predict(x_test)



import pickle


pickle.dump(logreg,open('model.pkl','wb'))



