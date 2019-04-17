import pandas as pd
import os
import time


path = r'C:\Users\Andy\PycharmProjects\untitled6\easyship_view\history_data\2019\excel'
file_list = os.listdir(path)
today = os.path.join(path, file_list[-1])
yesterday = os.path.join(path, file_list[-2])
day_after_yesterday = os.path.join(path, file_list[-3])


def read_xls():
    yesterday_data = pd.read_excel(yesterday)
    day_after_yesterday_data = pd.read_excel(day_after_yesterday)
    today_data = pd.read_excel(today)
    yesterday_ratio = yesterday_data[['turnoverratio', 'name', 'per', 'changepercent']]
    day_after_yesterday_ratio = day_after_yesterday_data[['name', 'turnoverratio']]
    today_win = today_data[['name', 'settlement', 'high', 'changepercent']]
    today_win1 = today_win.rename(index=str, columns={'changepercent':'win'})
    old_sheet = pd.merge(day_after_yesterday_ratio, yesterday_ratio, on=['name'])
    sheet = pd.merge(old_sheet, today_win1, on=['name'])
    sheet['percent'] = (sheet['turnoverratio_y'] / sheet['turnoverratio_x']).round(2)
    new_sheet1 = sheet.sort_values(by='turnoverratio_y', ascending=False)
    new_sheet = new_sheet1.drop_duplicates(['name'])
    final = new_sheet.loc[(new_sheet['percent'] > 2) & (new_sheet['per'] < 40) & (new_sheet['per'] > 0) & (new_sheet['turnoverratio_y'] < 11) & (new_sheet['changepercent'] < 9) & (new_sheet['changepercent'] > 0) & (new_sheet['turnoverratio_x'] > 0.1)]
    full_win = final.loc[(new_sheet['win'] > 9.4)]
    fix_number = final.count()[0]
    print('涨停率：%s' % (full_win.count()[0]/fix_number))
    print('满足条件的共有%s个' % fix_number)
    sell_win = ((final['high']-final['settlement'])/final['settlement']*100).__round__(2)
    win_number = (sell_win[sell_win > 3]).count()
    all_number = sell_win.count()
    print('成功率：%s' % (win_number/all_number*100))
    print(final)


read_xls()

# 如何衡量成功率？
# 成功率：盘中有3%-5%个点的获利空间即为成功
# 涨停率：涨停收盘