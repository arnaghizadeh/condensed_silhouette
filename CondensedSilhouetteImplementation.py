import numpy as np


import scipy.spatial.distance as distance
from sklearn.metrics.pairwise import pairwise_distances_chunked
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.externals.joblib import Parallel, delayed


def silhouette_score(X, labels, c, inertia, metric='euclidean', sample_size=None, random_state=None):
    if sample_size is not None:
        random_state = check_random_state(random_state)
        indices = random_state.permutation(X.shape[0])[:sample_size]
        if metric == "precomputed":
            raise ValueError('Distance matrix cannot be precomputed')
        else:
            X, labels = X[indices], labels[indices]
    return np.mean(silhouette_samples(X, labels, c, inertia, metric=metric))

def silhouette_samples(X, labels, c, inertia, metric='euclidean'):
    import time
    A = inertia / len(labels)
    B = _nearest_cluster_distance(X, labels, c, metric)
    print("Testing",A,B)
    sil_samples = (B - A) / np.maximum(A, B)
    return np.nan_to_num(sil_samples)

def _intra_cluster_distances_block_(suba, subb,  metric):
    dist = pairwise_distances(suba, subb, metric=metric)
    return dist.mean()
def _nearest_cluster_distance_block_(X, metric):
    dist = pairwise_distances(X, metric=metric)
    dist[dist == 0] = np.max(dist)+1#remove zeros
    dist = dist.min(axis=1)
    return dist.mean()

def _intra_cluster_distances(X, labels, c, metric, n_jobs=1):
    values = np.array(Parallel(n_jobs=n_jobs)(
            delayed(_intra_cluster_distances_block_)(
                X[np.where(labels == label)[0]],
                [c[label]],
                metric)
                for label in np.unique(labels)))
    return values.mean()

def _nearest_cluster_distance(X, labels, c, metric, n_jobs=1):
    values = _nearest_cluster_distance_block_(c,  metric)
    return values
