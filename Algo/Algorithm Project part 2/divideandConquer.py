import math

# Closest Pair of Points (Divide and Conquer)
def closest_pair(points):
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def closest_pair_rec(pts_sorted_x, pts_sorted_y):
        if len(pts_sorted_x) <= 3:
            return brute_force(pts_sorted_x)

        mid = len(pts_sorted_x) // 2
        left_x = pts_sorted_x[:mid]
        right_x = pts_sorted_x[mid:]
        midpoint = pts_sorted_x[mid][0]

        left_y = list(filter(lambda p: p[0] <= midpoint, pts_sorted_y))
        right_y = list(filter(lambda p: p[0] > midpoint, pts_sorted_y))

        (p1, q1, d1) = closest_pair_rec(left_x, left_y)
        (p2, q2, d2) = closest_pair_rec(right_x, right_y)

        (p3, q3, d3) = closest_split_pair(pts_sorted_x, pts_sorted_y, min(d1, d2))

        if d1 <= d2 and d1 <= d3:
            return p1, q1, d1
        elif d2 <= d1 and d2 <= d3:
            return p2, q2, d2
        else:
            return p3, q3, d3

    def brute_force(points):
        min_dist = float("inf")
        pair = (None, None)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = distance(points[i], points[j])
                if dist < min_dist:
                    min_dist = dist
                    pair = (points[i], points[j])
        return pair[0], pair[1], min_dist

    def closest_split_pair(px, py, delta):
        mid_x = px[len(px) // 2][0]
        strip = [p for p in py if mid_x - delta <= p[0] <= mid_x + delta]
        min_dist = delta
        closest_pair = (None, None)
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                p, q = strip[i], strip[j]
                dist = distance(p, q)
                if dist < min_dist:
                    min_dist = dist
                    closest_pair = (p, q)
        return closest_pair[0], closest_pair[1], min_dist

    sorted_x = sorted(points, key=lambda x: x[0])
    sorted_y = sorted(points, key=lambda x: x[1])
    return closest_pair_rec(sorted_x, sorted_y)


# Integer Multiplication (Divide and Conquer)
def multiply(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2

    x_high, x_low = divmod(x, 10**half)
    y_high, y_low = divmod(y, 10**half)

    z0 = multiply(x_low, y_low)
    z1 = multiply(x_low + x_high, y_low + y_high)
    z2 = multiply(x_high, y_high)

    return z2 * 10**(2 * half) + (z1 - z2 - z0) * 10**half + z0
