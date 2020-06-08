#cannot differentiate
import numpy as np
import random
import utils
import warnings
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans




file_name = utils.file_name
seed = 10
random.seed(seed)


points,labels = utils.readDataset(file_name)
points = np.array(points)

real_k = max(labels)+1

def chooseInit(n=5):
    max_value = -3
    max_startups = -3
    for j in range(n):
        startups = np.random.choice(points.shape[0], real_k, replace=False)
        kmeans = KMeans(n_clusters=real_k, init=points[startups], max_iter=500, random_state=seed,n_init=1)
        kmeans.fit(points)
        preds = kmeans.labels_
        score = silhouette_score(points, preds, metric='euclidean')
        if score > max_value:
            max_value = score
            max_startups = startups
    return max_startups

from time import process_time

t0 = process_time()
for i in range(100):
    print(i)
    startups = chooseInit(n=10)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        kmeans = KMeans(n_clusters=real_k, init=points[startups], max_iter=500, random_state=seed)
        kmeans.fit(points)
        labels_predicted = kmeans.labels_
    utils.showResults(labels, list(labels_predicted))
t = process_time() - t0
#print("Time is:",t)