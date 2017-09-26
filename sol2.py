from fractions import gcd
from collections import defaultdict as dd

MOD = 10 ** 9 + 7


def sol(n, k, ais):
    # special cases
    if not ais:
        return 0
    if k in (0, 1):
        # substracting 1 since we assume that the empty product is 0
        return reduce(lambda x, y: x * (y + 1), ais, 1) - 1

    curr = {1: 1}
    for ai in ais:
        nxt = dd(int)
        for key in curr:
            for el in (1, ai):
                nkey = key * gcd(k / key, el)
                nxt[nkey] = (nxt[nkey] + el * curr[key]) % MOD
        curr = nxt

    return curr[k]


if __name__ == "__main__":
    n, k = map(int, raw_input().strip().split())
    ais = filter(lambda x: x != 0, map(int, raw_input().strip().split()))
    n = len(ais)
    print sol(n, k, ais)

