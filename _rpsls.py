# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 14:54:04 2021

@author: 86186
"""

#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：
日期：
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="石头":
        return 0;
    elif name=="史波克":
        return 1
    elif name=="布":
        return 2
    elif name=="蜥蜴":
        return 3
    else:
        return 4
        
        
        
    
    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果




def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        return "石头"
    elif number==1:
        return "史波克"
    elif number==2:
        return "布"
    elif number==3:
        return "蜥蜴"
    else:
        return "剪刀"

    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果

    pass #编写执行代码,代码完成后将pass删除


def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    print("你的选择是：",player_choice)
    a=name_to_number(player_choice)
    b=random.randint(0,4)
    s1=number_to_name(b)
    print("机器的选择是：",s1)
    comp(a,b)
    


    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

   


def comp(a,b):
    if a==b:
        print("不分胜负嗷！")
    if a==0 and (b==3 or b==4):
        print("恭喜你赢了！")
    if a==0 and (b==1 or b==2):
        print("不好意思机器赢了~")
    if a==1 and (b==0 or b==4):
        print("恭喜你赢了！")   
    if a==1 and (b==2 or b==3):
        print("不好意思机器赢了~")
    if a==2 and (b==0 or b==1):
        print("恭喜你赢了！")   
    if a==2 and (b==3 or b==4):
        print("不好意思机器赢了~")
    if a==3 and (b==1 or b==2):
        print("恭喜你赢了！")   
    if a==3 and (b==0 or b==4):
        print("不好意思机器赢了~")
    if a==4 and (b==2 or b==3):
        print("恭喜你赢了！")   
    if a==4 and (b==0 or b==1):
        print("不好意思机器赢了~")
# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
choice_name=input("请输入你的选择：")
rpsls(choice_name)

