import unittest

from ..src.overlap import overlaps
from ..src.overlap import validate_input


class TestOverlap(unittest.TestCase):
    def test_overlapping(self):
        tests = [
            {
                'name': 'No overlapping',
                'data': ((1, 2), (3, 6)),
                'response': False
            },
            {
                'name': 'Overlapping',
                'data': ((2, 5), (1, 6)),
                'response': True
            },
            {
                'name': 'Overlapping (negative numbers)',
                'data': ((2, 5), (-1, 6)),
                'response': True
            },
            {
                'name': 'Overlapping (equal numbers)',
                'data': ((1, 5), (-1, 1)),
                'response': True
            },
            {
                'name': 'Overlapping (equal points)',
                'data': ((1, 1), (1, 1)),
                'response': True
            },
            {
                'name': 'No Overlapping (floating point numbers)',
                'data': ((1.5555, 6), (-1, 1.5)),
                'response': False
            },
            {
                'name': 'Overlapping (floating point numbers)',
                'data': ((1.5555, 6), (1, 1.6)),
                'response': True
            }
        ]

        for test in tests:
            self.assertEqual(test['response'], overlaps(*test['data']))

    def test_validate_input(self):
        tests = [
            {
                'name': 'Valid input',
                'data': ('1,6', '6,5'),
                'response': True
            },
            {
                'name': 'Valid input (floating point numbers)',
                'data': ('1.6576,6.78989', '6.77377,5.8909888'),
                'response': True
            },
            {
                'name': 'Valid input (negative floating point numbers)',
                'data': ('-1.6576,6.78989', '-6.77377,5.8909888'),
                'response': True
            },
            {
                'name': 'Invalid input',
                'data': ('1.9.3,9', '1.3.4,9.3.1'),
                'response': False
            },
            {
                'name': 'Invalid input',
                'data': ('1.9,9', '1.3.4,9.3.1'),
                'response': False
            },
            {
                'name': 'Invalid input',
                'data': ('1ab,9', '1.3,9bv'),
                'response': False
            }
        ]

        for test in tests:
            self.assertEqual(test['response'], bool(validate_input(*test['data'])))


if __name__ == '__main__':
    unittest.main()
