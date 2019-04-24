import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd


def get_code():
    excel = pd.read_excel(r'C:\Users\Andy\PycharmProjects\untitled6\easyship_view\history_data\2019\excel\t20190424.xls')
    code = excel['code'].tolist()
    code_list = []
    for i in code:
        if str(i).startswith('6') and len(str(i)) == 6:
            code_list.append('sh'+str(i))
        elif str(i).startswith('2') and len(str(i)) == 4:
            code_list.append('sh00'+str(i))
        elif str(i).startswith('300') and len(str(i)) == 6:
            code_list.append('sh' + str(i))
        else:
            if len(str(i)) == 3:
                code_list.append('sh000' + str(i))
            elif len(str(i)) == 2:
                code_list.append('sh0000' + str(i))
            elif len(str(i)) == 1:
                code_list.append('sh00000' + str(i))
            elif len(str(i)) == 4 and str(i).startswith('1'):
                code_list.append('sh00' + str(i))
            elif len(str(i)) == 6 and str(i).startswith('9'):
                code_list.append('sh00' + str(i))
            else:
                print(i)
    print(len(code_list))
    return code_list




get_code()


#3675个股数






