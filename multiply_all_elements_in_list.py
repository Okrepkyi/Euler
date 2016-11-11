__author__ = 'Moveton'
import time


start_time = time.time()

def mult(n):
    result = 1
    for j in n:
        result *= j
    return result

print(mult([3, 4, 5]))

print('It took ' + str(time.time() - start_time ) + " seconds")