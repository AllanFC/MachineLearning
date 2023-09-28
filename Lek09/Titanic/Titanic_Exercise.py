# Titanic dataset predictions

# import panda library and a few others we will need.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

# skipping the header
data = pd.read_csv('titanic_train_500_age_passengerclass.csv', sep=',', header=0)

# show the data
# print(data.describe(include='all'))
# the describe is a great way to get an overview of the data
# print(data.values)
# data["Age"].replace("", np.nan, inplace=True)
# data.dropna(how='any', axis=0, inplace=True)

# Replace unknown values. Unknown class set to 3
data["Pclass"].fillna(3, inplace=True)

# Replace unknown values. Unknown age set to 25
data["Age"].fillna(29, inplace=True)

# Replace unknown values. Unknown survival set to survived
data["Survived"].fillna(1, inplace=True)

yvalues = pd.DataFrame(dict(Survived=[]), dtype=int)
yvalues["Survived"] = data["Survived"].copy()
# now the yvalues should contain just the survived column

x = data["Age"]
y = data["Pclass"]
plt.figure()
plt.scatter(x.values, y.values, color='black', s=20)
# plt.show()

# now we can delete the survived column from the data (because
# we have copied that already into the yvalues.
data.drop('Survived', axis=1, inplace=True)

data.drop('PassengerId', axis=1, inplace=True)

# show the data
# print(data.describe(include='all'))

# Split in train and test set
from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(data, yvalues, test_size=0.20)

# xtrain = data.head(400)
# xtest = data.tail(100)
#
# ytrain = yvalues.head(400)
# ytest = yvalues.tail(100)

# print(ytrain)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(xtrain)
scaler.transform(xtrain)
scaler.transform(xtest)

from sklearn.neural_network import MLPClassifier

MLP = MLPClassifier(hidden_layer_sizes=(10, 8, 8, 4), max_iter=1000, random_state=0)

# 10, 8, 8, 4 62-74%

MLP.fit(xtrain, ytrain.values.ravel())

predictions = MLP.predict(xtest)

matrix = confusion_matrix(ytest, predictions)
print(matrix)

print(classification_report(ytest, predictions))
