import pandas as pd
import joblib
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler

# Load data
data_path = Path(__file__).parent.parent / "synthetic_fraud.csv"
df = pd.read_csv(data_path)

# Prepare features and target
X = df.drop('Class', axis=1)
y = df['Class']

# Scale features for logistic regression
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create models directory if it doesn't exist
models_dir = Path(__file__).parent.parent / "backend" / "models"
models_dir.mkdir(parents=True, exist_ok=True)

# Train Logistic Regression
print("Training Logistic Regression...")
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_scaled, y)
lr_path = models_dir / "logistic_regression.pkl"
joblib.dump(lr_model, lr_path)
print(f"✓ Saved: {lr_path}")

# Train XGBoost
print("Training XGBoost...")
xgb_model = XGBClassifier(n_estimators=100, random_state=42, verbosity=0)
xgb_model.fit(X, y)
xgb_path = models_dir / "xgboost_model.pkl"
joblib.dump(xgb_model, xgb_path)
print(f"✓ Saved: {xgb_path}")

print("\n✓ Model training complete!")
