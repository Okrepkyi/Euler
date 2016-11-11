__author__ = 'Moveton'
import time


start_time = time.time()

def is_prime(n):
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    else:
        return False

print(is_prime(2639))
print('It took ' + str(time.time() - start_time ) + " seconds")