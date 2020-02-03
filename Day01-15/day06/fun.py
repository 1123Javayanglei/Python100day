import random


def roll_dice(n=2):
    """摇骰子"""
    total = 0
    for _ in range(n):
        total += random.randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c


# 无指定，默认2颗
print(roll_dice())

print(roll_dice(3))

print(add())

print(add(1))

print(add(1, 2))

print(add(1, 2, 3))

# 可以不按照顺序，但是要指定参数名
print(add(c=5, a=100, b=200))

print(end='\n')


# 在参数名前面的*表示args是一个可变参数
def adds(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在调用adds函数时可以传入0个或多个参数
print(adds())

print(adds(1))

print(adds(1, 2))

print(adds(1, 2, 3))

print(adds(1, 2, 3, 4))

print(adds(1, 2, 3, 4, 5))
