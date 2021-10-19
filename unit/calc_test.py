#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/18 10:13
import unittest
from Calcium import Calcium


class CalcTest(unittest.TestCase):
    def test_add1(self):
        calc = Calcium()
        self.assertEqual(calc.add(7, 8), 15)

    def test_add2(self):
        calc = Calcium()
        self.assertEqual(calc.add(-7, 8), 1)

    def test_add3(self):
        calc = Calcium()
        self.assertEqual(calc.add(7, -8), -1)

    def test_add4(self):
        calc = Calcium()
        self.assertEqual(calc.add(0, 8), 8)

    def test_add5(self):
        calc = Calcium()
        self.assertEqual(calc.add(0, -8), -8)

    def test_add6(self):
        calc = Calcium()
        self.assertEqual(calc.add(0, 0), 0)

    def test_minus1(self):
        calc = Calcium()
        self.assertEqual(calc.minus(7, 8), -1)

    def test_minus2(self):
        calc = Calcium()
        self.assertEqual(calc.minus(8, 7), 1)

    def test_minus3(self):
        calc = Calcium()
        self.assertEqual(calc.minus(0, 8), -8)

    def test_minus4(self):
        calc = Calcium()
        self.assertEqual(calc.minus(0, -8), 8)

    def test_minus5(self):
        calc = Calcium()
        self.assertEqual(calc.minus(8, 0), 8)

    def test_minus6(self):
        calc = Calcium()
        self.assertEqual(calc.minus(-8, 0), -8)

    def test_multiply1(self):
        calc = Calcium()
        self.assertEqual(calc.multiply(1, 8), 8)

    def test_multiply2(self):
        calc = Calcium()
        self.assertEqual(calc.multiply(0, 8), 0)

    def test_multiply3(self):
        calc = Calcium()
        self.assertEqual(calc.multiply(5, 8), 40)

    def test_multiply4(self):
        calc = Calcium()
        self.assertEqual(calc.multiply(-5, 8), -40)

    def test_multiply5(self):
        calc = Calcium()
        self.assertEqual(calc.multiply(-5, -8), 40)

    def test_divide1(self):
        calc = Calcium()
        self.assertEqual(calc.divide(10, 5), 2)

    def test_divide2(self):
        calc = Calcium()
        self.assertEqual(calc.divide(10, -5), -2)

    def test_divide3(self):
        calc = Calcium()
        self.assertEqual(calc.divide(-10, 5), -2)

    def test_divide4(self):
        calc = Calcium()
        self.assertEqual(calc.divide(-10, -5), 2)

    def test_divide5(self):
        calc = Calcium()
        self.assertEqual(calc.divide(0, 10), 0)

    def test_divide6(self):
        calc = Calcium()
        self.assertEqual(calc.divide(0, -10), 0)

    def test_divide7(self):
        calc = Calcium()
        with self.assertRaises(ZeroDivisionError):
            calc.divide(10, 0)

    def test_divide8(self):
        calc = Calcium()
        with self.assertRaises(ZeroDivisionError):
            calc.divide(-10, 0)


if __name__ == '__main__':
    unittest.main()
