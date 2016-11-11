__author__ = 'Moveton'
import time

"""
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


start_time = time.time()
check_list = list(range(2, 21))

def euler5(step):
    for i in range(step, 380000000, step):
        if all(i % j == 0 for j in check_list):
            return i
    return None

print(euler5(380))
print('It took ' + str(time.time() - start_time ) + " seconds")