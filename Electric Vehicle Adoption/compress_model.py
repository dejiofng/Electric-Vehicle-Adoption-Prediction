import pickle
import joblib

with open("model.pickle", "rb") as f:
    model = pickle.load(f)

joblib.dump(model, "model.joblib", compress=9)

print("Model compressed successfully!")