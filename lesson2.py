# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import numpy as np
#生成随机序列
def creat_list():
    randomnum=random.randint(1,100)
    list_num=[]
    for i in range(1,randomnum):
        list_num.append(i)
    random.shuffle(list_num)
    return list_num
#自动排序算法
def sort_num(list_num):
    temp=list_num.copy()
    num = len(temp)
    if num==1 or num==0:
        return temp
    flag_index=int(num/2)#以此为flag值
    flag_num=list_num[flag_index]
    left=0
    right=1
    for i in range(0,num):
        if list_num[i] < flag_num:#比flag小的放左边
            temp[left]=list_num[i]
            left=left+1
        elif list_num[i] > flag_num:#比flag大的放右边
            temp[num-right]=list_num[i]
            right=right+1
    temp[left]=flag_num
    left_num=temp[0:left]#左边
    right_num=temp[-right:]#右边
    return sort_num(left_num)+sort_num(right_num)#递归处理左右两边部分

listnum=creat_list()
print("原始序列：",listnum)
lnum=sort_num(listnum)
print("处理序列：",lnum)

        
            
        
            
            