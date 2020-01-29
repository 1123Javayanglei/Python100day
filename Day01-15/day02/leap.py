"""
输入一个年份判断是否是闰年，若是输出true，否则输出false
(year%4 == 0 and year%100!=0)or(year%400==0)
"""
year = int(input('请输入年份：'))
leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(leap)
