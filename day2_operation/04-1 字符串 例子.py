'''
停车管理系统
'''
import time
import random

print('-' * 49)
print('-' * 15, '欢迎来到万宝停车场', '-' * 15)
print('-' * 49)

# 请先择功能
cars_list = []  # 停车场
MAX_CAR = 5  # 最多停车数 常量 全大写。
pos_list = ['1位', '2位', '3位', '4位', '5位']  # 剩余车位的标号信息 初始有5个车位。
cur_carNumber = 0  # 当前停车数量。
while True:
    choice = int(input('请选择功能：1.进入停车场 2.驶出停车场 3.查询停车场 4.查询所有车辆 5.退出系统'))
    # 判断选择功能
    if choice == 1:
        # 进入停车场
        if cur_carNumber < MAX_CAR:
            car_nubmer = input('输入你的车牌号码：')
            # 记入场时间
            start = time.time()  # 时间戳。 从1970.0.0.0.0到现在的秒数。
            # 随机分配车位。
            pos = random.choice(pos_list)  # choice从序列找随机找一个元素。
            # 删除pos随机的位置
            pos_list.remove(pos)
            # 填加到停车场中
            car_message = [car_nubmer, start, pos]
            cars_list.append(car_message)  # 列表中的元素仍是一个列表。
            cur_carNumber += 1
            print('{}停车完毕'.format(car_nubmer))
        else:
            print('车位已满，请选择其他停车场或等候')

    elif choice == 2:
        # 驶出停车场
        print('-' * 49)
        print('-' * 15, '驶出停车场', '-' * 15)
        print('-' * 49)
        out_carno = input('输入驶出车牌号码：')

        # 查询
        # 遍历停车场
        for car_msg in cars_list:
            # car_msg 是一个列表[车牌，时间戳，位置]
            if out_carno in car_msg:  # 车牌号在列表中
                # 出去
                # 开始计算费用
                end = time.time()
                cha = end - car_msg[1] #单位是秒
                #小时转换 除3600
                hour = cha//3600 #整数部分，小数部分
                money = hour *5 #一小时5元
                print ('车牌号：{}，停车时间是{}，费用：{}'.format(out_carno,hour,money))

                # 占用位置归位。
                pos_list.append(car_msg[2]) #车的位置信息加入
                # 当前停车数量-1
                cur_carNumber -= 1
                #从停车场中停除车辆信息
                cars_list.remove(car_msg)
                break
        else:
            print('停车场中没有此车：', search_no)
    elif choice == 3:
        # 查询车辆信息
        print('-' * 49)
        print('-' * 15, '查询车辆信息', '-' * 15)
        print('-' * 49)
        search_no = input('输入车牌号码：')
        # 遍历停车场
        for car_msg in cars_list:
            # car_msg 是一个列表[车牌，时间戳，位置]
            if search_no in car_msg:  # 车牌号在列表中
                print('{} 在停车场中'.format(search_no))
                break
        else:
            print('停车场中没有此车：', search_no)
    elif choice == 4:
        # 查询所有车辆
        print('-' * 49)
        print('-' * 15, '显示所有车辆信息', '-' * 15)
        print('-' * 49)
        for car_msg in cars_list:
            print(car_msg[0], car_msg[1], car_msg[2])
    elif choice == 5:
        answer = input('确定退出停车管理系统吗？(y/n)')
        if (answer.lower() == 'y'):
            print('即将退出停车管理系统')
            time.sleep(1)
            print('系统关闭！')
            break
    else:
        print('输入错误，请重新选择！')
