import threading
import logging


logging_lock = threading.Lock()
logfile_path = "C:/Users/Arthur/Desktop/INFORMATIQUE/PYTHON/multithreading.log"

logging.basicConfig(filename=logfile_path,
                        filemode='a',
                        format='%(asctime)s:%(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

def write_log():
    logging_lock.acquire()

    logging.info(f"{threading.current_thread().name}")
    
    logging_lock.release()



if __name__ == "__main__":

    clr = open(logfile_path, "w")
    clr.close()

    for i in range(4):
        t = threading.Thread(target=write_log, name=f"t{i}")
        t.start()