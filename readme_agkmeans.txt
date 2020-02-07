Advanced Graph-based Kmeans (AGKmeans) clustering is a graph extension of Kmeans clustering.
The Kmeans algorithm proposed by Lloyd is a simple iterative algorithm that can partition a dataset into a predefined number of clusters k.
Since Kmeans utilizes metrics such as Euclidean for calculating distances, the distance among nodes needs to satisfy triangle inequality.
 In clustering human contact datasets that contain dynamic objects, consisting of contact frequencies and durations, the distances among nodes may
not conform with the triangle inequality.
 In such situations, classical Kmeans clustering cannot be applied.
AGKmeans can be applied to datasets which can be modeled as graphs.
 In AGKmeans, initial centroids are selected based on the number of unique contacts of nodes.
The AGKmeans algorithm uses the Dijkstra  shortest path algorithm and consists of two steps: assignment and update.
