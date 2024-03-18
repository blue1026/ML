from sklearn.utils import shuffle
import pandas
from sklearn.cluster import KMeans

df = pandas.read_csv("C:\\Users\\bluew\\OneDrive\\桌面\\HW\\dye.csv")

# do clustering
clusters = {cls:df[df["class"]==cls] for cls in df["class"].unique()}
df.pop("class")

# each class use 50 data randomly
[clusters[cls].pop("class") for cls in clusters.keys()]
[shuffle(clusters[cls]) for cls in clusters.keys()]
[clusters[cls].reset_index(drop=True, inplace=True) for cls in clusters.keys()]
[clusters[cls].drop(clusters[cls].index[50:], inplace=True) for cls in clusters.keys()]

# set 2 clusters for each class
_cls_centers = [KMeans(2).fit(clusters[cls]).cluster_centers_ for cls in clusters.keys()]
cls_centers = []
[[cls_centers.append(center) for center in centers] for centers in _cls_centers]

# save the centers of all classes as an array
centers_df = pandas.DataFrame(cls_centers, columns=df.columns)
centers_df.to_csv("C:\\Users\\bluew\\OneDrive\\桌面\\HW\\centers.csv", index=False)
print(centers_df)