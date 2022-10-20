import pandas as pd
import numpy as np
from sklearn import metrics
from scipy.stats import spearmanr
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

DATA_PATH = "./powerDVFS.csv"

NUM_CLUSTER = 4
col_max = {} #stores the max value of the column
NU = 2 # importance of power

def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)

def get_data():
    df = pd.read_csv(DATA_PATH)
    # normalized the data to range 0-1
    for feat_name in df.columns:
        col_max[feat_name] = df[feat_name].max()
        df[feat_name] = df[feat_name].transform(lambda x: x/x.max())
    
    return df

def pca_analysis(df):
    # enter the selected list of columns to perform PCA analysis
    df_select = df[['Mem','CPU','GPU']]


def clustering_data(df):
    # we need to find a way to get clustering based on 
    df['EDPCPU'] = df['CPUPower']*pow(df["CPU"],NU)
    df['EDPMem'] = df['MemPower']*pow(df["Mem"],NU)
    df['EDPGPU'] = df['GPUPower']*pow(df["GPU"],NU)

    kmeanModel = KMeans(n_clusters=NUM_CLUSTER).fit(df[['EDPCPU','EDPMem','EDPGPU']])
    df['cluster'] = kmeanModel.labels_.tolist()
    return df

def print_cluster(df):
    cluster = [ [] for i in range(NUM_CLUSTER)]
    for idx, row in df.iterrows():
        cluster[int(row['cluster'])].append((row['CPUBig']*col_max['CPUBig'], row['CPUSmall']*col_max['CPUSmall'], row['MemFreq']*col_max['MemFreq'], row['GPUFreq']*col_max['GPUFreq']))
    
    for cl_idx in range(NUM_CLUSTER):
        for val in cluster[cl_idx]:
            print(cl_idx, val[0], val[1], val[2], val[3])
    


if __name__ == "__main__":
    df = get_data()
    df = clustering_data(df)
    print_cluster(df)

    # run something in here