#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/19 16:42

import unittest
from ddt import ddt, unpack, data
from Calcium import Calcium


@ddt
class TestCalcAdd(unittest.TestCase):
    data1 = [
        [1, 2, 3],
        [7, 8, 15],
        [-7, 8, 1],
        [7, -8, -1],
        [-7, -8, -15],
        [7, 0, 7],
        [0, 8, 8]
    ]

    @data(*data1)
    @unpack
    def test_calcadd(self, a, b, c):
        calc = Calcium()
        self.assertEqual(calc.add(a, b), c)
