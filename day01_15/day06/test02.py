"""
@projectName: Python100day
@file: test02.py
@description: TODO 判断一个数是不是素数
@date: 2020/2/9 1:35 上午
@author: YangLei
"""

import math


def is_prime(num):
    # 判断一个数是不是素数
    flag = False
    for factor in range(2, int(math.sqrt(num))+1):
        if num % factor == 0:
            flag = True
            break
    if flag or num == 1:
        return False
    else:
        return True

# print(is_prime(101))

def is_prime02(num):
    """判断一个数是不是素数"""
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False
