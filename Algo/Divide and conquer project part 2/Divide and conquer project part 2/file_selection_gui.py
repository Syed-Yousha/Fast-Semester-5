from tkinter import filedialog, Tk

def select_file():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select Input File")
    return file_path

# Example usage
if __name__ == "__main__":
    file_path = select_file()
    print(f"Selected file: {file_path}")
