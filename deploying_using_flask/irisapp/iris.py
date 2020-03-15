
import flask
app = flask.Flask(import_name="irisapp")
#Import scikit-learn dataset library
from sklearn import datasets
from sklearn.preprocessing import RobustScaler


#Load dataset
iris = datasets.load_iris()

# print the label species(setosa, versicolor,virginica)
#print(iris.target_names)

# print the names of the four features
#print(iris.feature_names)

# print the iris data (top 5 records)
#print(iris.data[0:5])

# print the iris labels (0:setosa, 1:versicolor, 2:virginica)
#print(iris.target)

# Creating a DataFrame of given iris dataset.
import pandas as pd
data=pd.DataFrame({
    'sepal length':iris.data[:,0],
    'sepal width':iris.data[:,1],
    'petal length':iris.data[:,2],
    'petal width':iris.data[:,3],
    'species':iris.target
})
# Import train_test_split function
from sklearn.cross_validation import train_test_split

X=data[['petal length', 'petal width', 'sepal length', 'sepal width']]  # Features
robust_scaler = RobustScaler()
X= robust_scaler.fit_transform(X)
y=data['species']  # Labels

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test

#Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier

#Create a Gaussian Classifier
clf1=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf1.fit(X_train,y_train)

y_pred=clf1.predict(X_test)

#Import scikit-learn metrics module for accuracy calculation
#from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
#print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    
from collections import OrderedDict 

def predict_flower():
    num_one = flask.request.form["value1"]
    num1=float(num_one)
    num_two = flask.request.form["value2"]
    num2=float(num_two)
    num_three = flask.request.form["value3"]
    num3=float(num_three)
    num_four= flask.request.form["value4"]
    num4=float(num_four)
    new_flower = OrderedDict([('petal length',num1),
                          ('petal width',num2),
                          ('sepal length',num3),
                          ('sepal width',num4)])
    flower = pd.Series(new_flower)
    data = flower.values.reshape(1, -1)
    data = robust_scaler.transform(data)
    prediction = clf1.predict(data)
    for species in prediction:
        if species ==0:
            specie="Setosa"
            return flask.render_template(template_name_or_list="irisresult.html",predicted_species=specie)
        elif species==1:
            specie="Versicolor"
            return flask.render_template(template_name_or_list="irisresult.html",predicted_species=specie)
        elif species==2:
            specie="Virginica"
            return flask.render_template(template_name_or_list="irisresult.html",predicted_species=specie)
            
               
def homepage():
    return flask.render_template(template_name_or_list="iris.html")
app.add_url_rule(rule="/", view_func=homepage)                
    
app.add_url_rule(rule="/form", view_func=predict_flower, methods=["POST"])
app.run(host="127.0.0.5", port=6300,debug=True)   # 
