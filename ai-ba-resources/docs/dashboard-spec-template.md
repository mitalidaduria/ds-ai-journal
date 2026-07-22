# Dashboard Specification Template

## 1. Dashboard name and purpose
- **Dashboard name:** [Insert dashboard name]
- **Purpose:** [Describe what decision the dashboard supports and why it matters]
- **Business outcome:** [State the operational, financial, or customer impact of using this dashboard]

## 2. Target audience and their decision context
- **Primary audience:** [Who uses the dashboard most often?]
- **Secondary audience:** [Who else relies on it?]
- **Decision context:** [What questions does the audience try to answer?]
- **Typical actions:** [What decisions or interventions are triggered from this dashboard?]

## 3. Metrics inventory
| Metric | Definition | Formula | Source | Granularity | Refresh rate |
|---|---|---|---|---|---|
| [Metric name] | [Plain-language definition] | [Calculation] | [System/table/source] | [Hourly/daily/real-time/etc.] | [Every X minutes/hours] |

## 4. Chart type for each metric with justification
- **[Metric name]:** [Chart type] — [Why this chart is appropriate for the metric and decision context]

## 5. Filters and dimensions
- **Filters:** [Time range, region, payment method, customer segment, etc.]
- **Dimensions:** [Breakdowns available for analysis, e.g. merchant, gateway, region, channel]
- **Default view:** [Default filters and drill-down behavior]

## 6. Alerting rules
- **Alert name:** [Describe the alert]
- **Condition:** [Threshold or change condition]
- **Window:** [Time period over which the condition is evaluated]
- **Severity:** [Info, warning, critical]
- **Notification channel:** [Pager, Slack, email, etc.]

## 7. Data freshness SLA
- **Expected freshness:** [How quickly data should appear after source updates]
- **SLA target:** [e.g. data available within 15 minutes of source event]
- **Operational impact if missed:** [What happens if freshness is not met?]

## 8. Acceptance criteria for launch
- Dashboard loads within [X] seconds for the default view
- All core metrics are available and match the agreed definitions
- Charts render correctly for the default and common filter combinations
- Alerts fire correctly and route to the correct on-call channel
- Data freshness meets the stated SLA during normal operations

---

# Worked Example: Payment Operations Dashboard

## 1. Dashboard name and purpose
- **Dashboard name:** Payment Operations Dashboard
- **Purpose:** Help payment operations teams monitor transaction health, detect declines in success rates, and quickly troubleshoot issues affecting customer payments.
- **Business outcome:** Reduce failed transactions, protect revenue, and improve customer trust by surfacing payment health issues early.

## 2. Target audience and their decision context
- **Primary audience:** Payment operations analysts and on-call engineers
- **Secondary audience:** Finance operations and product managers
- **Decision context:** Determine whether payment performance is healthy, identify emerging failures, and decide when to escalate issues to engineering or payment partners.
- **Typical actions:** Investigate sudden drops in payment success, review hourly trends, and confirm whether an incident needs immediate escalation.

## 3. Metrics inventory
| Metric | Definition | Formula | Source | Granularity | Refresh rate |
|---|---|---|---|---|---|
| Payment Success Rate | Percentage of initiated transactions that complete successfully | count(status='SUCCESS') / count(*) * 100 | transactions table in Redshift | Hourly | Every 15 minutes |
| Payment Volume | Total number of initiated transactions | count(*) | transactions table in Redshift | Hourly | Every 15 minutes |
| Failed Transactions | Number of transactions that did not complete successfully | count(status != 'SUCCESS') | transactions table in Redshift | Hourly | Every 15 minutes |

## 4. Chart type for each metric with justification
- **Payment Success Rate:** Line chart with a 7-day rolling window — this makes gradual trends and sudden drops easy to see over time.
- **Payment Volume:** Line chart or stacked bar chart — useful for comparing transaction load against success rate and identifying whether failures coincide with traffic spikes.
- **Failed Transactions:** Bar chart or line chart — helps operations teams quickly spot absolute spikes in failures and correlate them with incidents.

## 5. Filters and dimensions
- **Filters:** Time range, region, payment method, gateway, merchant, status category
- **Dimensions:** Region, payment method, gateway, merchant, channel, transaction type
- **Default view:** Last 24 hours, all regions, all payment methods, with an hourly breakdown

## 6. Alerting rules
- **Alert name:** Payment Success Rate Drop
- **Condition:** If payment success rate drops below 97% for 2 consecutive hours
- **Window:** 2-hour rolling window
- **Severity:** Critical
- **Notification channel:** Pager to on-call engineer and Slack alert to operations channel

## 7. Data freshness SLA
- **Expected freshness:** Data should be available within 15 minutes of source updates.
- **SLA target:** 95% of hourly aggregates refreshed within 15 minutes.
- **Operational impact if missed:** Delayed visibility into payment issues could postpone incident response and increase customer impact.

## 8. Acceptance criteria for launch
- Dashboard loads within 5 seconds for the default view
- Payment Success Rate, payment volume, and failed transaction metrics are visible and align with the agreed definitions
- The line chart correctly displays the 7-day rolling view and updates every 15 minutes
- The alert fires when the success rate remains below 97% for 2 consecutive hours
- Data freshness meets the 15-minute SLA during normal operations
