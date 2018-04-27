import numpy as np
from sklearn import svm
import helpers.datasets.adult as adult
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV


# Loading the learning set
adult_data = adult.load("learning", encode_features=True)
adult_data = adult.to_numpy_array(adult_data, remove_missing_values=True)

# Separating to target and features
adult_targets = adult_data[:, -1]
adult_data = adult_data[:, 0:-1]

param_grid = [{'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'gamma': [0.0001, 0.001, 0.1, 1], 'kernel': ['rbf']},
              {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'kernel': ['linear']}]

# Training the classifier
# svc = svm.SVC()
# clf = GridSearchCV(svc, param_grid=param_grid, n_jobs=5, cv=5)
# clf = clf.fit(adult_data, adult_targets)

clf = svm.SVC(kernel="linear", C=0.1)
clf.fit(adult_data, adult_targets)

print("Best parameters set found on development set:\n")
print(clf.best_params_)

# Loading the test set
adult_test = adult.load("testing", encode_features=True)
adult_test = adult.to_numpy_array(adult_test, remove_missing_values=True)

adult_test_targets = adult_test[:, -1]
adult_test_features = adult_test[:, 0:-1]

# predicting
adult_test_preds = clf.predict(adult_test_features)


print("Accuracy is: {0:3.2f}%".format(accuracy_score(adult_test_targets, adult_test_preds) * 100))
