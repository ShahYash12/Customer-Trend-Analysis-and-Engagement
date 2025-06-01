# engagement_modeling.py

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/customer_events.csv', parse_dates=['signup_date', 'last_active_date'])

# Create cohort month
df['cohort_month'] = df['signup_date'].dt.to_period('M')
df['activity_month'] = df['last_active_date'].dt.to_period('M')

# Retention matrix
cohorts = df.groupby(['cohort_month', 'activity_month']).agg(n_users=('customer_id', 'nunique')).reset_index()
retention_matrix = cohorts.pivot(index='cohort_month', columns='activity_month', values='n_users')

# Plot heatmap
plt.figure(figsize=(10, 6))
plt.title("Cohort Retention")
sns.heatmap(retention_matrix, annot=True, fmt='.0f', cmap='YlGnBu')
plt.show()