import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("patients_data.csv")

# Split features and labels
X = df.drop('label', axis=1)
y = df['label']

# Standardize features (important for KNN)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split for safety (you can skip this if training on full data)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Input from user
print("\nEnter the new patient's symptom features:")
input_features = []
for feature in X.columns:
    val = float(input(f"  {feature}: "))
    input_features.append(val)

k = int(input("\nEnter the value of k (number of neighbors): "))

# Prepare input for prediction
input_scaled = scaler.transform([input_features])

# KNN classifier
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)

# Predict
prediction = model.predict(input_scaled)[0]

# Output result
print("\n🔍 Prediction Result:")
if prediction == 1:
    print("✅ The patient **has** the medical condition.")
else:
    print("❌ The patient **does not** have the medical condition.")
