import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import StandardScaler
import umap

class DimensionalityReduction():

    def __init__(self):
        pass

    def tsne(self, X, y, n_components:int = 3):
         
        X_scaled = StandardScaler().fit(X).transform(X)

        if (n_components == 3):

            print("t-SNE 3d dimensionality reduction running...")
            df_tsne = pd.DataFrame(TSNE(n_components=n_components).fit_transform(X_scaled), columns=["component_1", "component_2", "component_3"])
            df_tsne["label"] = y
            self.plot_3d(df_tsne, title="t-SNE")

        elif (n_components == 2):

            print("t-SNE 2d dimensionality reduction running...")
            df_tsne = pd.DataFrame(TSNE(n_components=n_components).fit_transform(X_scaled), columns=["component_1", "component_2"])
            df_tsne["label"] = y
            self.plot_2d(df_tsne, title="t-SNE")

        elif (n_components == 1):

            print("t-SNE 1d dimensionality reduction running...")
            df_tsne = pd.DataFrame(TSNE(n_components=n_components).fit_transform(X_scaled), columns=["component_1"])
            df_tsne["label"] = y

        else:
            return -1

        g = sns.pairplot(df_tsne, hue='label', height=2.5)
        plt.show(block=False)

        return df_tsne

    def UMAP(self, X, y, n_components:int = 3):

        X_scaled = StandardScaler().fit(X).transform(X)

        if (n_components == 3):

            print("UMAP 3d dimensionality reduction running...")
            df_umap = pd.DataFrame(umap.UMAP(random_state=42, n_components=n_components).fit_transform(X_scaled), columns=["component_1", "component_2", "component_3"])
            df_umap["label"] = y
            self.plot_3d(df_umap, title="UMAP")

        elif (n_components == 2):

            print("UMAP 2d dimensionality reduction running...")
            df_umap = pd.DataFrame(umap.UMAP(random_state=42, n_components=n_components).fit_transform(X_scaled), columns=["component_1", "component_2"])
            df_umap["label"] = y
            self.plot_2d(df_umap, title="UMAP")

        elif (n_components == 1):

            print("UMAP 1d dimensionality reduction running...")
            df_umap = pd.DataFrame(umap.UMAP(random_state=42, n_components=n_components).fit_transform(X_scaled), columns=["component_1"])
            df_umap["label"] = y
        
        else:
            return -1

        g = sns.pairplot(df_umap, hue='label', height=2.5)
        plt.show(block=False)

        return df_umap

    def lda(self, X, y):

        X_scaled = StandardScaler().fit(X).transform(X)
        n_classes = len(y.unique())

        if (n_classes == 2):

            print("LDA 1d dimensionality reduction running...")
            df_lda = pd.DataFrame(LinearDiscriminantAnalysis(n_components=1).fit_transform(X_scaled, y), columns=["component_1"])
            df_lda["label"] = y

        elif (n_classes == 3):

            print("LDA 2d dimensionality reduction running...")
            df_lda = pd.DataFrame(LinearDiscriminantAnalysis(n_components=2).fit_transform(X_scaled, y), columns=["component_1", "component_2"])
            df_lda["label"] = y
            self.plot_2d(df_lda, title="LDA")

        elif (n_classes == 4):

            print("LDA 3d dimensionality reduction running...")
            df_lda = pd.DataFrame(LinearDiscriminantAnalysis(n_components=3).fit_transform(X_scaled, y), columns=["component_1", "component_2", "component_3"])
            df_lda["label"] = y
            self.plot_3d(df_lda, title="LDA")
        
        else:
            return -1

        g = sns.pairplot(df_lda, hue='label', height=2.5)
        plt.show(block=False)

        return df_lda

    def pca(self, X, y, n_components:int = 3):

        X_scaled = StandardScaler().fit(X).transform(X)

        if (n_components == 3):

            print("PCA 3d dimensionality reduction running...")
            df_pca = pd.DataFrame(PCA(n_components=n_components).fit_transform(X_scaled), columns=["component_1", "component_2", "component_3"])
            df_pca["label"] = y
            self.plot_3d(df_pca, title="PCA")

        elif(n_components == 2):

            print("PCA 2d dimensionality reduction running...")
            df_pca = pd.DataFrame(PCA(n_components=n_components).fit_transform(X_scaled), columns=["component_1", "component_2"])
            df_pca["label"] = y
            self.plot_2d(df_pca, title="PCA")

        elif(n_components == 1):

            print("PCA 1d dimensionality reduction computing...")
            df_pca = pd.DataFrame(PCA(n_components=n_components).fit_transform(X_scaled), columns=["component_1"])
            df_pca["label"] = y

        else:
            return -1

        g = sns.pairplot(df_pca, hue='label', height=2.5)
        plt.show(block = False)

        return df_pca