__author__ = 'Moveton'
import time

"""
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?

    NOTE: This is a way to slow code, which works with relatively small numbers. Don't use it for billion
"""


start_time = time.time()

def euler3(number):

    list_first = []

    # find all the dividers of the specific number
    for i in range(2, int(number / 2)):
        if number % i == 0:
            list_first.append(i)
    print(list_first)

    list_copy = list_first[:]
    list_last = []

    # find all the NON-PRIME dividers
    for i in list_first:
        for j in list_copy:
            if j > i and j % i == 0 and j not in list_last:
                list_last.append(j)
    print(list_last)

    # eq: prime dividers = all dividers - non-prime dividers
    print(max(set(list_copy).difference(set(list_last))))

print(euler3(13195))
print('It took ' + str(time.time() - start_time ) + " seconds")

