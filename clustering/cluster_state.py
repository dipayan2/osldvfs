import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # <--- This is important for 3d plotting 
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
from scipy.stats import spearmanr

# Point to where benchmark data is
DATA_PATH = "./PowerDVFS.csv"

# These control which analysis is run, typically
# just set one to True
PRINT_3D_PCA = False
PRINT_2D_PCA = False
PRINT_3D_CPU_GPU = False
ONE_DIM_CLUSTERING_ELBOW = False
ONE_DIM_CLUSTERING = False
FIND_CORRELATION = True


# If ANALYZE_SINGLE_APP is true, only look at a single
# application. I was a bit lazy so only did this 
# for some of the tests. If this is set
# ANALYZE_SINGLE_APP_NAME is set to the app we will
# look at
ANALYZE_SINGLE_APP = False
ANALYZE_SINGLE_APP_NAME = 0

# Sets the number. Found this using the ONE_DIM_CLUSTERING_ELBOW
# and manually analyzing the graph
NUM_CLUSTERS = 5

# Used to generate uniform colors
def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)


def main():
    # Reading the CSV into a dataframe
    df = pd.read_csv(DATA_PATH)

    # Normalizing all the timing data and frequencies
    df["Mem"] = df["Mem"].transform(lambda x: x / x.max())
    #print(df["MemPower"])
    df["CPU"] = df["CPU"].transform(lambda x: x / x.max())
    df["GPU"] = df["GPU"].transform(lambda x: x / x.max())
    #df["User (s)"] = df.groupby("Application")["User (s)"].transform(lambda x: x / x.max())
    #df["Sys (s)"] = df.groupby("Application")["Sys (s)"].transform(lambda x: x / x.max())
    # df["GPUFreq"] = df["GPUFreq"].transform(lambda x: x / x.max())
    # df["CPUBig"] = df["CPUBig"].transform(lambda x: x / x.max())
    # df["CPUSmall"] = df["CPUSmall"].transform(lambda x: x / x.max())
    # df["MemFreq"] = df["MemFreq"].transform(lambda x: x / x.max())

    # Removing the small CPU frequency for now
    #RestPower,MemPower,MemPower,MemPower,Power-UX,Total,GPU,CPU,Mem,UX,MemFreq,CPUBig,CPUSmall,GPUFreq
   # df = df.drop(columns = ["CPUSmall","RestPower","Power-UX","Total","GPU","CPU","Mem","UX"])

    # If configures, only look at a single application's data
    if ANALYZE_SINGLE_APP:
       # df = df[df["Application"] == ANALYZE_SINGLE_APP_NAME]
        print("Only looking at {}".format(ANALYZE_SINGLE_APP_NAME))

 
    # Going to calculate Spearman Correlation between all of the variables
    if FIND_CORRELATION:
        gpu_spearman_r, _ = spearmanr(df["GPUPower"], df["MemPower"])
        cpu_spearman_r, _ = spearmanr(df["CPUPower"], df["MemPower"])
        mem_spearman_r, _ = spearmanr(df["MemPower"], df["MemPower"])
        print("MemPower- GPUPower Spearman R: {}".format(gpu_spearman_r))
        print("MemPower- CPUPower Spearman R: {}".format(cpu_spearman_r))
        print("MemPower- MemPower Spearman R: {}".format(mem_spearman_r))

        gpu_spearman_r, _ = spearmanr(df["GPUPower"], df["CPUPower"])
        cpu_spearman_r, _ = spearmanr(df["CPUPower"], df["CPUPower"])
        mem_spearman_r, _ = spearmanr(df["MemPower"], df["CPUPower"])
        print("CPUPower- GPUPower Spearman R: {}".format(gpu_spearman_r))
        print("CPUPower- CPUPower Spearman R: {}".format(cpu_spearman_r))
        print("CPUPower- MemPower Spearman R: {}".format(mem_spearman_r))

        gpu_spearman_r, _ = spearmanr(df["GPUPower"], df["GPUPower"])
        cpu_spearman_r, _ = spearmanr(df["CPUPower"], df["GPUPower"])
        mem_spearman_r, _ = spearmanr(df["MemPower"], df["GPUPower"])
        print("GPUPower - GPUPower Spearman R: {}".format(gpu_spearman_r))
        print("GPUPower - CPUPower Spearman R: {}".format(cpu_spearman_r))
        print("GPUPower - MemPower Spearman R: {}".format(mem_spearman_r))
 
    # Use this to figure out the best number of clusters for the 1D  
    elif ONE_DIM_CLUSTERING_ELBOW:
        # Tring to find the best number of clusters for just the latency
        K = range(1, 20)
        distortions = []

        for k in K:
            kmeanModel = KMeans(n_clusters = k).fit(df[["Mem"]])
            distortions.append(sum(np.min(cdist(df[["Mem"]], kmeanModel.cluster_centers_, "euclidean"), axis=1)) / df[["Mem"]].shape[0])

        plt.plot(K, distortions, "bx-")
        plt.xlabel("k")
        plt.ylabel("Distortion")
        plt.title("The Elbow Method showing the optimal k")
        plt.show()

    elif ONE_DIM_CLUSTERING:

        kmeanModel = KMeans(n_clusters = NUM_CLUSTERS).fit(df[["Mem"]])
       
        clusters = [ [] for i in range(NUM_CLUSTERS)  ]
        distances = cdist(df[["Mem"]], kmeanModel.cluster_centers_, "euclidean")
        for idx, latency in enumerate(df["Mem"]):
            clusters[np.argmin(distances[idx])].append(latency)
             
        cmap = get_cmap(NUM_CLUSTERS)
        for idx, cluster in enumerate(clusters):
            plt.plot(cluster, len(cluster) * [1], 'x', c = cmap(idx)) 

        if ANALYZE_SINGLE_APP:
            plt.title(ANALYZE_SINGLE_APP_NAME)
        else:
            plt.title("All Applications")

        # So now once we get the clusters, we want to be able to backtrack which 
        cluster_frequencies = [ [] for i in range(NUM_CLUSTERS)  ]
        for idx, cluster in enumerate(clusters):
            for point in cluster:
                gpu_freq = df[df["Mem"] == point]["GPUFreq"].values[0]
                cpu_freq = df[df["Mem"] == point]["CPUBig"].values[0]
                mem_freq = df[df["Mem"] == point]["MemFreq"].values[0]
        
                # Can be kind of useful to see the actual values
                if idx == np.argmin(kmeanModel.cluster_centers_):
                    print(df[df["Mem"] == point])

                if not ([gpu_freq, cpu_freq, mem_freq] in cluster_frequencies[idx]):
                    cluster_frequencies[idx].append([gpu_freq, cpu_freq, mem_freq])

        for idx, (cluster_freq, cluster) in enumerate(zip(cluster_frequencies, clusters)):
            print("Cluster center: {}".format(kmeanModel.cluster_centers_[idx]))
            print("Number of equivalent frequencies: {}".format(len(cluster_freq)))
            print("Number of points in cluster: {}".format(len(cluster)))

        for cluster in range(NUM_CLUSTERS):
            print("\nFrequencies around center {}:".format(kmeanModel.cluster_centers_[cluster]))
            for i in cluster_frequencies[cluster]:
                print(i)

 
    elif PRINT_3D_PCA:
    
        # Have to drop applicatoin column as well when doing PCA
      #  df = df.drop(columns = ["Application"])
        
        # Doing some PCA stuff
        df = StandardScaler().fit_transform(df)
        pca = PCA(n_components = 3)
        x_pca = pca.fit_transform(df)
        pca_df = pd.DataFrame(data = x_pca, columns = ["PC1", "PC2", "PC3"])
        
        # Setting up the 3D stoof
        fig = plt.figure()
        ax = fig.add_subplot(projection = '3d')

        # Drawing the 
        ax.scatter(pca_df["PC1"], pca_df["PC2"], pca_df["PC3"])
        ax.set_xlabel("PC1")
        ax.set_ylabel("PC2")
        ax.set_zlabel("PC3")

    elif PRINT_2D_PCA:

        # Have to drop applicatoin column as well when doing PCA
       # df = df.drop(columns = ["Application"])
        
        # Doing some PCA stuff
        df = StandardScaler().fit_transform(df)
        pca = PCA(n_components = 2)
        x_pca = pca.fit_transform(df)
        pca_df = pd.DataFrame(data = x_pca, columns = ["PC1", "PC2"])
        
        # Setting up the 3D stoof
        fig = plt.figure()
        ax = fig.add_subplot()

        # Drawing the 
        ax.scatter(pca_df["PC1"], pca_df["PC2"])
        ax.set_xlabel("PC1")
        ax.set_ylabel("PC2")
        
        if ANALYZE_SINGLE_APP:
            ax.set_title(ANALYZE_SINGLE_APP_NAME)
        else:
            ax.set_title("All applications")

    elif PRINT_3D_CPU_GPU:

                
        # Setting up the 3D stoof
        fig = plt.figure()
        ax = fig.add_subplot(projection = '3d')

        # Drawing a 3D scatter plot of CPU, CPU, and System
        ax.scatter(df["GPUFreq"], df["CPUBig"], df["MemPower"])
        ax.set_xlabel("GPUFrequency")
        ax.set_ylabel("CPUBiguency")
        ax.set_zlabel("MemPower")
        
        if ANALYZE_SINGLE_APP:
            ax.set_title(ANALYZE_SINGLE_APP_NAME)
        else:
            ax.set_title("All applications")

        print("Just looking at the DF to see if it is right")
        print(df)
  

    # Creating the figure
    plt.show()
    



if __name__ == "__main__":
    main()
