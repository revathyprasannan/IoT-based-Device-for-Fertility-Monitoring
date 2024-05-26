import Tkinter
from Tkinter import *
import PIL.Image
from PIL import ImageTk
##import ga
import datetime
import tkMessageBox
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score as vals
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.externals import joblib

f=open("sample.txt","r")
rr=f.read()
f.close()
t=rr.split("\n")
print t[0]
x_data=[]
y_data=[]
for i in range(len(t)):
        print t[i]
        pq=t[i].split(",")
        x_data.append(','.join(pq[:-1]))
        y_data.append(pq[-1])

print "DONE"
print x_data
print y_data
lr_rate=0.33
def extraction(x_data_original):
    tfidf = TfidfVectorizer()
    print type(x_data_original)
    vectors = tfidf.fit_transform(x_data_original)
    bigrm = list(nltk.bigrams(stems))
    print vectors
    print bigrm


tfidf = TfidfVectorizer()
val=lr_rate
vectors = tfidf.fit_transform(x_data)
print vectors
neigh = KNeighborsClassifier(n_neighbors=3)
X_train, X_test, y_train, y_test = train_test_split(vectors, y_data, test_size=0.33, random_state=42)

print X_train,y_train
neigh.fit(X_train,y_train)
y_pred=neigh.predict(X_test)
val=val+vals(y_test, y_pred)
import numpy as np
joblib.dump(neigh, 'model.pkl')
vector_to_predict = tfidf.transform(["34.21,1"])
##        print neigh.predict(vector_to_predict)[0]
print neigh.predict(vector_to_predict)[0]
##        print neigh.predict(vector_to_predict)[0]




