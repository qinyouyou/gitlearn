# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""

import os
import openpyxl
import xlrd
import pandas as pd

#遍历文件夹
def walkFile(file):
    for root, dirs, files in os.walk(file):
        #root 表示当前正在访问的文件夹路径
        #dirs 表示该文件夹下的子目录名list
        #files 表示该文件夹下的文件list
        
        #生成各年份初始表单
        #total_filepath=file+'/'+'total.xlsx'
        #creat_total_file(total_filepath)
        
        #遍历文件夹
        num=[]
        for d in dirs:
            num.append(int(d.split('s')[1]))
        num.sort()
        sort_d=[]#存储新顺序的目录
        for i in num:
            for d in dirs:
                if str(i)==d.split('s')[1]:
                    sort_d.append(root+'/'+d)
        return sort_d

#创建各年份原始表单                
def creat_total_file(file):
    wb=openpyxl.Workbook()
    for i in range(1990,2021):
        wb.create_sheet(str(i))#创建各个年份的表1990-2020
    wb.remove(wb['Sheet'])#删除原有的表
    wb.save(file)

#集成指定路径下所有的文件路径
def get_data_path(fd):
    data=[]
    for d in fd:
        file_path=get_file_path_name(d)
        data.append(file_path)#获得所有文件夹下的文件路径
    return data

#从所有文件夹路径中提取某一年份所有文件
def get_year_file(data,year):
    filepath=[]
    for filelist in data:
        for file in filelist:
            if os.path.basename(file).split('.')[0]==str(year):
                filepath.append(file)
    return filepath #获得某一年的所有文件

#返回指定文件夹内所有xlsx后缀文件
def get_file_path_name(path):
    name=[]
    for root,dirs,files in os.walk(path):
        for f in files:
            if f.split('.')[1]=='xlsx':
                name.append(path+'/'+f)
        return name#返回某一文件夹内xlsx后缀的所有文件

#获取某一年份所有文件内数据
def get_year_data(filepath):
    total=[]
    for file in filepath:
        df=pd.read_excel(file)
        total.append(df)
    yeardata = pd.concat(total, axis=1, join_axes=[total[0].index])
    return yeardata#获取某一年的所有数据

#写入所有年数据 
def write_data(path):
    d = walkFile(path)
    data = get_data_path(d)
    writer=pd.ExcelWriter(path+'/'+'total.xlsx')
    for year in range(1990,2021):
        filepath=get_year_file(data,year)
        year_data=get_year_data(filepath)
        #write_year_data(year,year_data,'D:/pylearn2021/test_data/total.xlsx')
        year_data.to_excel(writer,sheet_name=str(year))
    writer.save()
    
write_data('D:/pylearn2021/test_data')

    
    
    
    