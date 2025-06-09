import random

def generate_random_integers(size):
    return [random.randint(1, 10000) for _ in range(size)]

def generate_random_points(size):
    return [(random.randint(1, 1000), random.randint(1, 1000)) for _ in range(size)]

def generate_input_files():
    for i in range(1, 11):
     
        integers = generate_random_integers(100 + i * 10)
        with open(f"integer_input_{i}.txt", "w") as f:
            f.write("\n".join(map(str, integers)))

        points = generate_random_points(100 + i * 10)
        with open(f"points_input_{i}.txt", "w") as f:
            for point in points:
                f.write(f"{point[0]} {point[1]}\n")

if __name__ == "__main__":
    generate_input_files()
    print("Input files generated.")
