import sys
from functools import reduce

from helpers.benchmark import benchmark


def naive_grid_traveler(m, n):
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0

    return naive_grid_traveler(m - 1, n) + naive_grid_traveler(m, n -1)


def memo_grid_traveler(m, n, memo={}):
    key = '%d-%d' % (m, n)

    if key in memo: return memo[key]
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0

    memo[key] = memo_grid_traveler(m - 1, n, memo) + memo_grid_traveler(m, n -1, memo)
    return memo[key]


if __name__ == '__main__':
    arg = (
        int(sys.argv[1]), 
        int(sys.argv[2])
    )

    def run_naive_grid_traveler():
        return naive_grid_traveler(arg[0], arg[1])
    def run_memo_grid_traveler():
        return memo_grid_traveler(arg[0], arg[1])

    benchmark(run_naive_grid_traveler)
    benchmark(run_memo_grid_traveler)