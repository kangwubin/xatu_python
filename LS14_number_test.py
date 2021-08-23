# coding:utf-8

title = '康康学校的春游'
class_count = 55
boys = 28
girls = 23

every_body_pay = 35.5

start_time = 8.00
bus_count = 2
site_every_bus = 30

come_park_time = 10.30

lunch_time = 12.00
lunch_pay = 25.5

leave_park_time = 3.05

bus_pay = 5

come_back_school_time = 5.00

back_pay = 5

if __name__ == '__main__':
    print(title)
    print('康康的班级有：', class_count, '人')
    print('男生人数：', boys)
    print('女生人数：', girls)
    print('每人支付：', every_body_pay, '元')
    print('出发时间：', start_time)
    print('大巴数量：', bus_count, '辆')
    print('每辆大巴有座位数：', site_every_bus, '个')
    print('到达公园的时间是：', come_park_time)
    print('吃午饭的时间是：', lunch_time)
    print('午饭的价格是：', lunch_pay, '元')
    print('离开公园的时间是：', leave_park_time)
    print('乘车费用是：', bus_pay, '元')
    print('返回到学校的时间是：', come_back_school_time)
    print('这一天康康花了：', 30.5, '元')
    print('最后退回：', back_pay, '元')
    print(type(back_pay))
    print(type(come_back_school_time))
