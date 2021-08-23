# coding: utf-8

'''
      1.字符串capitalize()首字母大写方法
      2.capitalize()对数字、中文不起作用；首字目原为大写字母，也不起作用
'''
str = 'good'
new_str = str.capitalize()
print(new_str)

'''
    1.lower()、casefold()：将字符串全体小写
    2.只对字符串中的字母有效，已经是小写，则无效
    3.casefold()相比lower是在python3.3后引入，支持更多语言
'''
str1 = 'XATU'
new_str1 = str1.lower()
print(new_str1)
new_str1_1 = str1.casefold()
print(new_str1_1)

'''
    1.upper()：将字符串全体大写
    2.只对字符串中的字母有效，已经是大写，则无效
'''
str2 = 'xatu'
new_str2 = str2.upper()
print(new_str2)

'''
    1.swapcase()：将字符串中大小写字符进行转换
    2.只对字符串中的字母有效
'''
str3 = 'KangWuBin'
new_str3 = str3.swapcase()
print(new_str3)
