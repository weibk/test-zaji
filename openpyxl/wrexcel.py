#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/14 20:13
import openpyxl
from openpyxl import Workbook

wd = openpyxl.load_workbook('2020年每个月的销售情况.xlsx')
names = wd.sheetnames
print(names)

jen = wd[names[0]].values
print(jen)
for row in jen:
    print(row)
    for i in row:
        print(i)
