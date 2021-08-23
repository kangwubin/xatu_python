# coding:utf-8
"""
    1.元组是一种可以存储多种数据结构的队列
    2.元组是一个有序的、且元素可以重复的集合
    3.元组：tuple--用()定义一个元组
    4.如果一个元组中，只有一个成员，则该成员的后面必须带上 ","
    5.元组是一个无限制长度的数据结构
    6.元组与列表的区别：
     （1）元组比列表占用资源更小
     （2）列表是可变的，元组是不可变的--内存地址不可变
      (3) 元组创建好之后，它的值就不可改变了
      (4) 元组中的列表的值是不可修改的
    7.元组中的类型：('字符串')、(int)、(float)、(bool)、(None)、
                  ((int),(int))--元组套元组、([int],[int])--元组种存列表、
                  (('字符串'),(int),(float),(bool),(None))--混合类型元组
    8.列表中添加元组：[('a','b'),('c','d'),('e',)]   --  列表中元组的值也是不可更改的
    9.元组创建好之后，不能再向元组中添加数据
"""

tuple_test = ('KWB',)
print(tuple_test)
print(type(tuple_test))

tuple_test1 = ('SY')  # 当元组中只有一个成员时，若不加 "," ，则表示最初时的数据类型
print(type(tuple_test1))  # class: str

tuple_01 = ()
tuple_02 = (1, 2, 3)  # class: tuple
print(type(tuple_01))  # class: tuple
# print(type(tuple_02))  # class: tuple

print(bool(()))  # false
print(bool((1,)))  # true

print(len(tuple_02))

tuple_test2 = (1, 2, 3)
max_count = max(tuple_test2)
min_count = min(tuple_test2)
print(max_count)
print(min_count)

print(1 in tuple_test2)
res = 2 in tuple_test2
print(res)
