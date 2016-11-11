__author__ = 'Moveton'
import time

"""
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


start_time = time.time()

# 2660 = 380 * 7 (bigger than 2520);
# 380000000 - just big enough number;
# 380 = 19 (biggest prime number) * 20.
for i in range(2660, 380000000, 380):
    if i % 2 == 0 and i % 3 == 0 and i % 3 == 0 and i % 5 == 0 and i % 6 == 0 and i % 7 == 0 \
    and i % 8 == 0 and i % 9 == 0 and i % 10 == 0 and i % 11 == 0 and i % 12 == 0 and i % 12 == 0 \
    and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 \
    and i % 19 == 0 and i % 20 == 0:
        print(i)

print('It took ' + str(time.time() - start_time ) + " seconds")