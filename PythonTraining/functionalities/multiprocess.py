import multiprocessing
import os

dir_path_w = r"C:\Users\Arthur\Desktop\INFORMATIQUE\PYTHON\integers"
dir_path = os.path.abspath(dir_path_w)

sum_file_path_w = r"C:\Users\Arthur\Desktop\INFORMATIQUE\PYTHON\sums.txt"
sum_file_path = os.path.abspath(sum_file_path_w)


sum_list = []
sum_lock = multiprocessing.Lock()

def sumIntInFile(file_path):
    global sum_list
    sum = 0

    print("current file: ", file_path)
    with open(file_path) as integer_file:
        for line in integer_file:
            sum += int(line)

    dir_sum = {"file_name":file_path, "sum":sum}
    print(dir_sum)


    sum_lock.acquire()

    with open(sum_file_path, "a") as sum_file:
        sum_file.write(str(dir_sum) + "\n")

    sum_lock.release()


if __name__ == "__main__":

    clr = open(sum_file_path, "w")
    clr.close()
    
    procs = []

    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        p = multiprocessing.Process(target=sumIntInFile, args=(file_path,))
        procs.append(p)
        p.start()

    while(True):
        for proc in procs:
            if(proc.is_alive()):
                continue
        
        break


        