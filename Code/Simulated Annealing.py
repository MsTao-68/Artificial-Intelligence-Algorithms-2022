# !usr/bin/python
# Author: Tracy Tao
# Date：2022/03/25
# -*- coding: utf-8 -*-
# Simulated Annealing

import sko
from sko.SA import SA
import matplotlib.pyplot as plt
import pandas as pd


def demo_func(x):
    '''
    多元函数优化
    :param x: x序列
    :return: 目标函数值
    '''
    x1, x2, x3 = x
    return x1 ** 2 + (x2 - 0.05) ** 2 + x3 ** 2


sa = SA(func=demo_func, x0 = [1,1,1], T_max=1, T_min=1e-9, L=300, max_stay_counter=150)
x_star, y_star =sa.run()
plt.plot(pd.DataFrame(sa.best_y_history).cummin(axis=0))
plt.show()

'''
旅行商问题
'''
import numpy as np
import time
import random
import math

T_start = 5000.0#初始温度
T_end = 1#终止温度
q_ratio = 0.98#温度衰减系数
L_max = 100#同一个温度下迭代次数
city_cnt = 31
#城市坐标
data = [(1304,2312),(3639,1315),(4177,2244),(3712,1399),
            (3488,1535),(3326,1556),(3238,1229),(4196,1004),
            (4312,790),(4386,570),(3007,1970),(2562,1756),
            (2788,1491),(2381,1676),(1332,695),
            (3715,1678),(3918,2179),(4061,2370),
            (3780,2212),(3676,2578),(4029,2838),
            (4263,2931),(3429,1908),(3507,2367),
            (3394,2643),(3439,3201),(2935,3240),
            (3140,3550),(2545,2357),(2778,2826),
            (2370,2975)
]

def calTotalDistance(result):
    '''
    评价函数，在旅行商问题中就是距离
    :param result: 需要计算的结果，结果形式为城市的索引，[index1, index2, index3....]
    :return:
    '''

    sum = 0
    for i in range(0,30):
        sum = sum+math.sqrt(pow((data[result[i]][0]-data[result[i+1]][0]), 2) +
                          pow((data[result[i]][1]-data[result[i+1]][1]), 2))
    return sum


def generate_new_result(old_result):
    '''
    随机交换两个城市
    :param old_result:旧解
    :return:新解
    '''
    city1 = random.randint(0, 30)
    city2 = random.randint(0, 30)

    # 深度复制旧结果
    new_result = old_result[:]
    # 交换结果中两个城市的位置
    new_result[city1], new_result[city2] = new_result[city2], new_result[city1]
    return new_result
# 开始模拟退火算法
result = []

# 随机产生初始结果，这里直接顺序添加
for i in range(city_cnt):
    result.append(i)
# 定义初始温度
T = 5000
# 最低温度
T_min = 1e-8
# 冷却率
cooling_rate = 0.98
# 每次退火时，迭代次数
iterors = 5000
# 记录有多少次新解没有被采纳
no_cnt = 0
# 记录解的变化
result_record = []
while T > T_min:
    for i in range(iterors):
        result_record.append(calTotalDistance(result))
        new_result = generate_new_result(result)
        # 判断新解和旧解哪个更好,这里需要注意新解-旧解, diff的正负会影响采纳新解的概率
        diff = calTotalDistance(new_result) - calTotalDistance(result)
        # 新解更好， 因为result>new_result
        if diff < 0:
            # 重新计数
            no_cnt = 0
            # 采纳新解
            result = new_result[:]
        else:
            no_cnt += 1
            # 新解更坏，这时候以一定几率踩纳
            P = pow(math.e, diff/T)
            # 如果随机数在概率之内，则采纳
            if random.random() < P:
                result = new_result[:]
    # 退火降温
    T = T * cooling_rate
    print(T)
    # 超过5000次没有被采纳，则结束迭代
    if no_cnt > 5000:
        break
result.append(result[0])
x = [data[index][0] for index in result]
y = [data[index][1] for index in result]
plt.figure(figsize=(15,10))
plt.plot(x,y,'o')
plt.plot(x,y,linewidth=1,color='red')
plt.plot(x[0],y[0],'v',markersize=20)
plt.title('SA_TSP')
plt.show()
