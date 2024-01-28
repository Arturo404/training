import os

dir_path_w = r"C:\Users\Arthur\Desktop\INFORMATIQUE\PYTHON"
dir_path = os.path.abspath(dir_path_w)

def dir_listing(dir_path):
    for name in os.listdir(dir_path):
        curr_path = os.path.join(dir_path, name)
        if(os.path.isdir(curr_path)):
            dir_listing(curr_path)
        else:
            with open(curr_path, 'r') as curr_file:
                print(curr_file.read())

if __name__ == "__main__":
    dir_listing(dir_path)
