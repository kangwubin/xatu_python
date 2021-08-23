# coding:utf-8

# int 0--false，非0--true
# float 0.0--false，非0.0--true
# str=''--false(即空字符串)，非空字符串--true
# Python：空类型，不属于任何数据类型，固定值：None表示，属于false的范畴

a = 0
b = 1
c = 0.0
d = 0.1
e = ''
f = 'None'
g = None

if __name__ == '__main__':
    print(bool(a))
    print(bool(b))
    print(bool(c))
    print(bool(d))
    print(bool(e))
    print(bool(f))
    print(bool(g))
