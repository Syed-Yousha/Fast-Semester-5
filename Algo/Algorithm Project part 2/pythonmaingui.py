from tkinter import Tk, filedialog, Button, Label
from divideandConquer import closest_pair, multiply

def select_file_for_closest_pair():
    file_path = filedialog.askopenfilename(title="Select Input File for Closest Pair")
    if file_path:
        run_closest_pair(file_path)

def select_file_for_integer_multiplication():
    file_path = filedialog.askopenfilename(title="Select Input File for Integer Multiplication")
    if file_path:
        run_integer_multiplication(file_path)

def run_closest_pair(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    points = [tuple(map(int, line.split())) for line in lines]
    p1, p2, dist = closest_pair(points)
    result_label.config(text=f"Closest Pair: {p1}, {p2} with Distance: {dist}")

def run_integer_multiplication(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    integers = list(map(int, lines))
    if len(integers) < 2:
        result_label.config(text="Error: Input must contain at least two integers.")
        return

    product = multiply(integers[0], integers[1])
    result_label.config(text=f"Product: {product}")

# Create the GUI
root = Tk()
root.title("Divide and Conquer Algorithms")

# Closest Pair of Points Section
closest_pair_button = Button(root, text="Run Closest Pair of Points", command=select_file_for_closest_pair)
closest_pair_button.pack()

# Integer Multiplication Section
integer_multiplication_button = Button(root, text="Run Integer Multiplication", command=select_file_for_integer_multiplication)
integer_multiplication_button.pack()

# Result Label
result_label = Label(root, text="")
result_label.pack()

# Run the GUI
root.mainloop()
