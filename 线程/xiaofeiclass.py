#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/14 15:34
import time
from threading import Thread

hamburger = 500


class Produce(Thread, object):
    def __init__(self, uname):
        super(Produce, self).__init__()
        self.uname = uname

    def run(self):
        global hamburger
        counter = 0
        while True:
            if hamburger >= 500:
                print(f'汉堡足够了{counter}')
                counter += 1
                time.sleep(3)
                continue

            else:
                print(f'{self.uname}做了一个汉堡,还有{hamburger}个')
                hamburger += 1


class Customer(Thread, object):
    def __init__(self, uname, money):
        super(Customer, self).__init__()
        self.uname = uname
        self.money = money

    def run(self):
        global hamburger
        while True:
            if self.money > 0 and hamburger > 0:
                hamburger -= 1
                self.money -= 5
                print(f'{self.uname}买了一个汉堡，还剩{self.money}元...')
            if self.money == 0:
                print(f'{self.uname}的钱花完了')
                break
            else:
                time.sleep(3)
                continue


chef1 = Produce('chef1')
chef2 = Produce('chef2')
chef3 = Produce('chef3')

pro1 = Customer('pro1', 100)
pro2 = Customer('pro2', 100)
pro3 = Customer('pro3', 100)
pro4 = Customer('pro4', 100)
pro5 = Customer('pro5', 100)
pro6 = Customer('pro6', 100)
chef1.start()
chef2.start()
chef3.start()
pro1.start()
pro2.start()
pro3.start()
pro4.start()
pro5.start()
pro6.start()
