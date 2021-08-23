# coding:utf-8
"""
  1.find：返回想寻找的成员的位置，返回一个整型，如果找不到，返回-1；
  2.index：返回想寻找的成员的位置，返回一个整型，如果找不到，会导致程序报错
  3.字符串里的位置：从左向右，从0开始
"""
info = 'python is a good code'
result = info.find('i')
print(result)

result1 = info.find('k')
print(result1)

result2 = info.index('a')
print(result2)
# result3 = info.index('m')  # error

'''
  1.strip：将去掉字符串左右两边的指定元素，默认是去掉空格-即strip中什么都不填；
    strip：传入的元素如果不在开头或结尾则无效
  2.lstrip：仅去掉字符串开头的指定元素或空格
  3.rstrip：仅去掉字符串结尾的指定元素或空格
'''
info_strip = ' my name is kwb'
new_info = info_strip.strip()
print(new_info)

'''
  1.replace：将字符串中某些旧的元素替换成新的元素，并能指定替换的数量
'''
