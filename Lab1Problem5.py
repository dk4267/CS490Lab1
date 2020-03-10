import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC, SVC
from sklearn.metrics import classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt

#deal with null data, make a histogram
data = pd.read_csv('adult.csv', header=0, delimiter=',', encoding='ascii', engine='python')
dataNoNull = data.interpolate().dropna()
plt.hist(dataNoNull['target'], color="blue")
plt.show()

#assign numeric values to non-numeric entries
workclass_map = {' Self-emp-not-inc': 1, ' Self-emp-inc': 2, ' Federal-gov': 3, ' Local-gov': 4, ' State-gov': 5,
                 ' Without-pay': 6, ' Never-worked': 7, ' Private': 8}
dataNoNull['workclass'] = dataNoNull['workclass'].map(workclass_map)
dataNoNull['workclass'] = dataNoNull['workclass'].fillna(0)

education_map = {' Some-college': 1, ' 11th': 2, ' HS-grad': 3, ' Prof-school': 4, ' Assoc-acdm': 5, ' Assoc-voc': 6,
                 ' 9th': 7, ' 7th-8th': 8, ' 12th': 9, ' Masters': 10, ' 1st-4th': 11, ' 10th': 12, ' Doctorate': 13,
                 ' 5th-6th': 14, ' Preschool': 15, ' Bachelors': 16}
dataNoNull['education'] = dataNoNull['education'].map(education_map)
dataNoNull['education'] = dataNoNull['education'].fillna(0)

marital_map = {' Married-civ-spouse': 1, ' Divorced': 2, ' Never-married': 3, ' Separated': 4, ' Widowed': 5,
               ' Married-spouse-absent': 6, ' Married-AF-spouse': 7}
dataNoNull['marital-status'] = dataNoNull['marital-status'].map(marital_map)
dataNoNull['marital-status'] = dataNoNull['marital-status'].fillna(0)

#this is when I started to regret using this data set
occupation_map = {' Tech-support': 1, ' Craft-repair': 2, 'Other-service': 3, ' Sales': 4, ' Exec-managerial': 5,
                  'Prof-specialty': 6, ' Handlers-cleaners': 7, ' Machine-op-inspct': 8, ' Adm-clerical': 9,
                  ' Farming-fishing': 10, ' Transport-moving': 11, ' Priv-house-serv': 12, ' Protective-serv': 13,
                  ' Armed-Forces': 14}
dataNoNull['occupation'] = dataNoNull['occupation'].map(occupation_map)
dataNoNull['occupation'] = dataNoNull['occupation'].fillna(0)

relationship_map = {' Wife': 1, ' Own-child': 2, ' Husband': 3, ' Not-in-family': 4, ' Other-relative': 5,
                    ' Unmarried': 6}
dataNoNull['relationship'] = dataNoNull['relationship'].map(relationship_map)
dataNoNull['relationship'] = dataNoNull['relationship'].fillna(0)

race_map = {' White': 1, ' Asian-Pac-Islander': 2, ' Amer-Indian-Eskimo': 3, ' Other': 4, ' Black': 5}
dataNoNull['race'] = dataNoNull['race'].map(race_map)
dataNoNull['race'] = dataNoNull['race'].fillna(0)

sex_map = {' Female': 1, ' Male': 2}
dataNoNull['sex'] = dataNoNull['sex'].map(sex_map)
dataNoNull['sex'] = dataNoNull['sex'].fillna(0)

#I regret everything :/
country_map = {' United-States': 1, ' Cambodia': 2, ' England': 3, ' Puerto-Rico': 4, ' Canada': 5, ' Germany': 6,
               '  Outlying-US(Guam-USVI-etc)': 7, ' India': 8, ' Japan': 9, ' Greece': 10, ' South': 11, ' China': 12,
               ' Cuba': 13, ' Iran': 14, ' Honduras': 15, ' Philippines': 16, ' Italy': 17, ' Poland': 18,
               ' Jamaica': 19, ' Vietnam': 20, ' Mexico': 21, ' Portugal': 22, ' Ireland': 23, ' France': 24,
               '  Dominican-Republic': 25, '  Laos': 26, ' Ecuador': 27, ' Taiwan': 28, ' Haiti': 29, ' Columbia': 30,
               ' Hungary': 31, '  Guatemala': 32, ' Nicaragua': 33, ' Scotland': 34, ' Thailand': 35, ' Yugoslavia': 36,
               '  El-Salvador': 37, '  Trinadad&Tobago': 38, ' Peru': 39, ' Hong': 40, '  Holand-Netherlands': 41}
dataNoNull['native-country'] = dataNoNull['native-country'].map(country_map)
dataNoNull['native-country'] = dataNoNull['native-country'].fillna(0)

target_map = {' >50K': 1, '  <=50K': 2}
dataNoNull['target'] = dataNoNull['target'].map(target_map)
dataNoNull['target'] = dataNoNull['target'].fillna(0)

#find 5 least correlated values and drop them from dataset
corr = dataNoNull.corr()
print(corr['target'].sort_values(ascending=False)[1:5], '\n')
print(corr['target'].sort_values(ascending=False)[-5:])
dataNoNull = dataNoNull.drop(['workclass', 'occupation', 'race', 'relationship', 'marital-status'], axis=1)

#create train test split
X_train = dataNoNull.drop(['target'], axis=1)
Y_train = dataNoNull['target']
X_train, X_test, y_train, y_test = train_test_split(X_train, Y_train, test_size=0.3, random_state=0)

#Naive Bayes algorithm
naiveBayes = GaussianNB()
prediction = naiveBayes.fit(X_train, y_train).predict(X_test)
print('NB: ' + classification_report(y_test, prediction))

#SVM algorithm
svc = SVC()
prediction = svc.fit(X_train, y_train).predict(X_test)
print('SVM: ' + classification_report(y_test, prediction))

#KNN algorithm
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)
acc_knn = round(knn.score(X_train, Y_train) * 100, 2)
print("KNN: ", acc_knn)

#NB got a slightly higher score than SVM
#KNN crashed because of an inconsistent number of samples in the dataset, but I couldn't figure out how
#to solve that problem