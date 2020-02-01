"""
九九乘法表
V:0.1
A:杨磊
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d+%d+%d' % (i, j, i * j), end='\t')
    print()
