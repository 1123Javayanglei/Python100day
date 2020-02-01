"""
for 循环实现1～100求和
V：0.1
Author:杨磊

for-in 循环
"""
cnt = 0
for x in range(1, 101):
    # range(1,101) 产生一个1到100的整数序列
    # range(101) 从0到100的整数序列
    # range(1,100,2) 1到99的奇数序列，2是步长(即数值序列的增量)
    # range(2,101,2) 2到100的偶数序列，2是步长
    cnt += x
print('1 to 100 = %d' % cnt)
