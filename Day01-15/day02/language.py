# 变量
# 分为int，double，String，布尔,复数形

a = 321
b = 123
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
# a // b a整除b
print(a % b)
print(a ** b)
# a**b 等价 a^b

print()
print()
print()

testOfA = 100
testB = 12.345
testC = 1 + 5j
testD = 'hello,world'
testE = True

print(type(testOfA))

# type(变量名) 获取变量的类型
"""
int():将一个数值或字符串转为整数，可指定进制
float()：将一个字符串转换为浮点数
str()：将指定的对象转为字符串，可以指定编码
chr()：整数转换为编码对应的字符
ord()：字符串(字符)转为对应的编码(整数)
"""
print(type(testB))
print(type(testC))
print(type(testD))
print(type(testE))

print()

"""
input()获取输入
int()类型转换
print使用了占位符,%d整数，%f小数，%%表示百分号
"""

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

print()
print()
print()
