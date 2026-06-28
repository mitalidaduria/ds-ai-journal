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

# ── Demonstrate type coercion risk ────────────
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
