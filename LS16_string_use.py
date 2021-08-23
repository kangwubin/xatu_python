# coding:utf-8

# 内置成员运算符：in--判断数据中是否存在想要的成员
# max：返回数据中最大的成员---中文符号>字母>数字>英文符号==[中文按照拼音的首字目来计算]
# min: 返回数据中最小的成员---中文符号>字母>数字>英文符号==[中文按照拼音的首字目来计算]

info = 'python是一个非常有魅力的语言'

result = '魅力' in info
print(result)

result1 = '语言' not in info
print(result1)

info2 = 'python is a good code'
print(max(info2))
print(',', min(info2), ',')

info3 = '天气好，要多锻炼身体' + ';'
info4 = '多锻炼身体，身体会变得更好' + "!"

info5 = info3 + info4
print(info3 + info4)
print(info5)


