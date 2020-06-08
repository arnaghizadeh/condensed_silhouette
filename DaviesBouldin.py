#cannot differentiate
import numpy as np
import random
import utils
import warnings
import sklearn.metrics as metrics
from sklearn.cluster import KMeans

file_name = utils.file_name
seed = 10
random.seed(seed)


points,labels = utils.readDataset(file_name)
points = np.array(points)

real_k = max(labels)+1

def chooseInit(n=5):
    min_value = 10000
    min_startups = 10000
    for j in range(n):
        startups = np.random.choice(points.shape[0], real_k, replace=False)
        kmeans = KMeans(n_clusters=real_k, init=points[startups], max_iter=500, random_state=seed, n_init=1)
        kmeans.fit(points)
        preds = kmeans.labels_
        with np.errstate(divide='ignore'):
            score = metrics.davies_bouldin_score(points,preds)
        if score < min_value:
            min_value = score
            min_startups = startups
    return min_startups

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

