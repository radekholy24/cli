#!/usr/bin/env python
"""The CLI.

In order to run the CLI, run this module. For example, execute the following command::

  $ /usr/bin/env python -m radekholy24.cli

or::

  $ ./__main__.py

"""

import argparse
import locale

if __name__ == "__main__":
    # Make sure locale is in US English language since the texts are in US English too.
    locale.setlocale(locale.LC_ALL, ("en_US", locale.getpreferredencoding()))
    parser = argparse.ArgumentParser(add_help=False)
    parser.parse_args()
