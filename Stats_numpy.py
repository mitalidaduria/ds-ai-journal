##### Descriptive Stats with Numpy

import numpy as np

# Simulated payment transaction amounts (INR)

txn_amounts = np.array([150, 299, 450, 1200, 899, 75, 4500, 250, 180, 620, 980, 3200, 90, 750, 1100, 550, 8900, 420])

# Central Tendency
###( When analyzing business metrics like user transaction values, platform latency, or system processing times, always check the median. The mean can easily lie to you if a few massive outliers skew the data.)
print("Mean:", np.mean(txn_amounts).round(2))  #average
print("Median:", np.median(txn_amounts))       # middle value

# Why median matters: one 8900 outlier skews the mean upward
# For payment data, median is often more representative

# Spread

print("Std dev:", np.std(txn_amounts).round(2))
print("Min:", txn_amounts.min(), "Max:", txn_amounts.max())

# Percentiles

print("P50:", np.percentile(txn_amounts, 50))
print("P95:", np.percentile(txn_amounts, 95)) # P95 latency = 95% of transactions complete faster than this.
# Useful for defining NFR acceptance criteria

# Data Quality Flag
threshold = np.mean(txn_amounts) + 3*np.std(txn_amounts)
outliers = txn_amounts[txn_amounts > threshold]
print(f"Outliers (>3σ): {outliers}")
