#!/usr/bin/env python
score=int(input('请输入成绩：')) #获取用户成绩
#input获取的都是字符串  可以使用int()将字符串转为整数
if score >= 90:
    print('优秀')
elif score >= 80:
    print('很好')
elif score >= 70:
    print('良')
elif score >= 60:
    print('及格')
else:
    print('你要努力了')