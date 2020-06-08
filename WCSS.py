from sklearn.cluster import KMeans
import sklearn.cluster
import utils


import random

file_name = utils.file_name
seed = 100
random.seed(seed)

points,labels = utils.readDataset(file_name)

real_k = max(labels)+1

from time import process_time

t0 = process_time()
for i in range(100):
    print(i)
    kmeans = KMeans(n_clusters=real_k, max_iter = 500)
    kmeans.fit(points)
    labels_predicted = kmeans.labels_


    utils.showResults(labels, list(labels_predicted))
t = process_time() - t0
#print("Time is:",t)






