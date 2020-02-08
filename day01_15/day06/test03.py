"""
@projectName: Python100day
@file: test03.py
@description: TODO 判断一个数是不是回文数
@date: 2020/2/9 1:54 上午
@author: YangLei
"""


def is_palindrome(num):
    # 判断一个数是不是回文数
    origin = num
    reversed_integer = 0
    # 翻转
    while num != 0:
        remainder = num % 10
        reversed_integer = reversed_integer * 10 + remainder
        num //= 10
    #       必须用地板除
    # 判断
    if origin == reversed_integer:
        return True
    else:
        return False

# print(is_palindrome(11))

def is_palindrome02(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num