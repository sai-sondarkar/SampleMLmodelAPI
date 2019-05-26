#import of the dependencies 
import pandas as pd 
import numpy as np 
import os 

#loading of of our dataset into the model.py srcipt 

dir_path = os.path.dirname(os.path.realpath(__file__))

uri = dir_path +"/data/train.csv"

df = pd.read_csv(uri)

include = ['Age','Sex','Survived','Embarked']

df_ = df[include]

#data processing 
categories = []
for col,col_type in df_.dtypes.iteritems():
    if col_type == 'O':
        categories.append(col)
    else:
        df_[col].fillna(0,inplace= True)

    
df_ohe = pd.get_dummies(df_,columns = categories, dummy_na= True )


#Logistic Regression Classifiers 

from sklearn.linear_model import LogisticRegression

dependent_variables = "Survived"

x = df_ohe[df_ohe.columns.difference([dependent_variables])]
y = df_ohe[dependent_variables]

lr = LogisticRegression()

lr.fit(x,y)

#saving the model 
from sklearn.externals import joblib

#saving our model in to a pickle file
joblib.dump(lr,'model.pkl')
print('Model Dumped')

#loading from the model which we saved
lr = joblib.load('model.pkl')

#saving our columns which we used for the model train
model_columns = list(x.columns)
joblib.dump(model_columns,'model_columns.pkl')
print("model colunms dumped")