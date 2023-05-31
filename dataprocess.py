# coding=utf-8
import copy
import time
import csv
import openpyxl
import pandas as pd
import numpy as np
from main_informer import show
from main_informer import train
new=pd.DataFrame(columns=['date','banner','col1'])
pd.set_option("display.max_colwidth", 300)
pd.set_option('expand_frame_repr',False)
pd.options.display.max_rows=None  # 显示最多行数
pd.options.display.max_columns=None # 显示最多列数
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
# outputflder=r'E:/code/genshin/dataset/data/'
log1 = open(r'E:/code/genshin/dataset/transfer.csv', mode='w')
log2 = open(r'E:/code/genshin/dataset/ETTh1.csv', mode='w')
df=pd.read_excel(r'E:/code/genshin/dataset/data/wish_record.xlsx')
# # df=df.loc[:,['时间','类别','星级']]
# df.index=range(len(df))
for i in range(len(df)):
    if int(df.iloc[i][3])==3:
        # num=1
        s = pd.Series([df.iloc[i][0],int(df.iloc[i][4]),int(14)], index=new.columns)
        new = new.append(s, ignore_index=True)
        # df.iloc[i][3]=1#3
    elif df.iloc[i][3]==4:
        if df.iloc[i][2]=='武器':
            # df.iloc[i][3]=2#40
            # num = 2
            s = pd.Series([df.iloc[i][0],int(df.iloc[i][4]),int(11)], index=new.columns)
            new = new.append(s, ignore_index=True)
        else:
            # df.iloc[i][3]=3#41
            # num = 3
            s = pd.Series([df.iloc[i][0],int(df.iloc[i][4]),int(11)], index=new.columns)
            new = new.append(s, ignore_index=True)
    else:
        if  df.iloc[i][2]=='武器':
            # df.iloc[i][3]=4#50
            # num = 4
            s = pd.Series([df.iloc[i][0],int(df.iloc[i][4]),int(17)], index=new.columns)
            new = new.append(s, ignore_index=True)
        elif df.iloc[i][2]=='角色' and (df.iloc[i][1]=='提纳里' or df.iloc[i][1]=='七七' or df.iloc[i][1]=='琴' or df.iloc[i][1]=='迪卢克' or df.iloc[i][1]=='莫娜' or df.iloc[i][1]=='刻晴' or df.iloc[i][1]=='迪希雅'):
            # df.iloc[i][3]=5#51
            # num = 5
            s = pd.Series([df.iloc[i][0],int(df.iloc[i][4]),int(17)], index=new.columns)
            new = new.append(s, ignore_index=True)
        else:
            # df.iloc[i][3]=4#50
            # num = 4
            s = pd.Series([df.iloc[i][0],int(df.iloc[i][4]),int(17)], index=new.columns)
            new = new.append(s, ignore_index=True)
# df=df.loc[:,['时间','类别','星级']]
# print(df,file=log1)
# def preprocess(filename):
#     df = pd.read_csv(r'E:/code/genshin/dataset/transfer.csv', sep=r'\s+', encoding='gbk', dtype=object)
#     dh = pd.read_excel(filename)
#     dh.index = range(len(dh))
#     for i in range(len(dh)):
#         if dh.iloc[i][3] == '3':
#             pass
#         elif dh.iloc[i][3] == '4':
#             if dh.iloc[i][2] == '武器':
#                 dh.iloc[i][3] = 40
#             else:
#                 dh.iloc[i][3] = 41
#         else:
#             if dh.iloc[i][2] == '武器':
#                 dh.iloc[i][3] = 50
#             elif dh.iloc[i][2] == '角色' and (
#                     dh.iloc[i][1] == '提纳里' or dh.iloc[i][1] == '七七' or dh.iloc[i][1] == '琴' or dh.iloc[i][
#                 1] == '迪卢克' or dh.iloc[i][1] == '莫娜' or dh.iloc[i][1] == '刻晴' or dh.iloc[i][1] == '迪希雅'):
#                 dh.iloc[i][3] = 51
#             else:
#                 dh.iloc[i][3] = 50
#     dh = dh.loc[:, ['时间', '类别', '星级']]
#     df=pd.concat([df,dh],ignore_index=True)
# for i in range(len(df)):
#     s = pd.Series([df.iloc[i][0], df.iloc[i][2]], index=new.columns)
#     new = new.append(s, ignore_index=True)
# print(df['date'])
print(new,file=log2)
print(new.columns)
# print(df.columns)
# df.to_csv(log2,index=False)
# df.index=range(len(df))
# print(df,file=log2))
# new=pd.DataFrame(columns=['data','star'])
# new=pd.concat([new,df],ignore_index=True)
# print(df,file=log2)
# df = pd.read_csv(r'E:/code/genshin/dataset/ETTh1.csv', sep=r'\s+', encoding='utf-8',quoting=3, dtype=object)
print(len(new))
# print(new)
# train()
pred=show()
print(pred,file=log1)
# train()
# pred=linear()
# print(pred)
# yhat=list(pred)
# print(yhat)
# print(len(yhat))
# file = np.load('E:/code/genshin/results/test_DLinear_custom_ftMS_sl40_ll20_pl90_dm512_nh1_el2_dl1_df2048_fc1_ebtimeF_dtTrue_test_3/pred.npy')
# print(file)
# np.savetxt('E:/code/genshin/results/test_DLinear_custom_ftMS_sl40_ll20_pl90_dm512_nh1_el2_dl1_df2048_fc1_ebtimeF_dtTrue_test_3/pred.txt',file)


