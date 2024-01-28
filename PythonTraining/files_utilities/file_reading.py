import os

file_to_read_path_w = r"C:\Users\Arthur\Desktop\INFORMATIQUE\PYTHON\integers\integer3.txt"
file_to_read_path = os.path.abspath(file_to_read_path_w)


def file_reading(file_path):
    with open(file_path, 'r') as file_obj:
        generator = (line for line in file_obj)
        for line in generator:
            print(line)
    
if __name__ == "__main__":

    file_reading(file_to_read_path)