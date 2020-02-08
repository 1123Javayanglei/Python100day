"""
@projectName: Python100day
@file: test04.py
@description: TODO 判断一个数是不是回文素数
@date: 2020/2/9 2:03 上午
@author: YangLei
"""
from day01_15.day06.test03 import *
from day01_15.day06.test02 import *

for num in range(1, 99):
    if __name__ == '__main__':
        # num = int(input('请输入正整数：'))
        if is_palindrome(num) and is_prime(num):
            print('%d是回文素数' % num)
