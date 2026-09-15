import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"sqaure : {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube : {i*i*i}")


if __name__=="__main__":
    t = time.time()

    #creating 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    #Start the process
    p1.start()
    p2.start()

    #wait for complete the process
    p1.join()
    p2.join()

    finished_time = time.time()-t
    print(finished_time)              