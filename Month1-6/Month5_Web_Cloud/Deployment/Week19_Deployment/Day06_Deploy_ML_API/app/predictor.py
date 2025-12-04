import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

def predict_flower(data):
    arr = np.array(data).reshape(1, -1)
    return int(model.predict(arr)[0])
