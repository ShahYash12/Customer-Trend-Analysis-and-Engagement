# customer_segmentation.py

import pandas as pd

def segment_customers(df):
    conditions = [
        (df['purchase_count'] == 0),
        (df['purchase_count'] > 0) & (df['purchase_count'] <= 3),
        (df['purchase_count'] > 3)
    ]
    segments = ['Inactive', 'New', 'Loyal']
    df['segment'] = pd.cut(df['purchase_count'], bins=[-1, 0, 3, float('inf')], labels=segments)
    return df