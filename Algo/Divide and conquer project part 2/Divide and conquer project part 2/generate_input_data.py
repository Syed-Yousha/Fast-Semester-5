import random

def generate_random_integers(size):
    return [random.randint(1, 10000) for _ in range(size)]

def generate_random_points(size):
    return [(random.randint(1, 100), random.randint(1, 100)) for _ in range(size)]

# Generate random integers for multiplication testing
input_integers = generate_random_integers(100)
with open("input_integers.txt", "w") as f:
    f.write("\n".join(map(str, input_integers)))

# Generate random points for closest pair testing
input_points = generate_random_points(100)
with open("input_points.txt", "w") as f:
    for point in input_points:
        f.write(f"{point[0]} {point[1]}\n")

print("Random input data generated and saved to files.")
