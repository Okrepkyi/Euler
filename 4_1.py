__author__ = 'Moveton'
import time

"""
    A palindromic number reads the same both ways. The largest palindrome
    made from the product of two 2-digit numbers is 9009 = 91 ? 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
"""

start_time = time.time()
l = []

for i in range(100, 1000):
    for j in range(100, i):
        mult = i * j
        if mult == int(''.join(list(str(mult))[::-1])):
            l.append(mult)

print(max(l))
print('It took ' + str(time.time() - start_time ) + " seconds")
