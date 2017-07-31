# -*- coding: utf-8 -*-

import unittest
import morse


class BasicTestSuite(unittest.TestCase):
    """Docs here."""

    def test_cyclic(self):
        # We should be able to make a round trip with encoding/decoding
        aString = "HERE IS A STRING TO TEST 12345"
        result = morse.translate.decode(morse.translate.encode(aString))
        self.assertEqual(aString, result)

    def test_cyclic2(self):
        aString = "HERE IS A STRING TO TEST 12345"
        result = morse.translate.decode(morse.translate.encode(aString))
        self.assertEqual(aString, result)


if __name__ == '__main__':
    unittest.main()
