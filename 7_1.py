__author__ = 'Moveton'
import time

"""
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
"""


start_time = time.time()

def is_prime(n):
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return n
    else:
        return False

print([i for i in map(is_prime, range(111111)) if i is not False][10000])

print('It took ' + str(time.time() - start_time ) + " seconds")
