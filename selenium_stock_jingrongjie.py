from selenium import webdriver
import time
from bs4 import BeautifulSoup
import random
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def get_page_source(url):
    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver.minimize_window()
    driver.get(url)
    element = WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "summary")))
    wb_data = driver.page_source
    soup = BeautifulSoup(wb_data, 'lxml')
    summary = soup.find('div', class_='summary').find_all('p')[0].get_text()
    title = soup.find('title').get_text()
    driver.quit()
    print(title, summary)
    return [title, summary]


def get_code():
    excel = pd.read_excel(r'C:\Users\Administrator\Desktop\eCom\easyship_view\stock\history_data\2019\excel\t20190426.xls')
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
                code_list.append('sh' + str(i))
            else:
                print(i)
    return code_list


def main():
    j = 1
    for i in get_code():
        print(j)
        url = r'http://f10.eastmoney.com/f10_v2/CoreConception.aspx?code={}'.format(i)
        try:
            with open('concept.txt', 'a+', encoding='utf-8') as f:
                f.write(str(get_page_source(url)))
                f.write('\n')
                f.close()
            j += 1
            time.sleep(random.randint(2, 9))
        except Exception as e:
            print('出错的链接：')
            print(e, url)
            pass

main()



# http://f10.eastmoney.com/f10_v2/CoreConception.aspx?code=sh600368
