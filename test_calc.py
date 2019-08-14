# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

import unittest
import test_function


class TestCalc(unittest.TestCase):

    def test_add(self):
        # result = test_function.add(10, 5)
        self.assertEqual(test_function.add(10, 5), 15)
        self.assertEqual(test_function.add(-1, 1), 0)
        self.assertEqual(test_function.add(-1, -3), -4)

    def test_substract(self):
        # result = test_function.add(10, 5)
        self.assertEqual(test_function.substract(10, 5), 5)
        self.assertEqual(test_function.substract(-1, 1), -2)
        self.assertEqual(test_function.substract(-1, -3), 2)

    def test_multiply(self):
        # result = test_function.add(10, 5)
        self.assertEqual(test_function.multiply(10, 5), 50)
        self.assertEqual(test_function.multiply(-1, 1), -1)
        self.assertEqual(test_function.multiply(-1, -3), 3)

    def test_divide(self):
        # result = test_function.add(10, 5)
        self.assertEqual(test_function.divide(10, 5), 2)
        self.assertEqual(test_function.divide(-1, 1), -1)
        self.assertEqual(test_function.divide(-1, -1), 1)

        # self.assertRaises(ValueError, test_function.divide, 10, 0)

        with self.assertRaises(ValueError):
            test_function.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
