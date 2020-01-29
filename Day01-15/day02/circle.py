"""
输入半径计算圆的周长和面积
面积 s=pi*(r**2)
周长 c=2*pi*r
"""
import math

r = float(input('请输入圆的面积'))
s = (math.pi * math.pow(r, 2))
c = 2 * math.pi * r
print('半径为%.2f的圆的面积是%.2f,周长是%.2f' % (r, s, c))
