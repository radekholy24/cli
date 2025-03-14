=================
Radekholy24's CLI
=================

A CLI to a file server.

*Radekholy24's CLI* is being implemented incrementally towards the goal of developing a command-line interface which
retrieves files from a server, by providing means to select either a REST API or a gRPC API, to query either file
metadata or file contents, and to write the data either to a file or the standard output.

Roughly, the underlying principles that guide the design and implementation are:

* Documentation Driven Development
* reliability, stability, maintainability, and transparency
* The Zen of Python
* You aren't gonna need it
* Keep it simple, stupid

Contents
========

``radekholy24/cli/``
  the CLI; see ``radekholy24/cli/__init__.py``

``tests/``
  a test suite; see ``tests/__init__.py``

``CHANGELOG.rst``
  a list of changes for each version of the project

``LICENSE``
  see below

``README.rst``
  this file

pyproject.toml
  project metadata compliant with `PyPA pyproject.toml specification <https://packaging.python.org/en/latest/specifications/pyproject-toml/#pyproject-toml-spec>`__
  as of January 2025

See the individual packages for more information. You can either inspect them manually or use the Python's built-in help
system (i.e. the ``help`` function).

There are no ``AUTHORS``, ``CODE_OF_CONDUCT``, ``CODEOWNERS``, ``CONTRIBUTORS``, ``SECURITY``, and ``SUPPORT`` files as
there are no users and contributors expected.

The entire contents of the repository is free and open-source. More precisely, it is distributed under the MIT license
as the author strongly believes in the freedom to use, modify and redistribute any "intellectual property". Since the
laws of the Czech Republic do not allow authors of software to release their work into the public domain, the MIT
license was chosen as the most permissive, popular, and simple and stupid license available. See the ``LICENSE`` file
found in the top-level directory of this distribution. There are no license headers in the contained files as the
repository is always meant to be distributed as whole.

Requirements
============

* a Linux-based operating system
* the en_US.UTF-8 locale available
* `CPython 3.9 - 3.13 <https://www.python.org/>`__, `PyPy 3.10 - 3.11 <https://pypy.org/>`__ or `GraalPy 34.1 or compatible <https://www.graalvm.org/python/>`__

Packaging
=========

Generate a built distribution from this directory using your preferred `PEP 517 <https://peps.python.org/pep-0517/>`__
compatible package builder (such as `build <https://build.pypa.io/en/stable/index.html>`__). For example, execute the
following command::

  $ /usr/bin/env python -m build

Installation
============

Pack the CLI, set the requirements up and install the CLI's distribution. For example, execute the following command::

  $ /usr/bin/env python -m pip install dist/radekholy24_cli-0.1.0-py3-none-any.whl

Usage
=====

Run the ``radekholy24.cli`` package. For example, execute the following command::

  $ /usr/bin/env python -m radekholy24.cli

