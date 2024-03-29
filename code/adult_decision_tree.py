import numpy as np
# import graphviz as gviz
from sklearn import tree
from helpers.datasets import adult
from sklearn.metrics import accuracy_score, f1_score

# Loading the learning set
adult_data = adult.load("learning", encode_features=True)
adult_data = adult.to_numpy_array(adult_data, remove_missing_values=True)

# Separating to target and features
adult_targets = adult_data[:, -1]
adult_data = adult_data[:, 0:-1]

# Training the classifier
clf = tree.DecisionTreeClassifier(max_depth=3, criterion="entropy")
clf = clf.fit(adult_data, adult_targets)


# Loading the test set
adult_test = adult.load("testing", encode_features=True)
adult_test = adult.to_numpy_array(adult_test, remove_missing_values=True)

adult_test_targets = adult_test[:, -1]
adult_test_features = adult_test[:, 0:-1]

# predicting
adult_test_preds = clf.predict(adult_test_features)


print("Accuracy is: {0:3.2f}%".format(accuracy_score(adult_test_targets, adult_test_preds) * 100))
print("F-1 score is: {0:3.2f}%".format(f1_score(adult_test_targets, adult_test_preds) * 100))


# Drawing the decision tree
# dot_data = tree.export_graphviz(clf, out_file=None,
#                                 feature_names=adult.feature_names,
#                                 filled=True, rounded=True,
#                                 special_characters=True,
#                                 max_depth=5)
# graph = gviz.Source(dot_data)
# graph.render("Adult")


# Evaluating demographic parity and equality of opportunity
adult_test = adult.load("testing", encode_features=True)
adult_test = adult.to_numpy_array(adult_test, remove_missing_values=True)

adult.evaluate_fairness(adult_test, adult_test_preds, adult_test_targets, clf, adult)
