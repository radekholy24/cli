#!/usr/bin/env python
"""``__main__`` module's tests."""

import os
import subprocess
import sys
import unittest


class TestCase(unittest.TestCase):
    """Tests of no arguments."""

    def test(self):
        """Test that it does nothing.

        Raises ``AssertionError`` if the test fails.

        """
        main = _run_main(
            # Make sure standard input is ignored.
            input_="whatever\r\n💚\0.",
            # Make sure the encoding is preserved.
            encoding="UTF-8",
            # Make sure LC_ALL does not affect the CLI's locale.
            language="zh_TW",
            stderr=subprocess.STDOUT,
            check=True)
        self.assertFalse(main.stdout)

    def test_encoding(self):
        """Test that it does nothing if a different encoding is used.

        Raises ``AssertionError`` if the test fails.

        """
        main = _run_main(
            # Make sure standard input is ignored.
            input_="whatever\r\n€\0.",
            # Make sure the encoding is preserved.
            encoding="ISO-8859-15",
            # Make sure LC_ALL does not affect the CLI's locale.
            language="et_EE",
            stderr=subprocess.STDOUT,
            check=True)
        self.assertFalse(main.stdout)


class UnrecognizedTestCase(unittest.TestCase):
    """Tests of an unrecognized argument."""

    def test(self):
        """Test that it fails gracefully.

        Raises ``AssertionError`` if the test fails.

        """
        main = _run_main(
            # Make sure standard input is ignored.
            input_="whatever\r\n💚\0.",
            # Make sure the encoding is preserved.
            encoding="UTF-8",
            # Make sure LC_ALL does not affect the CLI's locale.
            language="zh_TW",
            command_args=("--help",),
            # argparse wraps text to COLUMNS.
            width=7)
        self.assertTrue(main.returncode)
        self.assertFalse(main.stdout)
        self.assertEqual(
            main.stderr,
            "usage: __main__.py\n"
            "__main__.py: error: unrecognized arguments: --help\n")

    def test_encoding(self):
        """Test that it fails gracefully if a different encoding is used.

        Raises ``AssertionError`` if the test fails.

        """
        main = _run_main(
            # Make sure standard input is ignored.
            input_="whatever\r\n€\0.",
            # Make sure the encoding is preserved.
            encoding="ISO-8859-15",
            # Make sure LC_ALL does not affect the CLI's locale.
            language="et_EE",
            command_args=("--help",),
            # argparse wraps text to COLUMNS.
            width=7)
        self.assertTrue(main.returncode)
        self.assertFalse(main.stdout)
        self.assertEqual(
            main.stderr,
            "usage: __main__.py\n"
            "__main__.py: error: unrecognized arguments: --help\n")


def _run_main(
    *,
    input_="",
    encoding="UTF-8",
    language="en_US",
    command_args=(),
    width=80,
    stderr=subprocess.PIPE,
    check=False):
    """Run the ``__main__`` module with ``command_args``.

    The child process' environment variables are set as follows:

    "COLUMNS"
      ``width``

    "LC_ALL"
      ``f"{language}.{encoding}"``

    "PYTHONPATH"
      inherited from the current process' environment

    ``input_`` encoded with ``encoding`` is passed to the child process' standard input stream.

    New pipes to the child process' standard output and standard error streams are created. If ``stderr`` is
    ``subprocess.STDOUT``, the standard error is captured into the same file handle as the standard output.

    Returns a ``subprocess.CompletedProcess`` object with ``stdout`` and ``stderr`` as strings decoded using
    ``encoding``.

    If ``check`` is true, and the child process exits with a non-zero exit code, a ``subprocess.CalledProcessError``
    exception will be raised. Attributes of that exception hold the arguments, the exit code, and stdout and stderr as
    they were captured.

    """
    return subprocess.run(
        env={
            "COLUMNS": str(width),
            "LC_ALL": f"{language}.{encoding}",
            "PYTHONPATH": os.environ.get("PYTHONPATH", "")},
        input=input_,
        encoding=encoding,
        args=[sys.executable, "-m", "radekholy24.cli"] + list(command_args),
        stderr=stderr,
        stdout=subprocess.PIPE,
        check=check)


if __name__ == "__main__":
    unittest.main()
