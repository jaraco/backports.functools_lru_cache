backports.functools_lru_cache
=============================

Backport of functools.lru_cache from Python 3.3 as published at `ActiveState
<http://code.activestate.com/recipes/578078/>`_.

Usage
-----

Consider using this technique for importing the 'lru_cache' function::

    try:
        from functools import lru_cache
    except ImportError:
        from backports.functools_lru_cache import lru_cache
