#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/15 15:59

import unittest


class TestAbsFunc(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_positive(self):
        self.assertEqual(abs(1), 1)
        self.assertEqual(abs(1.2), 1.2)
        self.assertEqual(abs(0.99), 0.99)

    def test_negative(self):
        self.assertEqual(abs(-1), 1)
        self.assertEqual(abs(-1.2), 1.2)
        self.assertEqual(abs(-0.99), 0.99)
        
    def test_zero(self):
        self.assertEqual(abs(0), 0)
        
    def test_nonumber(self):
        with self.assertRaises(TypeError):
            abs(None)
        with self.assertRaises(TypeError):
            abs([])
        with self.assertRaises(TypeError):
            abs({})
