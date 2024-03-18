import math
from threading import Thread
import pandas
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

N_CLUSTERS = 3
RANDOM_STATE = 0

def get_kmeans_result(num_iter):
    model = KMeans(N_CLUSTERS, max_iter=num_iter, random_state=RANDOM_STATE).fit(df)
    history_through_iteration[num_iter] = {
        "centers": model.cluster_centers_, 
        "classes": model.predict(df)
    }

def get_average_distance(history):
    return sum([math.dist(history["centers"][history["classes"][i]], df.iloc[i]) for i in range(len(df))]) / len(df)

df = pandas.read_csv("C:\\Users\\bluew\\OneDrive\\桌面\\HW\\dye.csv")
df.drop("class", axis=1, inplace=True)

kmeans = KMeans(N_CLUSTERS, random_state=RANDOM_STATE)
num_iterations = kmeans.fit(df).n_iter_

#using this dumb method to get center vs iteration because sklearn doesn't provide history of fitting
history_through_iteration = {}
[Thread(target=get_kmeans_result, args=(n,)).start() for n in range(1, num_iterations+1)]
while (len(history_through_iteration)<num_iterations):
    pass

# save the clusters
pandas.DataFrame(kmeans.cluster_centers_, columns=df.columns).to_csv("C:\\Users\\bluew\\OneDrive\\桌面\\HW\\cluster3.csv", index=False)

# get average distances
avg_dist_vs_iters = [get_average_distance(history_through_iteration[i]) for i in range(1, num_iterations+1)]

# plot "Average Distance vs Iteration"
fig, axes = plt.subplots(1, 2)

axes[1].plot([i for i in range(1, len(avg_dist_vs_iters)+1)], avg_dist_vs_iters, "*-")
axes[1].set_xlabel("number of iteration")
axes[1].set_title("kmeans center")

# plot the three center (d1-c1)
axes[0].plot(kmeans.cluster_centers_[0][0], kmeans.cluster_centers_[0][1], "^")
axes[0].plot(kmeans.cluster_centers_[1][0], kmeans.cluster_centers_[1][1], "o")
axes[0].plot(kmeans.cluster_centers_[2][0], kmeans.cluster_centers_[2][1], "+")
axes[0].set_xlabel("d1")
axes[0].set_ylabel("c1")

plt.show()