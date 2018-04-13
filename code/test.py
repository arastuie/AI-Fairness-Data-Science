import numpy as np
import pandas as pd
import graphviz as gviz
from sklearn import tree
import helpers.datasets.adult as adult
from sklearn.metrics import accuracy_score

adult_data = adult.load(adult.data_path, encode_labels=True)
adult_data = adult.to_numpy_array(adult_data, remove_missing_values=True)

adult_targets = adult_data[:, -1]
adult_data = adult_data[:, 0:-1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(adult_data, adult_targets)

adult_test = adult.load(adult.test_path, encode_labels=True)
adult_test = adult.to_numpy_array(adult_test, remove_missing_values=True)

adult_test_targets = adult_test[:, -1]
adult_test = adult_test[:, 0:-1]

adult_test_preds = clf.predict(adult_test)

print(accuracy_score(adult_test_targets, adult_test_preds))

dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=adult.feature_names,
                                filled=True, rounded=True,
                                special_characters=True,
                                max_depth=5)
graph = gviz.Source(dot_data)
graph.render("Adult")
