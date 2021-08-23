# coding:utf-8

"""
    1.python中的赋值运算符
    2.字符串只可以和数字作乘法
    3.列表、元组可以做乘法
    4.字典类型不能做乘法
"""
a = 1
b = 2
c = 3
e = 4
d = a + b + c
print(d)

d += c
print(d)

d -= a
print(d)

d *= b
print(d)

a /= b
print(a)  # 0.5

a //= b
print(a)  # 0.0

c %= 1
print(c)  # 0

e %= 3
print(e)  # 1

f = 10
f **= 2  # 平方运算
print(f)  # 100

# 列表乘法
list_01 = [1, 2, 3]
print(list_01 * 2)  # [1, 2, 3, 1, 2, 3]

# 元组乘法
tuple_01 = (1, 2, 3)
print(id(tuple_01))  # 140398583195968

print(tuple_01 * 2)  # (1, 2, 3, 1, 2, 3)
print(id(tuple_01 * 2))  # 140398583066240

gb = 1
b = gb * 1024 * 1024 * 1024
print(b)
