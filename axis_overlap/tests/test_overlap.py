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
            print(test['name'])
            self.assertEqual(test['response'], overlaps(*test['data']))


if __name__ == '__main__':
    unittest.main()
