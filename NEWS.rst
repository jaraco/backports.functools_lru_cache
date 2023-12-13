v2.0.0
======

Features
--------

- Refreshed implementation from CPython.


Deprecations and Removals
-------------------------

- Drop support for Python 2 and require Python 3.8 or later. In most cases, users should rely on the 1.x releases for an implementation that runs on older Pythons. This 2.0 series provides minimal value for users of Python 3.3 and later except to provide packaging updates and possibly preview access to functionality on later Python versions.


v1.6.6
======

Bugfixes
--------

- Restored install compatibilty on Python 2. (#20)


v1.6.5
======

No significant changes.


v1.6.4
======

#16: For test dependencies, when indicating Python 3, use ``>=3``
instead of ``>3`` to satisfy
`python-poetry/poetry#3862 <https://github.com/python-poetry/poetry/issues/3862>`_.

v1.6.3
======

#15: Restore universal wheel.

v1.6.2
======

Packaging refresh.

v1.6.1
======

Publish release notes on readthedocs.

v1.6.0
======

Refresh package metadata.
Use black for code style.
Enroll with Tidelift.

1.5
===

Refresh package metadata including publishing license with the
wheel (#11).

1.4
===

#9: Updated namespace package to use pkgutil for declaring the
namespace.

1.3
===

Tagged commits are automatically released following passing
tests.

1.2
===

Issue #5: Added a minimal test suite.

1.1
===

Moved hosting to Github.
Library uses setuptools_scm for version tagging.
Added license declaration.
