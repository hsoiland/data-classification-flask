import numpy as np
import pandas as pd
from sklearn import datasets
import psycopg2

con = psycopg2.connect(host="localhost", user="postgres", password="password", dbname="creditdb")
cur = con.cursor()

dataset = pd.read_csv('preprocessed.csv')

from sklearn.model_selection import train_test_split

x_w = dataset.iloc[0:999, :-1].values
y_w = dataset.iloc[0:999, 59].values


x = dataset.iloc[0:399, :-1].values
y = dataset.iloc[0:399, 59].values

x_v = dataset.iloc[400:999,:-1].values
y_p = dataset.iloc[400:999, 59].values



x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.5, random_state=0)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=7)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

print cm

from sklearn.model_selection import cross_val_score
print np.mean(cross_val_score(classifier, x_train, y_train, cv=10))

large_set = classifier.predict(x_v)
cm1 = confusion_matrix(y_p, large_set)
print cm1
crossvalidation = np.mean(cross_val_score(classifier, x_v, y_p, cv=10))
print crossvalidation

data = classifier.predict(x_w)
data = pd.DataFrame(data)

# query = """UPDATE creditclassified SET classification =("%s");"""
# cur.execute(query, data)
cur.executemany('UPDATE creditclassified SET classification= %s', ((val,) for val in data))


data.to_csv("predictions.csv", sep=",")

from sklearn.externals import joblib

joblib.dump(classifier, 'model.pk1')
