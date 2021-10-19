#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/19 16:47
import os
import threading
import unittest
from HTMLTestRunner import HTMLTestRunner
from threading import Thread


class Banktest(Thread):
    def run(self):
        threadLock.acquire()
        tests = unittest.defaultTestLoader.discover(os.getcwd(),
                                                    pattern='TestBank.py')
        runner = HTMLTestRunner.HTMLTestRunner(
            title='测试报告',
            description='银行转账测试报告',
            verbosity=1,
            stream=open(file='bankreport.html', mode='w+', encoding='utf-8')
        )

        runner.run(tests)
        threadLock.release()


class Addtest(Thread):
    def run(self):
        threadLock.acquire()
        tests = unittest.defaultTestLoader.discover(os.getcwd(),
                                                    pattern='TestCalcAdd.py')
        runner = HTMLTestRunner.HTMLTestRunner(
            title='测试报告',
            description='加法测试报告',
            verbosity=1,
            stream=open(file='addreport.html', mode='w+', encoding='utf-8')
        )

        runner.run(tests)
        threadLock.release()


class Minustest(Thread):
    def run(self):
        threadLock.acquire()
        tests = unittest.defaultTestLoader.discover(os.getcwd(),
                                                    pattern='TestCalcMinus.py')
        runner = HTMLTestRunner.HTMLTestRunner(
            title='测试报告',
            description='减法测试报告',
            verbosity=1,
            stream=open(file='minusreport.html', mode='w+',
                        encoding='utf-8')
        )

        runner.run(tests)
        threadLock.release()

threadLock = threading.Lock()

t1 = Banktest()
t2 = Addtest()
t3 = Minustest()
t1.start()
t2.start()
t3.start()
