"""
用户身份验证
name:yang
pwd:123
"""
userName = input('请输入用户名：')
passWorld = input('请输入密码：')
leap = userName == 'yang' and passWorld == '123';
if leap:
    print('成功')
else:
    print('失败')
