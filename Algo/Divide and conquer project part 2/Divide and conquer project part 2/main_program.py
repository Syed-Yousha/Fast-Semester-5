import sys
from closest_pair import closest_pair
from integer_multiplication import karatsuba
from generate_input_data import generate_random_integers, generate_random_points
from file_selection_gui import select_file

def read_input(file_path):
    with open(file_path, "r") as f:
        data = f.readlines()
    return data

def process_input(file_path):
    # Decide based on file type (integers or points)
    if file_path.endswith(".txt"):
        data = read_input(file_path)
        print(f"Processing data from {file_path}...")
        if "point" in file_path:
            points = [tuple(map(int, line.split())) for line in data]
            print(f"Closest Pair: {closest_pair(points)}")
        else:
            integers = [int(x.strip()) for x in data]
            result = karatsuba(integers[0], integers[1])
            print(f"Multiplication result: {result}")

if __name__ == "__main__":
    # Select input file via GUI
    file_path = select_file()
    process_input(file_path)
