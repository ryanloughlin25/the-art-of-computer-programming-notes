import unittest

def euclid(m, n):
    r = m % n
    if r == 0:
        return n
    else:
        return euclid(n, r)

class TestEuclid(unittest.TestCase):
    def test_0(self):
        self.assertEqual(euclid(6, 8), 2)

    def test_1(self):
        self.assertEqual(euclid(55, 121), 11)

    def test_2(self):
        self.assertEqual(euclid(119, 544), 17)

if __name__ == '__main__':
    unittest.main()
