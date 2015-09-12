import unittest

def euclid(m, n):
    r = m % n
    if r == 0:
        return n
    else:
        return euclid(n, r)

class TestEuclid(unittest.TestCase):

    correct = [
        {
            'm': 119,
            'n': 544,
            'answer': 17,
        },
    ]
    incorrect = [
        {
            'm': 119,
            'n': 544,
            'answer': 1,
        },
    ]

    def test_correct(self):
        for test in self.correct:
            self.assertEqual(euclid(test['m'], test['n']), test['answer'])

    def test_incorrect(self):
        for test in self.incorrect:
            self.assertNotEqual(euclid(test['m'], test['n']), test['answer'])

if __name__ == '__main__':
    unittest.main()
