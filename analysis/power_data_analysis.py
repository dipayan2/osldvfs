import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import shutil

DATA_PATH = "/Users/samhachem/Downloads/onStopTriggerExport_30491_-8585269145389504800.csv"

def get_data():
    df = pd.read_csv(DATA_PATH)
    # normalized the data to range 0-1
    # for feat_name in df.columns:
    #     col_max[feat_name] = df[feat_name].max()
    #     df[feat_name] = df[feat_name].transform(lambda x: x/x.max())
    return df

df = get_data()

print(df.iloc[:29999])



