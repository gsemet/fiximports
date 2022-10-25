import unittest

from unittest import mock

from fiximports.fiximports import FixImports
from fiximports.fiximports import main

example_input = """\
from any_module import d, f
from other_module import z, x
from any_module import b, e
from any_module import a, \\
                       c

from a_module_that_should_be import at, after, all_others
"""

example_expected = """\
from any_module import a
from any_module import b
from any_module import c
from any_module import d
from any_module import e
from any_module import f
from other_module import x
from other_module import z

from a_module_that_should_be import after
from a_module_that_should_be import all_others
from a_module_that_should_be import at
"""

class TestFixImport(unittest.TestCase):
    maxDiff = None

    def assertSortImports(self, data, expected, **kwargs):
        kwargs.setdefault("filename", "test.py")
        success, output = FixImports().sortImportGroups(data=data, **kwargs)
        self.assertTrue(success)
        self.assertEqual(expected, output)

    def test_readme_example(self):
        self.assertSortImports(example_input, example_expected)

    def test_sort_names(self):
        self.assertSortImports(
            "import b\nimport a\n",
            "import a\nimport b\n",
        )

    def test_sort_modules(self):
        self.assertSortImports(
            "from b import x\nfrom a import b\nfrom b import a\n",
            "from a import b\nfrom b import a\nfrom b import x\n",
        )

    def test_split_import(self):
        self.assertSortImports(
            "import b, a\n",
            "import a\nimport b\n",
        )

    def test_split_from_import(self):
        self.assertSortImports(
            "from m import b, c\n",
            "from m import b\nfrom m import c\n",
        )

    def test_statements_not_split(self):
        self.assertSortImports(
            "import os; import sys\n",
            "import os; import sys\n",
        )

    def test_reject_parenthesis(self):
        success, _ = FixImports().sortImportGroups("parens.py", "from m import (a, b)\n")
        self.assertFalse(success)

    @mock.patch("sys.argv", ["fiximports"])
    def test_cli_without_arguments(self):
        with self.assertRaises(SystemExit) as e:
            main()
        self.assertEqual(e.exception.code, 2)

    @mock.patch("sys.argv", ["fiximports", "--help"])
    def test_cli_help(self):
        with self.assertRaises(SystemExit) as e:
            main()
        self.assertEqual(e.exception.code, 0)

    @mock.patch("sys.argv", ["fiximports", "one.py", "two.py"])
    @mock.patch("fiximports.fiximports.open")
    @mock.patch("fiximports.fiximports.FixImports")
    def test_cli_filenames(self, fixer, mock_open):
        mocked_input = "# Mocked input\n"
        mocked_output = "# Mocked output\n"

        sort_imports = fixer.return_value.sortImportGroups
        sort_imports.return_value = (True, mocked_output)

        mock.mock_open(mock_open, mocked_input)

        rv = main()
        self.assertEqual(rv, 0)

        mock_open.assert_any_call("one.py", "r")
        mock_open.assert_any_call("two.py", "r")
        sort_imports.assert_any_call("one.py", mocked_input)
        sort_imports.assert_any_call("two.py", mocked_input)

        mock_open.assert_any_call("one.py", "w")
        mock_open.assert_any_call("two.py", "w")
        mock_open().write.assert_any_call(mocked_output)

    @mock.patch("sys.argv", ["fiximports", "one.py"])
    @mock.patch("fiximports.fiximports.open")
    def test_cli_errors(self, mock_open):
        mocked_input = "from m import (a, b)\n"
        mock.mock_open(mock_open, mocked_input)

        rv = main()
        self.assertEqual(rv, 1)

        mock_open.assert_any_call("one.py", "r")
        mock_open().write.assert_not_called()
