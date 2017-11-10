import unittest
from fizzbuzz import robot

class FizzbuzzTest(unittest.TestCase):

    def test_say_1_when_1(self):
        self.assertEqual(robot(1), '1')

    def test_say_2_when_2(self):
        self.assertEqual(robot(2), '2')

    def test_say_fizz_when_3(self):
        self.assertEqual(robot(3), 'fizz')

    def test_say_4_when_4(self):
        self.assertEqual(robot(4), '4')

    def test_say_buzz_when_5(self):
        self.assertEqual(robot(5), 'buzz')

    def test_say_fizz_when_6(self):
        self.assertEqual(robot(6), 'fizz')

    def test_say_7_when_7(self):
        self.assertEqual(robot(7), '7')

    def test_say_8_when_8(self):
        self.assertEqual(robot(8), '8')

    def test_say_fizz_when_9(self):
        self.assertEqual(robot(9), 'fizz')

    def test_say_buzz_when_10(self):
        self.assertEqual(robot(10), 'buzz')

    def test_say_11_when_11(self):
        self.assertEqual(robot(11), '11')

    def test_say_fizz_when_12(self):
        self.assertEqual(robot(12), 'fizz')

    def test_say_13_when_13(self):
        self.assertEqual(robot(13), '13')

    def test_say_14_when_14(self):
        self.assertEqual(robot(14), '14')

    def test_say_fizzbuzz_when_15(self):
        self.assertEqual(robot(15), 'fizzbuzz')

if __name__ == "__main__":
    unittest.main()
