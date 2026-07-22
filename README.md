# ds-ai-journal
Companion notebooks and notes Data Science AI Machine Learning


## Journal Index

Descriptive Statistics & NumPy | Mean vs. Median (Outlier handling), Standard Deviation ($\sigma$), Percentiles (P95 metrics), Anomaly Detection

## Tech Stack & Tools
Languages: Python
Libraries: NumPy, Pandas (Upcoming)
Frameworks: Data Governance, MDM, Data Quality Engineering

## Model Selection Guidance

As a Data PM, choose TF-IDF + traditional ML when:
- volume is extremely high (cost sensitivity)
- interpretability is required (you need to explain why a complaint was classified as fraud)
- latency is critical (< 10ms)

Choose LLM when:
- the categories are nuanced or context-dependent
- training data is scarce
- the input language is highly variable
