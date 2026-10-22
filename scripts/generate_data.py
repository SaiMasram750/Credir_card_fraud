import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(42)

n_samples = 5000
n_legit = int(n_samples * 0.98)
n_fraud = n_samples - n_legit

# Generate legitimate transactions (Class 0)
legit_time = np.random.uniform(0, 172800, n_legit)
legit_v_features = np.random.normal(0, 1, (n_legit, 28))
legit_amount = np.random.exponential(50, n_legit)
legit_class = np.zeros(n_legit)

legit_data = np.column_stack([legit_time, legit_v_features, legit_amount, legit_class])

# Generate fraudulent transactions (Class 1) - with anomalous patterns
fraud_time = np.random.uniform(0, 172800, n_fraud)
fraud_v_features = np.random.normal(2, 2, (n_fraud, 28))  # Shifted distribution
fraud_amount = np.random.exponential(200, n_fraud)  # Larger amounts
fraud_class = np.ones(n_fraud)

fraud_data = np.column_stack([fraud_time, fraud_v_features, fraud_amount, fraud_class])

# Combine and shuffle
all_data = np.vstack([legit_data, fraud_data])
np.random.shuffle(all_data)

# Create DataFrame
columns = ['Time', 'Amount'] + [f'V{i}' for i in range(1, 29)] + ['Class']
columns = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount', 'Class']
df = pd.DataFrame(all_data, columns=columns)

# Save to project root
output_path = Path(__file__).parent.parent / "synthetic_fraud.csv"
df.to_csv(output_path, index=False)
print(f"✓ Dataset generated: {output_path}")
print(f"  - Total transactions: {len(df)}")
print(f"  - Legitimate: {len(df[df['Class'] == 0])}")
print(f"  - Fraudulent: {len(df[df['Class'] == 1])}")
