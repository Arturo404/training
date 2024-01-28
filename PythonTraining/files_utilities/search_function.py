import os

dir_path_w = r"C:\Users\Arthur\Desktop\INFORMATIQUE\PYTHON"
dir_path = os.path.abspath(dir_path_w)

def generator_names(dir_path, pattern):
    for name in os.listdir(dir_path):
        if pattern in name:
            yield name

        curr_path = os.path.join(dir_path, name)
        if(os.path.isdir(curr_path)):
            generator_names(curr_path, pattern)


def search_pattern(dir_path, pattern):
    for name in generator_names(dir_path, pattern):
        print(name)


if __name__ == "__main__":
    search_pattern(dir_path, "e")