import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

#read data, handle nulls, replace nonnumeric values with numeric ones
data = pd.read_csv('student-mat.csv', header=0, delimiter=';', encoding='ascii')
dataNoNull = data.interpolate().dropna()

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

#set up x and y datasets and make train test split
xdata = dataNoNull.drop(['G3'], axis=1)
ydata = dataNoNull['G3']
X_train, X_test, y_train, y_test = train_test_split(
                                    xdata, ydata, random_state=42, test_size=.33)

#Set up linear regression model
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)

#RMSE test
predictions = model.predict(X_test)
print('RMSE before is: \n', mean_squared_error(y_test, predictions))

#R squared test
print("R^2 before is: \n", model.score(X_test, y_test))

#find least correlated columnns and remove them from dataset
corr = dataNoNull.corr()
print (corr['G3'].sort_values(ascending=False)[:5], '\n')
print (corr['G3'].sort_values(ascending=False)[-5:])
dataNoNull = dataNoNull.drop(['goout', 'Mjob', 'age', 'higher', 'failures'], axis=1)

#make new train test split using updated data
xdata = dataNoNull.drop(['G3'], axis=1)
ydata = dataNoNull['G3']
X_train, X_test, y_train, y_test = train_test_split(
                                    xdata, ydata, random_state=42, test_size=.33)

#Set up linear regression model for updated data
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)

#RMSE test
predictions = model.predict(X_test)
print('RMSE after is: \n', mean_squared_error(y_test, predictions))

#R squared test
print("R^2 after is: \n", model.score(X_test, y_test))

#slight increase in r squared value after removing least correlated items