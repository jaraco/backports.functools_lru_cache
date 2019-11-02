import random

from backports.functools_lru_cache import lru_cache


def test_invocation():
    @lru_cache()
    def func():
        return random.random()

    assert func() == func()
