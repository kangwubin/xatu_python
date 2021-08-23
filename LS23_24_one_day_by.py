# coding: utf-8

user_name = '小慕'
get_up_time = '8:00'
bf_time = '8:30'  # 早餐时间
bf_contents = ['牛奶', '面包', '麦片']

study_time = '9:00'
books = ('高等数学', '历史', 'python入门')
study_book = 'python入门'

ready_lunch_time = '12:00'
brother_phone = 123456789
real_lunch_time = '12:55'
lunch_pay = 12.5
lunch_name = '西红柿鸡蛋盖饭'

shopping_time = '1:25'
shop = {
    'snacks': ['薯片', '锅巴', '饼干'],
    'live': ['洗发水', '香皂', '沐浴露'],
    'fruits': ['苹果', '香蕉', '哈密瓜', '橘子', '西瓜'],
    'vegetables': ['西红柿', '黄瓜', '韭菜', '大白菜'],
    'drinks': ['雪碧', '可乐', '矿泉水']
}

a, b, c = 5, 10, 15
cola_pay = 2.5
potato = 4
apple_two = 1.2
cabbage = 0.9

total = cola_pay + potato + apple_two + cabbage + c

sport_time = 2.5
before_weight = 44.78
after_weight = 44.76

go_backhome_time = '5:00'

if __name__ == '__main__':
    print('我们的主人公是：', user_name)
    print('他是', get_up_time, '起床')
    print(bf_time, '吃早餐')
    print('早餐都有：', bf_contents)
    print(study_time, '开始学习')
    print('书架上都有', books)
    print(user_name, '看的书是：', study_book)
    print(user_name, '准备', ready_lunch_time, '吃午饭')
    print('外卖小哥的电话是：', brother_phone)
    print(user_name, '在', real_lunch_time, '开始吃饭')
    print('他午饭吃的是：', lunch_name, '并且价格是：', lunch_pay)
    print('购物的时间是：', shopping_time)
    print('超市柜台有：', shop)
    print(user_name, '共花费了：', total, '元')
    print('购物之后，去健身了')
    print('健身之前的体重是：', before_weight)
    print('经过了', sport_time, '小时锻炼')
    print('体重变成了', after_weight)
    print(user_name, '在', go_backhome_time, '回家了')
