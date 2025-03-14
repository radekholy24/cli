"""The test suite.

Submodules:

test___main__
  ``__main__`` module's tests

Additional test requirements:

* the en_US.ISO-8859-15 locale available
* the et_EE.ISO-8859-15 locale available
* the zh_TW.UTF-8 locale available

In order to run the tests, install the CLI, set the additional test requirements up and pass the selected tests to the
``unittest`` module. For example, execute the following command::

    /usr/bin/env python -m unittest

The ``unittest`` module is just enough to fulfill the task of testing the CLI. Thanks to that we can keep the usage of
the tests simple (no need to install a third-party module) and minimize the risks of supply chain attacks (which are low
anyway in this case, I guess).

"""
