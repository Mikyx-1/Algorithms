# Implementation of cloest pair with Divide and Conquer algorithm

import math

def distance(p1, p2):
    # Calculate the Euclidean distance between two points
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force(points, start, end):
    # Compute the closest pair of points using brute force
    min_distance = float('inf')
    closest_pair = None

    for i in range(start, end):
        for j in range(i + 1, end):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (points[i], points[j])

    return min_distance, closest_pair


def closest_pair(points, start, end):
    if end - start <=3 :
        return brute_force(points, start, end)
    
    mid = (start + end)//2

    left_dist, left_pair = brute_force(points, start, mid)
    right_dist, right_pair = brute_force(points, mid, end)

    if left_dist < right_dist:
        min_distance = left_dist
        closest = left_pair
    else:
        min_distance = right_dist
        closest = right_pair

    strip = []
    for i in range(start, end):
        if abs(points[i][0] - points[mid][0]) < min_distance:
            strip += [points[i]]
    
    strip.sort(key=lambda point: point[1])
    for i in range(len(strip)-1):
        for j in range(i+1, len(strip)):
            if distance(strip[i], strip[j]) < min_distance:
                min_distance = distance(strip[i], strip[j])

                closest = (strip[i], strip[j])

    return min_distance, closest


# Example usage
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
points.sort()  # Sort the points by x-coordinate

n = len(points)

min_distance, closest = closest_pair(points, 0, n)
print("Closest pair: ", closest)
print("Distance: ", min_distance)