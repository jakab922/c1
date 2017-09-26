import pytest
from random import shuffle, randint as ri


@pytest.fixture
def ais(request):
    args = request.node.funcargs
    n = args["n"]
    ret = [ri(1, n ** 2) for _ in xrange(n)]
    shuffle(ret)
    return ret

