import numpy as np
import pandas as pd

data_path = "../datasets/adult/adult.data.txt"
test_path = "../datasets/adult/adult.test.txt"


def load(path, encode_labels=False, verbose=False):
    feature_names = ["Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Martial Status", "Occupation",
                     "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss", "Hours per week", "Country",
                     "Target"]

    if not encode_labels:
        adult_data = pd.read_csv(path, names=feature_names, sep=r'\s*,\s*', engine='python', na_values="?",
                                 verbose=verbose)

        return adult_data

    dframe = {"Workclass": ["Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov", "State-gov",
                            "Without-pay", "Never-worked"],
              "Education": ["Bachelors", "Some-college", "11th", "HS-grad", "Prof-school", "Assoc-acdm", "Assoc-voc",
                            "9th", "7th-8th", "12th", "Masters", "1st-4th", "10th", "Doctorate", "5th-6th",
                            "Preschool"],
              "Martial Status": ["Married-civ-spouse", "Divorced", "Never-married", "Separated", "Widowed",
                                 "Married-spouse-absent", "Married-AF-spouse"],
              "Occupation": ["Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial",
                             "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical",
                             "Farming-fishing", "Transport-moving", "Priv-house-serv", "Protective-serv",
                             "Armed-Forces"],
              "Relationship": ["Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", "Unmarried"],
              "Race": ["White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"],
              "Sex": ["Female", "Male"],
              "Country": ["United-States", "Cambodia", "England", "Puerto-Rico", "Canada", "Germany",
                          "Outlying-US(Guam-USVI-etc)", "India", "Japan", "Greece", "South", "China", "Cuba", "Iran",
                          "Honduras", "Philippines", "Italy", "Poland", "Jamaica", "Vietnam", "Mexico", "Portugal",
                          "Ireland", "France", "Dominican-Republic", "Laos", "Ecuador", "Taiwan", "Haiti", "Columbia",
                          "Hungary", "Guatemala", "Nicaragua", "Scotland", "Thailand", "Yugoslavia", "El-Salvador",
                          "Trinadad&Tobago", "Peru", "Hong", "Holand-Netherlands"],
              "Target": [">50K", "<=50K"]}

    encoders = {"Workclass": lambda x: dframe['Workclass'].index(x) if not pd.isnull(x) else x,
                "Education": lambda x: dframe['Education'].index(x) if not pd.isnull(x) else x,
                "Martial Status": lambda x: dframe['Martial Status'].index(x) if not pd.isnull(x) else x,
                "Occupation": lambda x: dframe['Occupation'].index(x) if not pd.isnull(x) else x,
                "Relationship": lambda x: dframe['Relationship'].index(x) if not pd.isnull(x) else x,
                "Race": lambda x: dframe['Race'].index(x) if not pd.isnull(x) else x,
                "Sex": lambda x: dframe['Sex'].index(x) if not pd.isnull(x) else x,
                "Country": lambda x: dframe['Country'].index(x) if x is not None else x,
                "Target": lambda x: dframe['Target'].index(x.replace('.', '')) if not pd.isnull(x) else x}

    adult_data = pd.read_csv(path, names=feature_names, converters=encoders, sep='\s*,\s*', engine='python',
                             na_values="?", verbose=verbose)

    return adult_data


def to_numpy_w_no_missing_value(panda_data_frame):
    np_data = panda_data_frame.as_matrix()

    # Deleting rows with empty values
    np_data = np_data[~pd.isnull(np_data).any(axis=1)].astype(int)

    return np_data