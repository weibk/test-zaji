#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/19 16:43

import unittest
from ddt import ddt, unpack, data
from Calcium import Calcium


@ddt
class TsetCalcMinus(unittest.TestCase):
    data2 = [
        [1, 2, -1],
        [7, 8, -1],
        [-7, 8, -15],
        [7, -8, 15],
        [-7, -8, 1],
        [7, 0, 7],
        [0, 8, -8]
    ]

    @data(*data2)
    @unpack
    def test_calcminus(self, a, b, c):
        calc = Calcium()
        self.assertEqual(calc.minus(a, b), c)
