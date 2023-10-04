#Titanic dataset predictions
import numpy as np
#import panda library and a few others we will need.
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.svm import SVC

# skipping the header
data =pd.read_csv( 'titanic_800.csv' , sep = ',' , header = 0 )

# show the data
# print ( data.describe( include = 'all' ))
#the describe is a great way to get an overview of the data
# print ( data .values)

# Replace unknown values. Unknown class set to 3
data["Pclass"].fillna(3, inplace = True)

# # Replace unknown values. Unknown age set to 25
data["Age"].fillna(29, inplace = True)
# #data["Age"].replace("", np.nan, inplace=True)
# # data.dropna(how='any', axis=0, inplace=True)

# Replace sex with numbers
data['Sex'] = data['Sex'].replace(['female'],1.0 )
data['Sex'] = data['Sex'].replace(['male'],0.0 )

# Replace unknown values with 0
data["SibSp"].fillna(0, inplace = True)

# Replace unknown values with 0
data["Parch"].fillna(0, inplace = True)

# Replace embark town letter with numbers
data["Embarked"].fillna(2.0, inplace = True)
data['Embarked'] = data['Embarked'].replace(['C'],1.0 )
data['Embarked'] = data['Embarked'].replace(['Q'],2.0 )
data['Embarked'] = data['Embarked'].replace(['S'],3.0 )

# Replace unknown values. Unknown survival set to survived
data["Survived"].fillna(1, inplace = True)

yvalues = pd.DataFrame( dict ( Survived =[]), dtype = int )
yvalues[ "Survived" ] = data [ "Survived" ].copy()
#now the yvalues should contain just the survived column

# x = data[ "Age" ]
# y = data[ "Pclass" ]
# plt.figure()
# plt.scatter(x.values, y.values, color = 'black' , s = 20 )
# plt.show()

#now we can delete the survived column from the data (because
#we have copied that already into the yvalues.
data.drop( 'Survived' , axis = 1 , inplace = True )

data.drop( 'PassengerId' , axis = 1 , inplace = True )

data.drop( 'Name' , axis = 1 , inplace = True )

data.drop( 'Ticket' , axis = 1 , inplace = True )

data.drop( 'Fare' , axis = 1 , inplace = True )

data.drop( 'Cabin' , axis = 1 , inplace = True )

# show the data
#print ( data.describe( include = 'all' ))

xtrain, xtest, ytrain, ytest = train_test_split(data, yvalues, test_size=0.20)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(xtrain)
scaler.transform(xtrain)
scaler.transform(xtest)

from sklearn.neural_network import MLPClassifier

# MLP = MLPClassifier(hidden_layer_sizes=(20, 10, 6), max_iter=1000, random_state=0)
#
# MLP.fit(xtrain, ytrain.values.ravel())
#
# predictions = MLP.predict(xtest)
#
# matrix = confusion_matrix(ytest, predictions)
# print(matrix)
#
# print(classification_report(ytest, predictions))

# Experiments
svm_rbf = SVC(kernel='rbf', C= 100, random_state=0)

svm_rbf.fit(xtrain, ytrain.values.ravel())

predictions = svm_rbf.predict(xtest)

matrix = confusion_matrix(ytest, predictions)
print(matrix)

print(classification_report(ytest, predictions))


