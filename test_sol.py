from sol2 import sol, MOD
import pytest
from itertools import combinations
from random import randint as ri

TOTAL = 1000
MAX = 30


def brute_sol(n, k, ais):
    ret = 0
    p = lambda x: reduce(lambda y, z: y * z, x, 1)
    for l in xrange(n + 1):
        for subset in combinations(ais, l):
            val = 0 if not subset else p(subset)
            if val % k == 0:
                ret = (ret + val) % MOD

    return ret


@pytest.mark.parametrize(
    "n,k", 
    [(n, ri(1, n)) for n in (ri(1, MAX) for _ in xrange(TOTAL))])
def test_sol(n, k, ais):
    n = 5
    k = 1
    ais = [2, 5, 2, 5, 5]
    assert sol(n, k, ais) == brute_sol(n, k, ais)
        
