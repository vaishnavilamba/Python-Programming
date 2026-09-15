from concurrent.futures import ProcessPoolExecutor
import time

def squres(number):
    time.sleep(1)
    return f"sqaure : {number*number}"

numbers = [1,2,3,4,5,6]

if __name__=='__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(squres,numbers)

    for result in results:
        print(result)        