import pandas as pd
import os
import tushare
import time

def get_today_data():
    file_name = 'today.xls'
    try:
        today = tushare.get_today_all()
        today.to_excel(file_name, index=False)
    except Exception as e:
        print(e)


def read_xls():
    yesterday = int(time.strftime("%Y%m%d", time.localtime()))-1
    yesterday_file = 't' + str(yesterday)
    yesterday_data = pd.read_excel('../history_data/2019/excel/%s.xls' % yesterday_file, encoding='utf-8')
    today_file_name = 'today.xls'
    today_data = pd.read_excel(today_file_name)
    today_ratio = today_data[['turnoverratio', 'name', 'per', 'changepercent']]
    yesterday_ratio = yesterday_data[['name', 'turnoverratio']]
    sheet = pd.merge(yesterday_ratio, today_ratio, on=['name'])
    sheet['percent'] = (sheet['turnoverratio_y'] / sheet['turnoverratio_x']).round(2)
    new_sheet1 = sheet.sort_values(by='turnoverratio_y', ascending=False)
    new_sheet = new_sheet1.drop_duplicates(['name'])
    final = new_sheet.loc[(new_sheet['percent'] > 2) & (new_sheet['per'] < 40) & (new_sheet['per'] > 0) & (new_sheet['turnoverratio_y'] < 11) & (new_sheet['changepercent'] < 9) & (new_sheet['changepercent'] > 0) & (new_sheet['turnoverratio_x'] > 0.1)]
    fix_number = final.count()[0]
    print('满足条件的共有%s个' % fix_number)
    print(final)
    final.to_excel('buy.xls')


if __name__ == '__main__':
    try:
        if os.path.exists('today.xls'):
            print('文件已存在')
            pass
        else:
            get_today_data()
        read_xls()
    except Exception as e:
        print(e)

