import math

# Function to calculate distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Function to find the closest pair of points using a divide and conquer approach
def closest_pair(points):
    points.sort()  # Sort the points based on the x-coordinate
    return closest_pair_recursive(points)

# Recursive function to find the closest pair
def closest_pair_recursive(points):
    if len(points) <= 3:
        return brute_force_closest_pair(points)

    mid = len(points) // 2
    left_points = points[:mid]
    right_points = points[mid:]

    # Recursively find the closest pair in left and right halves
    left_closest = closest_pair_recursive(left_points)
    right_closest = closest_pair_recursive(right_points)

    # The closest pair will be either in the left, right, or across the midpoint
    min_dist = min(left_closest[0], right_closest[0])
    closest = left_closest if left_closest[0] < right_closest[0] else right_closest

    # Combine the results
    return closest

# Brute force approach to find closest pair for small number of points
def brute_force_closest_pair(points):
    min_dist = float('inf')
    closest_pair = None
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])
    return (min_dist, closest_pair)

# Function to read points from file
def read_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by space (instead of comma) and strip extra spaces
            x, y = map(int, line.strip().split())  # Default is to split by any whitespace
            points.append((x, y))  # Append the point (x, y) as a tuple
    return points


# Example usage
points = read_points('input_points.txt')
result = closest_pair(points)

# Result will contain the minimum distance and the closest pair
print("Closest pair:", result[1], "with distance:", result[0])
