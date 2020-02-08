from day01_15.day06.module1 import foo

print('第一种:\n')
# python 倒入模块 必须是 "python package" ,普通目录无法导入模块，且必须加上全名
foo()
# out hello

from day01_15.day06.module2 import foo

foo()
# out goodbye


import day01_15.day06.module1 as m1
import day01_15.day06.module2 as m2

print('第二种:\n')
m1.foo()
m2.foo()

print('第三种:\n')
from day01_15.day06.module1 import foo
from day01_15.day06.module2 import foo

foo()
# out goodbye ,因为第一个foo被第二个foo覆盖


import day01_15.day06.module3
# 导入 module3时 不会执行模块中if成立时的代码，因为模块的名字是module3而不是__main__
