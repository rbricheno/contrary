#!/usr/bin/env python3

# test_contrary.py - unittests for contrary

import unittest
import contrary


class TestContrary(unittest.TestCase):
    """Tests for `contrary.py`."""

    def test_contrary_blank_list_raises(self):
        self.assertRaises(AssertionError, contrary.Contrary, [])

    def test_contrary_none_raises(self):
        self.assertRaises(AssertionError, contrary.Contrary, None)

    def test_contrary_dict_raises(self):
        self.assertRaises(AssertionError, contrary.Contrary, {'apples': 'foo'})

    # TODO more tests!
