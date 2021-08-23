# coding:utf-8
'''
    1.zfill()：为字符串定义长度，如不满足，缺少的部分用0填补
    2.与字符串的字符无关
    3.如果定义长度小于当前字符串长度，则不发生变化
'''

heart = 'love'

if __name__ == '__main__':
    print(' t  ' + heart)
    print('t    ' + heart)
    print(heart.zfill(10))
    print(heart.zfill(9))
    print(heart.zfill(8))
    print(heart.zfill(6))
    print(heart.zfill(4))

'''
    1.count()：返回当前字符串中某个成员(元素)的个数
    2.count()：如果查询的成员不存在，则返回 0 
'''

print('---------------------count函数使用如下------------------------')

info = '''
        The mission of the Python Software Foundation is to promote, protect, 
        and advance the Python programming language, 
        and to support and facilitate the growth of a diverse and international community of Python programmers
'''
a = info.count('a')
b = info.count('b')
c = info.count('c')
d = info.count('d')
e = info.count('e')
f = info.count('f')
print(a, b, c, d, e, f)
number_list = [a, b, c, d, e, f]
print(number_list)
print(max(number_list))
print(min(number_list))

number_dict = {
    'a': a,
    'b': b,
    'c': c,
    'd': d,
    'e': e,
    'f': f
}
print(number_dict)

print('--------------------------startswith()与endswith()使用如下--------------------------------')
'''
    1.startswith()：判断字符串开始位置是否是某成员
    2.endswith()：判断字符串结尾位置是否是某成员
'''
info1 = 'this is a string example !!!'
res = info1.startswith('this')
print(res)
res1 = info1.endswith('example')
print(res1)

res2 = info1.startswith('this is a string example !!!')
print(res2)  # true

print(bool(info1 == 'this is a string example !!!'))  # true
