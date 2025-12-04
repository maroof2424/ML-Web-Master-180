import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

X, y = load_iris(return_X_y=True)
clf = RandomForestClassifier().fit(X, y)

pickle.dump(clf, open("model.pkl", "wb"))
