# coding:utf-8
"""
   1.（1）列表：即队列，各种数据类型的集合，一种数据结构；
     （2）列表是一种有序，且内容可重复的集合类型
     （3）列表内置函数：list--用[]表示
     （4）列表是一个无限长度的数据结构
     （5）列表中的类：[字符串、int、float、bool、None]、[[int],[float]]--列表嵌套列表
"""

none_list = [None, None, None]
print(none_list)
print(bool(none_list))  # true
print(len(none_list))
print()

print([])
print(bool([]))  # false
print(len([]))  # 0
print()

max_list1 = [1, "KWB", 3.14]  # 混合数据类型的max\min是不能进行计算的
max_list = [1, 3.14]
id_address = max_list
print(max(max_list))
print(min(max_list))
print(id(max_list))
print(id(id_address))
