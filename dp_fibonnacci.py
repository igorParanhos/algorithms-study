import sys
from functools import reduce

from helpers.benchmark import benchmark


def expensive_fib(n):
    if n <= 2: f = 1
    else: f = expensive_fib(n - 1) + expensive_fib(n - 2)
    return f


def recursive_memo_fib(n):
    fib_memo = {}

    def inner(k):
        if fib_memo.get(k): return fib_memo[k]

        if k <= 2: f = 1
        else: f = inner(k - 1) + inner(k - 2)
        fib_memo[k] = f
        return f

    return inner(n)


def linear_memo_fib(n):
    fib_memo = {}

    def inner():
        for k in range(1, n + 1):
            if k <= 2: f = 1
            else: f = fib_memo[k - 1] + fib_memo[k - 2]
            fib_memo[k] = f

        return fib_memo[n]
        
    return inner()


def normal_fib(n):
    total = 0
    last = 1
    for k in range(n):
        last, total = total, total + last

    return total


def reducer_fib(n):
    # return reduce(lambda p, b: [*p, p[b-1] + p[b-2]] if b > 1 else [*p, 1], range(n), [])
    return reduce(lambda p, b: [p[1] + p[0], p[0]] , range(n), [1, 0]).pop()
    

if __name__ == '__main__':
    arg = int(sys.argv[1])

    def run_expensive_fib():
        return expensive_fib(arg)
    def run_recursive_memo_fib():
        return recursive_memo_fib(arg)
    def run_linear_memo_fib():
        return linear_memo_fib(arg)
    def run_normal_fib():
        return normal_fib(arg)
    def run_reducer_fib():
        return reducer_fib(arg)

    benchmark(run_expensive_fib)
    benchmark(run_recursive_memo_fib)
    benchmark(run_linear_memo_fib)
    benchmark(run_normal_fib)
    benchmark(run_reducer_fib)
