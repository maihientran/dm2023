import random
import matplotlib.pyplot as plt

# Generate 300 random 2D points
D = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(300)]

def euclid_dist(point1,point2):
    return ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**0.5

# Define hierarchical clustering function
def hierarchCluster(points, distFunc):
    # Initialize each point as a separate cluster
    clusters = [[point] for point in points]

    # Perform clustering until all points are in a single cluster
    while len(clusters) > 1:
        # Initialize variables to keep track of closest clusters and their distance
        min_dist = float('inf')
        closest_clusters = None

        # Iterate over all pairs of clusters and find the closest pair
        for i in range(len(clusters)):
            for j in range(i+1, len(clusters)):
                # Calculate distance between the two clusters using the provided distance function
                dist = distFunc(clusters[i], clusters[j])

                # Update minimum distance and closest clusters if this distance is smaller
                if dist < min_dist:
                    min_dist = dist
                    closest_clusters = (i, j)

        # Merge the two closest clusters into a single cluster
        i, j = closest_clusters
        clusters[i] += clusters[j]
        del clusters[j]

    return clusters

# Define minimum cluster distance function
def minClusterDist(cluster1, cluster2):
    min_dist = float('inf') # Initialize minimum distance to infinity

    # Calculate distance between each point in cluster1 and each point in cluster2
    for point1 in cluster1:
        for point2 in cluster2:
            dist = euclid_dist(point1,point2)
            if dist < min_dist:
                min_dist = dist

    return min_dist
...

# Cluster the population using hierarchical clustering and minimum cluster distance function
clusters = hierarchCluster(D, minClusterDist)

# Print each cluster
for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1}: {cluster}")

for i, cluster in enumerate(clusters):
    # Extract x and y coordinates of points in the cluster
    xs = [point[0] for point in cluster]
    ys = [point[1] for point in cluster]

    # Plot the points with a different color for each cluster
    plt.scatter(xs, ys, c=f'C{i}')

# Set the plot title and axis labels
plt.title('Hierarchical Clustering of Random Points')
plt.xlabel('Width')
plt.ylabel('Height')

# Show the plot
plt.show()