# coding:utf-8

"""
    1.字典：dict；字典是可以进行修改与添加的
    2.定义方式：a = dict{}; b = {}
    3.存储值：通过 {} 将一个个key与value存入字典中，key支持字符串、数字和元组类型，丹列表不支持，value支持所有Python的数据类型
    4.列表与元组中的字典：
     （1）dict_array = [{1:1,2:2},{'one':1,'two',2}]
      (2) dict_tuple = ({1:1,2:2},{'one':1,'two',2})   --- 元组中的字典是无法修改的，元组一旦创建，就不可改变
    5.Python3.7之前，字典是无序的；3.7之后是有序的；
    6.字典的重要特性：
    （1）字典中每一个key一定是唯一存在的
    （2）
"""

user_info = {'name': '康康', 'age': 18, 'top': '180cm'}

res = 'name' in user_info
print(res)

res = 'hope' not in user_info
print(res)

count = len(user_info)
print(count)

res_bool = bool(user_info)
print(res_bool)  # true

empty_dict = {}
print(bool(empty_dict))  # false
print(type(empty_dict))  # class: dict

print(max(user_info))
print(min(user_info))
