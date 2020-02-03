import unittest

from .context import compare


class TestVersionValidation(unittest.TestCase):
    def test_validation(self):
        tests = [
            {
                'name': 'Equal',
                'data': ('1.2.3', '1.2.3'),
                'response': ('1.2.3',)
            },
            {
                'name': 'v1 greater than v2',
                'data': ('2.0.1', '2.0.0'),
                'response': ('2.0.0', '2.0.1')
            },
            {
                'name': 'v2 greater than v1',
                'data': ('0.1.0', '1.0.0.0.1'),
                'response': ('0.1.0', '1.0.0.0.1')
            },
            {
                'name': 'v1 greater than pre-release v2',
                'data': ('2.0.1', '2.0.1-alpha'),
                'response': ('2.0.1-alpha', '2.0.1')
            },
            {
                'name': 'pre-release v1 greater than pre-release v2',
                'data': ('3.0.1-beta', '3.0.1-alpha'),
                'response': ('3.0.1-alpha', '3.0.1-beta')
            },
            {
                'name': 'pre-release v1 greater than pre-release v2',
                'data': ('3.0.1-beta', '3.0.1-beta.1'),
                'response': ('3.0.1-beta', '3.0.1-beta.1')
            },
            {
                'name': 'pre-release v2 greater than pre-release v1',
                'data': ('3.0.1-beta', '3.0.1-rc.1'),
                'response': ('3.0.1-beta', '3.0.1-rc.1')
            },
            {
                'name': 'Bad input',
                'data': ('3,0,1', 'bad_input'),
                'response': None
            }
        ]

        for test in tests:
            self.assertEqual(test['response'], compare(*test['data']))


if __name__ == '__main__':
    unittest.main()
