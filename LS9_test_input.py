# coding:utf-8
"""
    1、input函数，接受一个标准输入，返回String
"""
name = input('你的名字是：')
birthday = input('你的生日是：')
like_fruit = input('喜欢的水果是：')
like_sport = input('喜欢的运动是：')
like_animal = input('喜欢的动物是：')
print('你的名字叫：%s，你的生日是：%s，你喜欢的水果是：%s，你喜欢的运动是：%s，你喜欢的动物是:%s'
      % (name, birthday, like_fruit, like_sport, like_animal))  # 表示格式化的内容
