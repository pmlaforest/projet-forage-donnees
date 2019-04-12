import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.model_selection  import GridSearchCV
from sklearn.metrics import classification_report
from sklearn import tree
from sklearn.metrics import accuracy_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.dummy import DummyClassifier

from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder,LabelEncoder

from numpy import array
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron

from sklearn.metrics import confusion_matrix

import graphviz

def main():

    df = pd.read_csv('agaricus-lepiota.csv')
    createTestandTrainSets(df)
    dummyClassifier()
    CASTDecisionTree()
    naiveBayes()
    perceptron()
    printClassifiersPerformances()
    print('end of script')
    return

def createTestandTrainSets(df):

    global X_train, X_test, y_train, y_test

    y = df['edibility']
    X = df.drop(['edibility'], axis=1)

    # Categorical boolean mask
    categorical_feature_mask = X.dtypes==object

    # filter categorical columns using mask and turn it into a list
    categorical_cols = X.columns[categorical_feature_mask].tolist()

    le = LabelEncoder()
    X[categorical_cols] = X[categorical_cols].apply(lambda col: le.fit_transform(col))
    X[categorical_cols].head(10)
    y_trans = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y_trans, test_size=0.25, random_state=33)

    return

def perceptron():

    global X_train, X_test, y_train, y_test, perceptronEncodedPredictions, perceptronClf

    perceptronClf = Perceptron(tol=1e-3, random_state=0)
    perceptronClf.fit(X_train, y_train)
    perceptronEncodedPredictions = perceptronClf.predict(X_test)

    return

def dummyClassifier():

    global X_train, X_test, y_train, y_test, dummyClassifierEncodedPredictions, dcClf

    dcClf  = DummyClassifier(strategy='most_frequent')
    dcClf.fit(X_train, y_train)
    dummyClassifierEncodedPredictions = dcClf.predict(X_test)

    return

def CASTDecisionTree():
    
    global X_train, X_test, y_train, y_test, CASTEncodedPredictions, CASTClf

    CASTClf = DecisionTreeClassifier(criterion='entropy')
    CASTClf.fit(X_train, y_train)
    CASTEncodedPredictions = CASTClf.predict(X_test)

    return

def naiveBayes():

    global X_train, X_test, y_train, y_test, naiveBayesEncodedPredictions, naiveBayesClf

    naiveBayesClf  = GaussianNB()
    naiveBayesClf.fit(X_train.values, y_train)
    naiveBayesEncodedPredictions = naiveBayesClf.predict(X_test.values)

    return


def printClassifiersPerformances():

    print('')
    print('Dummy Classifier')
    print('----------------')
    print(classification_report(y_test, dummyClassifierEncodedPredictions, target_names=['e', 'p']))
    print('accuracy score: ', accuracy_score(y_test, dummyClassifierEncodedPredictions))
    print('cross-validation: ', cross_val_score(dcClf, X_train, y_train, cv=10))
    print('confusion matrix: ', confusion_matrix(y_test, dummyClassifierEncodedPredictions))
        
    print('')
    print('CAST Classifier')
    print('---------------')
    print(classification_report(y_test, CASTEncodedPredictions, target_names=['e', 'p']))
    print('accuracy score', accuracy_score(y_test, CASTEncodedPredictions))
    print('cross-validation: ', cross_val_score(CASTClf, X_train, y_train, cv=10))
    print('confusion matrix: ', confusion_matrix(y_test, CASTEncodedPredictions))

    dot_data = tree.export_graphviz(CASTClf, out_file=None, 
            feature_names=list(X_train.columns),
            label=['e', 'p'],           
            filled=True, 
            rounded=True,  
            special_characters=True)  

    graph = graphviz.Source(dot_data) 
    graph.render('agaricus_lepiota_CAST_tree') 

    print('')
    print('naiveBayes classifier')
    print('---------------------')
    print(classification_report(y_test, naiveBayesEncodedPredictions, target_names=['e', 'p']))
    print('accuracy score', accuracy_score(y_test, naiveBayesEncodedPredictions))
    print('cross-validation: ', cross_val_score(naiveBayesClf, X_train, y_train, cv=10))
    print('confusion matrix: ', confusion_matrix(y_test, naiveBayesEncodedPredictions))

    print('')
    print('perceptron classifier')
    print('---------------------')
    print(classification_report(y_test, perceptronEncodedPredictions, target_names=['e', 'p']))
    print('accuracy score', accuracy_score(y_test, perceptronEncodedPredictions))
    print('cross-validation: ', cross_val_score(perceptronClf, X_train, y_train, cv=10))
    print('confusion matrix: ', confusion_matrix(y_test, perceptronEncodedPredictions))

    return

main()