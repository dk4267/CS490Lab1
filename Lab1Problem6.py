import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing

#read in data, handle nulls
data = pd.read_csv('student-mat.csv', header=0, delimiter=';', encoding='ascii')
dataNoNull = data.interpolate().dropna()

#give numeric values for nonnumeric data
school_map = {'GP': 1, 'MS': 2}
dataNoNull['school'] = dataNoNull['school'].map(school_map)
dataNoNull['school'] = dataNoNull['school'].fillna(0)

sex_map = {'F': 1, 'M': 2}
dataNoNull['sex'] = dataNoNull['sex'].map(sex_map)
dataNoNull['sex'] = dataNoNull['sex'].fillna(0)

address_map = {'U': 1, 'R': 2}
dataNoNull['address'] = dataNoNull['address'].map(address_map)
dataNoNull['address'] = dataNoNull['address'].fillna(0)

famsize_map = {'LE3': 1, 'GT3': 2}
dataNoNull['famsize'] = dataNoNull['famsize'].map(famsize_map)
dataNoNull['famsize'] = dataNoNull['famsize'].fillna(0)

pstatus_map = {'T': 1, 'A': 2}
dataNoNull['Pstatus'] = dataNoNull['Pstatus'].map(pstatus_map)
dataNoNull['Pstatus'] = dataNoNull['Pstatus'].fillna(0)

job_map = {'teacher': 1, 'health': 2, 'services': 3, 'at_home': 4, 'other': 5}
dataNoNull['Mjob'] = dataNoNull['Mjob'].map(job_map)
dataNoNull['Mjob'] = dataNoNull['Mjob'].fillna(0)
dataNoNull['Fjob'] = dataNoNull['Fjob'].map(job_map)
dataNoNull['Fjob'] = dataNoNull['Fjob'].fillna(0)

reason_map = {'home': 1, 'reputation': 2, 'course': 3, 'other': 4}
dataNoNull['reason'] = dataNoNull['reason'].map(reason_map)
dataNoNull['reason'] = dataNoNull['reason'].fillna(0)

guardian_map = {'mother': 1, 'father': 2, 'other': 3}
dataNoNull['guardian'] = dataNoNull['guardian'].map(guardian_map)
dataNoNull['guardian'] = dataNoNull['guardian'].fillna(0)

yes_no_map = {'yes': 1, 'no': 2}
dataNoNull['schoolsup'] = dataNoNull['schoolsup'].map(yes_no_map)
dataNoNull['schoolsup'] = dataNoNull['schoolsup'].fillna(0)

dataNoNull['famsup'] = dataNoNull['famsup'].map(yes_no_map)
dataNoNull['famsup'] = dataNoNull['famsup'].fillna(0)

dataNoNull['paid'] = dataNoNull['paid'].map(yes_no_map)
dataNoNull['paid'] = dataNoNull['paid'].fillna(0)

dataNoNull['activities'] = dataNoNull['activities'].map(yes_no_map)
dataNoNull['activities'] = dataNoNull['activities'].fillna(0)

dataNoNull['nursery'] = dataNoNull['nursery'].map(yes_no_map)
dataNoNull['nursery'] = dataNoNull['nursery'].fillna(0)

dataNoNull['higher'] = dataNoNull['higher'].map(yes_no_map)
dataNoNull['higher'] = dataNoNull['higher'].fillna(0)

dataNoNull['internet'] = dataNoNull['internet'].map(yes_no_map)
dataNoNull['internet'] = dataNoNull['internet'].fillna(0)

dataNoNull['romantic'] = dataNoNull['romantic'].map(yes_no_map)
dataNoNull['romantic'] = dataNoNull['romantic'].fillna(0)

#create x data set
xdata = dataNoNull.drop(['G3'], axis=1)

#elbow method - best value seems to be n=5
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, max_iter=300, random_state=0)
    kmeans.fit(xdata)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

#do kmeans on the dataset using the number found from the elbow method
nclusters = 5
km = KMeans(n_clusters=nclusters)
km.fit(xdata)

# calculate silhouette score
y_cluster_kmeans = km.predict(xdata)
from sklearn import metrics
score = metrics.silhouette_score(xdata, y_cluster_kmeans)
print('Silhouette score before: ' + str(score))

#scatter plot showing correlation between G2 and G3 (highest correlated features)
plt.scatter(dataNoNull['G2'], dataNoNull['G3'], color='b')
plt.xlabel('G2 score')
plt.ylabel('G3 score')
plt.title('cluster using G2')
plt.show()

#use PCA on data, see if the silhouette score improves
scaler = preprocessing.StandardScaler()
scaler.fit(xdata)
X_scaled_array = scaler.transform(xdata)
X_scaled = pd.DataFrame(X_scaled_array, columns=xdata.columns)

pca = PCA(2)
X_pca = pca.fit_transform(X_scaled_array)

#kmeans after PCA
km3 = KMeans(n_clusters=nclusters)
km3.fit(X_pca)

#silhouette score after PCA
y_cluster_kmeans3 = km3.predict(X_pca)
score = metrics.silhouette_score(X_pca, y_cluster_kmeans3)
print('Silhouette score after PCA: ' + str(score))

#The silhouette score improved quite a bit after PCA