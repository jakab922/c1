from fractions import gcd
from sys import setrecursionlimit as srl
from functools import wraps
srl(10 ** 6)

CACHE = {}
rhave, right, mod = None, None, 10 ** 9 + 7


def cache(fn):
    @wraps(fn)
    def cached(have, nxt):
        key = (have, nxt)
        global CACHE
        if key not in CACHE:
            CACHE[key] = fn(*key)
        return CACHE[key]
    return cached


@cache
def rsolve(have, nxt):
    print "have: %s" % (have,)
    print "nxt: %s" % (nxt,)
    need = k / have
    
    if nxt == n:
        return 1 if need == 1 else 0
    elif need == 1:
        return right[nxt] if nxt != n else 1
    if rhave[nxt] % need != 0:
        return 0

    curr = 0
    for i in xrange(nxt, n):
        if rhave[i] % need != 0:
            break
        c = gcd(ais[i], need)    
        curr = (curr + ais[i] * rsolve(have * c, i + 1)) % mod

    return curr

def solve(n, k, ais):
    ais = sorted(ais, key=lambda x: gcd(k, x), reverse=True)
    print "ais: %s" % (ais,)
    global rhave
    global right
    
    rhave = [1] * n
    rhave[-1] = gcd(ais[-1], k)
    right = [1] * n
    right[-1] = ais[-1] + 1 
    for i in xrange(n - 2, -1, -1):
        rhave[i] = gcd(rhave[i + 1] * ais[i], k)
        right[i] = (right[i + 1] * (ais[i] + 1)) % mod
    
    if rhave[0] % k != 0:
        return 0
    elif k in (0, 1):
        return right[0]
    else:
        return rsolve(1, 0)


if __name__ == "__main__":
    n, k = map(int, raw_input().strip().split())
    print "k: %s" % (k,)
    ais = filter(lambda x: x != 0, map(int, raw_input().strip().split()))
    print solve(len(ais), k, ais)


