import unittest

def extended_euclid(m, n, a=0, a_prime=1, b=1, b_prime=0):
    q, r = divmod(m, n)
    if r == 0:
        return n
    else:
        return extended_euclid(n, r, a, a_prime, b, b_prime)#, d, r)

class TestEuclid(unittest.TestCase):

    def test_0(self):
        self.assertEqual(extended_euclid(6, 8), 2)

    def test_1(self):
        self.assertEqual(extended_euclid(55, 121), 11)

    def test_2(self):
        self.assertEqual(extended_euclid(119, 544), 17)

    def test_3(self):
        self.assertEqual(extended_euclid(1769, 551), 29)

if __name__ == '__main__':
    unittest.main()
