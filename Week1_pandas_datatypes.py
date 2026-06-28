import pandas as pd
import numpy as np

def profile_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Returns a data quality summary for any DataFrame."""
    profile = []
    for col in df.columns:
        null_count = df[col].isnull().sum()
        profile.append({
            'column': col,
            'dtype': str(df[col].dtype),
            'null_count': null_count,
            'null_pct': (null_count / len(df) * 100).round(2),
            'unique': df[col].nunique(),
            'sample': str(df[col].dropna().iloc[0]) if null_count < len(df) else 'ALL NULL'
        })
    return pd.DataFrame(profile)

# ── DEMONSTRATE TYPE COERCION RISK ──────────────────────────────────
# Creating a dummy raw dataset with mixed types
df_raw = pd.DataFrame({
    'txn_id':    ['T001', 'T002', 'T003'],
    'amount':    ['1200', '450.5', 'N/A'],  # ← Looks numeric, but it's text
    'timestamp': ['2024-01-15', '2024-01-16', '2024-01-17']
})

print("--- Before Cleaning ---")
print(profile_dataframe(df_raw))
print("\n" + "="*50 + "\n")

# Fix: Convert types explicitly to unleash proper data analysis
# errors='coerce' turns the string 'N/A' into a proper float NaN (null)
df_raw['amount']    = pd.to_numeric(df_raw['amount'], errors='coerce')
df_raw['timestamp'] = pd.to_datetime(df_raw['timestamp'])

print("--- After Cleaning ---")
print(profile_dataframe(df_raw))
print("\n" + "="*50 + "\n")


# ── STEP 3: APPLY TO PAYMENTS DATA & OPTIMIZE CATEGORIES ────────────
# Simulating the payments dataset with a highly repetitive text column
df_payments = pd.DataFrame({
    'transaction_id': [f'TXN_{i}' for i in range(1000)],
    'hour':           ['14:00', '09:00', '14:00', '21:00', '09:00'] * 200, 
    'amount':         [150.50, 2300.00, 45.00, 99.99, 1200.00] * 200
})

print("--- Step 3: Initial Payments Profile ---")
print(profile_dataframe(df_payments))

# Check the exact memory footprint before optimization
mem_before = df_payments['hour'].memory_usage(deep=True)
print(f"Memory used by 'hour' as Object: {mem_before} bytes")
print("\n" + "-"*30 + "\n")

# Optimization: Convert 'hour' to a category dtype since it has low unique cardinality
df_payments['hour'] = df_payments['hour'].astype('category')

print("--- Step 3: Optimized Payments Profile ---")
print(profile_dataframe(df_payments))

# Check the exact memory footprint after optimization
mem_after = df_payments['hour'].memory_usage(deep=True)
print(f"Memory used by 'hour' as Category: {mem_after} bytes")

# Calculate and display optimization metrics
savings = ((mem_before - mem_after) / mem_before * 100).round(2)
print(f" Total Memory Saved for 'hour' column: {savings}%")
