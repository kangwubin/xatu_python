# coding:utf-8

# 内置函数id：返回变量的内存地址
# 内置函数len：返回字符串的长度，无法返回数字类型的长度    返回值 = len(字符串)
# 字符串的定义方式：''、""、""" """、
# 字符串仅支持拼接

name = 'KWB'
name_01 = 'SY'

print(id(name))
print(type(name))

print(id(name_01))
print(type(name_01))

new_name = name  # 将旧变量赋值给新变量，新变量与旧变量的内存地址是相同的
print(id(new_name))
print(type(new_name))

# 要输出带有引号的字符串

new_str = '我来自"西安"'
print(new_str)

new_str1 = "我来自'西安'"
print(new_str1)

# 空字符串
new_str2 = ''
print(len(new_str2))

