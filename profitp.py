# -*- coding: utf-8 -*-
"""profitp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_Vb34Y6EbOfyp_CpSJlXHHgYbLoju58Q
"""

import numpy as np # mathematical calculations
import matplotlib.pyplot as plt # for ploting
import pandas as pd # for handling dataset
import seaborn as sns # graps,statistical
import sklearn # for model evaluation-regression model

from google.colab import drive
drive.mount('/content/drive')

dataset = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/50_Startups.csv')

dataset.head()

dataset.tail()

dataset.describe()

print('There are ',dataset.shape[0],'rows and ',dataset.shape[1],'columns in the dataset.')

print('There are',dataset.duplicated().sum(),'duplicate values in the dateset.') #using duplicated() pre-defined function

dataset.isnull().sum()

dataset.info()

c = dataset.corr()
c

#direct correlation with profit
sns.heatmap(c,annot=True,cmap='Blues')
plt.show()

# relationship between them where the variables can be continuous or categorical.
sns.pairplot(dataset)
plt.show()

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

from sklearn.preprocessing import LabelEncoder

labelencoder = LabelEncoder() # non-num to num labl
X[:, 2] = labelencoder.fit_transform(X[:, 2])
X1 = pd.DataFrame(X) 
X1.head()

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(X,y,train_size=0.7,random_state=0)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x_train,y_train) # adjusts weights according to data values so that better accuracy can be achieved.
print('Model has been trained successfully')

y_pred = model.predict(x_test)
y_pred

testing_data_model_score = model.score(x_test, y_test)
print("Model Score/Performance on Testing data",testing_data_model_score)

training_data_model_score = model.score(x_train, y_train)
print("Model Score/Performance on Training data",training_data_model_score)

"""# New section"""

df = pd.DataFrame(data={'Predicted value':y_pred.flatten(),'Actual Value':y_test.flatten()})#narrow format ^ comp spd
df

from sklearn.metrics import r2_score

r2Score = r2_score(y_pred, y_test)
print("R2 score of model is :" ,r2Score*100)

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_pred, y_test)
print("Mean Squarred Error is :" ,mse*100)

rmse = np.sqrt(mean_squared_error(y_pred, y_test))
print("Root Mean Squarred Error is : ",rmse*100)

from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_pred,y_test)
print("Mean Absolute Error is :" ,mae)