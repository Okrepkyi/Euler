__author__ = 'Moveton'
import time

"""
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?

    NOTE: This is a way to slow code, which works with relatively small numbers. Don't use it for billion
"""

start_time = time.time()
list_first = []

# find all the dividers of the specific number
def euler3(number):
    for i in range(2, int(number / 2)):
        if number % i == 0:
            list_first.append(i)

# check, whether the number in a 'list_first' is a prime one
def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return number

print(euler3(13195))
print(max(list(map(is_prime, list_first))))
print('It took ' + str(time.time() - start_time ) + " seconds")


