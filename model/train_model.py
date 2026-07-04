import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Dataset Load
data = pd.read_csv("dataset/Crop_recommendation.csv")

# Features
X = data.drop("label", axis=1)

# Target
y = data["label"]

# Model
model = RandomForestClassifier()

# Train
model.fit(X, y)

# Save Model
with open("model/model.pkl", "wb") as file:
    pickle.dump(model, file)

print("✅ Model Trained Successfully!")