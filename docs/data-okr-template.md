# Data Product OKR Framework & Examples

## The 3-Quarter Data Product OKR Template

### Quarter 1: Data Quality & Reliability Focus
* **Objective:** [State the data reliability or quality goal here]
* **Key Result 1:**
    * **Metric:** [e.g., Latency, Error Rate, Completeness %]
    * **Current Baseline:** * **Target:** * **Measurement Method:** [e.g., Datadog logs, CloudWatch metrics, Snowflake audit tables]
* **Key Result 2:**
    * **Metric:** * **Current Baseline:** * **Target:** * **Measurement Method:** *
    * **Key Result 3:**
    * **Metric:** * **Current Baseline:** * **Target:** * **Measurement Method:** ---

### Quarter 2: Adoption & Platform Integration Focus
* **Objective:** [State the team onboarding or consumption goal here]
* **Key Result 1:**
    * **Metric:** [e.g., Active Downstream Teams, API requests, Time-to-Insight]
    * **Current Baseline:** * **Target:** * **Measurement Method:** * **Key Result 2:**
    * **Metric:** * **Current Baseline:** * **Target:** * **Measurement Method:** * **Key Result 3:**
    * **Metric:** * **Current Baseline:** * **Target:** * **Measurement Method:** ---

### Quarter 3: Downstream Business Impact Focus
* **Objective:** [State how the data product moves business metrics like revenue or fraud reduction]
* **Key Result 1:**
    * **Metric:** [e.g., Model F1 Score, Operational Dollars Saved, Incident Response Time]
    * **Current Baseline:** * **Target:** * **Measurement Method:** * **Key Result 2:**
    * **Metric:** * **Current Baseline:** * **Target:** * **Measurement Method:** * **Key Result 3:**
    * **Metric:** * **Current Baseline:** * **Target:** * **Measurement Method:** ---

## Worked Example: Payment Anomaly Detection Data Product

### Q1 Focus: Making Data Pipeline Production-Ready
* **Objective:** Make payment anomaly data reliable enough for real-time downstream decisioning.
* **Key Result 1:**
    * **Metric:** Pipeline P99 Latency
    * **Current Baseline:** 45 seconds
    * **Target:** Under 5 seconds
    * **Measurement Method:** Kafka pipeline end-to-end telemetry logging.
* **Key Result 2:**
    * **Metric:** Data Completeness (Gateway fields)
    * **Current Baseline:** 94.2%
    * **Target:** ≥99.5% for all critical gateway fields
    * **Measurement Method:** Great Expectations automated data quality check suite.
* **Key Result 3:**
    * **Metric:** Platform Adoption
    * **Current Baseline:** 0 downstream ML models
    * **Target:** Onboard 3 downstream ML production models consuming the anomaly feed live
    * **Measurement Method:** API Gateway / Schema Registry client access logs.
