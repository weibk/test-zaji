#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/19 15:08

import unittest
from ddt import ddt, unpack, data
from Calcium import Calcium
from bank import bank_transformMoney


@ddt()
class TestBank(unittest.TestCase):
    data3 = [
        ['ijklmnop', 'abcdefgh', '123456', 1000, 0],
        ['ijklmnop', 'abcdefgh', '123466', 1000, 2],
        ['ijklmnop', 'abcdefgh', '123456', 8000, 3],
        ['ijklmnop', 'abxdefgh', '123456', 1000, 1],
    ]

    @data(*data3)
    @unpack
    def test_bankadd(self, a, b, c, d, e):
        s = bank_transformMoney(a, b, c, d)
        self.assertEqual(s, e)
