import numpy as np
from sklearn import svm
from helpers.datasets import adult
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV


# Loading the learning set
adult_data = adult.load("learning", encode_features=True)
adult_data = adult.to_numpy_array(adult_data, remove_missing_values=True)

# Separating to target and features
adult_targets = adult_data[:, -1]
adult_data = adult_data[:, 0:-1]

# Grid search on SVC
# param_grid = [{'kernel': ['rbf'], 'gamma': [1e-2, 1e-3, 1e-4, 1e-5], 'C': [0.01, 0.1, 1, 5, 10, 50, 100, 1000]},
#               {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]
#
#
# clf = make_pipeline(StandardScaler(), GridSearchCV(svm.SVC(), param_grid=param_grid, n_jobs=6, cv=5, refit=True))
# clf.fit(adult_data, adult_targets)
# print("Best parameters set found on development set:\n")
# c = clf.named_steps.gridsearchcv.best_params_
# print(c)

# Training the classifier -- This gets an accuracy of 84.39%
clf = make_pipeline(StandardScaler(), svm.SVC(kernel="rbf", C=100, gamma=0.001))
clf.fit(adult_data, adult_targets)

# Loading the test set
adult_test = adult.load("testing", encode_features=True)
adult_test = adult.to_numpy_array(adult_test, remove_missing_values=True)

adult_test_targets = adult_test[:, -1]
adult_test_features = adult_test[:, 0:-1]

# predicting
adult_test_preds = clf.predict(adult_test_features)

print("Accuracy is: {0:3.2f}%".format(accuracy_score(adult_test_targets, adult_test_preds) * 100))

# Evaluating demographic parity and equality of opportunity
adult_test = adult.load("testing", encode_features=True)
adult_test = adult.to_numpy_array(adult_test, remove_missing_values=True)

adult.evaluate_fairness(adult_test, adult_test_preds, adult_test_targets, clf, adult)
