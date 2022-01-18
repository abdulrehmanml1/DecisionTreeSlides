

import pandas as pd


# import tree from sklearn 
from sklearn import tree



# load the  dataset 
df = pd.read_csv('weat.csv')






# store the feature matrix (X) and response vector (y) 
X =df.iloc[:,:-1].values
Y =df.iloc[:,4].values



#Transformation of x Data into Numeric data
from sklearn.preprocessing import LabelEncoder ,OneHotEncoder


labelencoder_X_1=LabelEncoder()
X[:,0]=labelencoder_X_1.fit_transform(X[:,0])
OneHotencoder_1=OneHotEncoder(categorical_features=[0])

labelencoder_X_2=LabelEncoder()
X[:,1]=labelencoder_X_2.fit_transform(X[:,1])
OneHotencoder_2=OneHotEncoder(categorical_features=[1])

labelencoder_X_3=LabelEncoder()
X[:,2]=labelencoder_X_2.fit_transform(X[:,2])
OneHotencoder_3=OneHotEncoder(categorical_features=[2])

labelencoder_X_4=LabelEncoder()
X[:,3]=labelencoder_X_2.fit_transform(X[:,3])
OneHotencoder_4=OneHotEncoder(categorical_features=[3])

X=OneHotencoder_1.fit_transform(X).toarray()
X=OneHotencoder_2.fit_transform(X).toarray()
X=OneHotencoder_3.fit_transform(X).toarray()
X=OneHotencoder_4.fit_transform(X).toarray()

labelencoder_Y=LabelEncoder()
Y=labelencoder_Y.fit_transform(Y)


# splitting X and y into training and testing sets -
# test_size = size of test data
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2) 
  




# Initialize model
tree_model = tree.DecisionTreeClassifier(criterion="entropy")


tree_model.fit(X_train, y_train)



#predict the test data , without label
y_pred = tree_model.predict(X_test)


from sklearn.metrics import accuracy_score 



# comparing actual response values (y_test) with predicted response values (y_pred) 

print("Model accuracy(in %):", accuracy_score(y_test, y_pred)*100)


