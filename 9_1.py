__author__ = 'Moveton'
import time

"""
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a ** 2 + b ** 2 = c ** 2
    For example, 3 ** 2 + 4 ** 2 = 9 + 16 = 25 = 5 ** 2.
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
"""


start_time = time.time()

for i in range(1, 1000):
    for j in range(i, 1000 - i):
        k = 1000 - i - j
        if i * i + j * j == k * k:
            print(i, j, k)
            print('Product : {0}'.format(i * j * k))

print('It took ' + str(time.time() - start_time) + " seconds")