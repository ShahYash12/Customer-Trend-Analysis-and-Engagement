# email_kpi_analysis.py

import pandas as pd

def calculate_kpis(df):
    df['open_rate'] = df['emails_opened'] / df['emails_sent']
    df['click_rate'] = df['emails_clicked'] / df['emails_sent']
    summary = df[['open_rate', 'click_rate']].mean().to_dict()
    return summary