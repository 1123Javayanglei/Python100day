"""
AttributeError: module 'random' has no attribute 'randint'
报错原因：fileName random和random(moduleName) 冲突
"""
import random

answer = random.randint(1, 100)

counter = 0
while True:
    counter += 1
    number = int(input('请输入:'))
    if number > answer:
        print('大了')
    elif number < answer:
        print('小了')
    else:
        print('你答对了')
        break
print('你一共猜了%d次 ' % counter)
if counter > 7:
    print('你的智商余额不足')


