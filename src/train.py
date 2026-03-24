import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

from utils import evaluate

# Load dataset
df = pd.read_csv("../data/processed/dataset.csv")

# Features & target
X = df.drop(columns=["power", "file"], errors="ignore")
y = df["power"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scaling (important for SVR & KNN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Models
models = {
    "SVR": SVR(),
    "KNN": KNeighborsRegressor(),
    "RandomForest": RandomForestRegressor(n_estimators=100),
    "XGBoost": XGBRegressor(
    n_estimators=200,
    max_depth=4,
    learning_rate=0.1
  )
}

results = []

for name, model in models.items():
    if name in ["SVR", "KNN"]:
        model.fit(X_train_scaled, y_train)
        preds = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

    mae, mse, rmse = evaluate(y_test, preds)

    results.append({
        "Model": name,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse
    })

# Save results
results_df = pd.DataFrame(results)
results_df.to_csv("../results/metrics.csv", index=False)

print(results_df)