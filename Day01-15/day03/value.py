"""
分段函数求值
x>1 3x-5
x>=-1 and x<=1 x+2
x<-1 5x+3
"""
x = int(input('请输入一个数：'))
if x < -1:
    print('%d' % (5 * x + 3))
elif -1 <= x <= 1:
    print('%d' % (x + 2))
else:
    print('%d' % (3 * x - 5))
