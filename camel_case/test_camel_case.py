from camel_case import camel_case
import unittest
from unittest import TestCase


class TestCamelCase(TestCase):

    def test_camel_case_with_strings_only(self):
        given_sentence = 'Surely this will work'
        correct_output = 'surelyThisWillWork'
        self.assertEqual(correct_output, camel_case.camel_case(given_sentence))

    def test_with_lots_of_spaces(self):
        given_sentence = '      maybe    this  one  '
        correct_output = 'maybeThisOne'
        self.assertEqual(correct_output, camel_case.camel_case(given_sentence))

    def test_no_special_chars(self):
        given_sentence = '  maybe    !@#$this &^%$#  one  '
        correct_output = 'maybeThisOne'
        self.assertEqual(correct_output, camel_case.camel_case(given_sentence))



if __name__ == '__main__':
    unittest.main()
