# -*- coding: utf-8 -*-
"""
Created on Wed July 07 2021
@author: Saurabh Singh
"""

import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

df = pd.read_csv("spam.csv",encoding="latin-1")
#df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'],axis=1,inplace=True)

#Features and labels
df['label'] = df['class'].map({'ham': 0,'spam': 1})
X = df['message']
y = df['label']

#Extract Feature with CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(X) #fit the data

pickle.dump(cv,open('transform.pkl','wb'))

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33,random_state=42)

#Naive Bayes Classifier
clf = MultinomialNB()
clf.fit(X_train,y_train)
clf.score(X_test,y_test)
filename = 'nlp_model.pkl'
pickle.dump(clf, open(filename,'wb'))

