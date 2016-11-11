__author__ = 'Moveton'
import time

"""
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
"""


start_time = time.time()

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n

print(sum(list(map(is_prime, (i for i in range(2000000))))))

print('It took ' + str(time.time() - start_time) + " seconds")