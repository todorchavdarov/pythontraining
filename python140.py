import math
from functools import wraps
import functools
import time


def return_average(*numbers):
    sums = 0

    for number in numbers:
        sums = sums + number

    avg = sums / len(numbers)
    return avg


# avg = return_average(1, 2, 3, 4, 5, 6)
# print(avg)

def timer(func):
    """Execution time of a function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        total_time = 0
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        total_time += run_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} seconds")
        return "Total time " + str(total_time)

    return wrapper_timer


def memoize(func):
    memo = {}

    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = func(*args)
            memo[args] = rv
            return rv

    return wrapper


# @timer
@memoize
def lucas(number):
    if number == 0:
        return 2;
    if number == 1:
        return 1
    return lucas(number - 1) + lucas(number - 2)


def prime_factorization(number):
    i = 2
    factors = []
    while i <= number:
        if (number % i) == 0:
            factors.append(i)
            number = number / i
        else:
            i = i + 1
    return factors


l60 = lucas(60)
l61 = lucas(61)

#print(prime_factorization(l60))
print(prime_factorization(l61))
