import numpy as np 
import pandas as pd 

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df=pd.read_csv('crime_dataset.csv')
print(df.columns)

features=df.drop(["id"],axis=1)


kmeans = KMeans(
    init="k-means++",
    n_clusters=2,
    n_init=20,
    max_iter=300,
    random_state=1
)
kmeans.fit(features)
print('inertia ',kmeans.inertia_)

print('iteration  ',kmeans.n_iter_)
print('centers  ',kmeans.cluster_centers_)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x=df['personal_traits']
y=df['social_characteristics']
z=df['motivating_factors']

ax.scatter(x, y, z, c='r', marker='o')
cx=[kmeans.cluster_centers_[0][1],kmeans.cluster_centers_[1][1]]
cy=[kmeans.cluster_centers_[0][2],kmeans.cluster_centers_[1][2]]
cz=[kmeans.cluster_centers_[0][3],kmeans.cluster_centers_[1][3]]
ax.scatter(cx,cy,cz, c='b',marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()