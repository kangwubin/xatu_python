# conding: utf-8

"""
1.身份运算符：判断两个对象存储单元是否相同--is、判断两个对象存储单元是否不同--is not
2.在控制台中输入两个数，判断两个不同变量名称的相同值(a = 18 , b = 18 ; a is b -- true)，因为Python解释器中的值是 (0 - 255),超出255，就会返回false
3.在pyCharm中，判断两个不同变量名称的相同值(a = 300 , b = 300 ; a is b -- true) ，因为Python解释器已经把 a 变量的值定义在了内存中【有了内存地址】，b 至少借用了一下
"""

a = 1
b = 2.2
c = 0
d = 18
e = -3
f = 300
f_01 = 300
d_01 = 18

print(a == b)
print(a != b)
print(a < b)
print(a > e)
print(d >= b)

print(d == d_01)  # true
print(d is d_01)  # true
print(id(d))  # 140709198961488
print(id(d_01))  # 140709198961488

print(f == f_01)
print(f is f_01)

print(f is d)
print(f is not d)
