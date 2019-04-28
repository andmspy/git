from selenium import webdriver
import time
from bs4 import BeautifulSoup
import random

def data_filter():
    tag_list = {}
    url_head = 'http://summary.jrj.com.cn'
    with open('page_source.txt', 'r+') as f:
        data = f.read()
        soup = BeautifulSoup(data, 'lxml')
        a_tag = soup.find_all('a')
        for i in a_tag[1:-2]:
            tag_list[i.text] = url_head + i['href']
    return tag_list


def get_page_source():
    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver.minimize_window()
    # driver.get(url)
    # wb_data = driver.page_source
    total_list = []
    for key, values in data_filter().items():
        concept_list = [key]
        init_list = []
        driver.get(values)
        wb_data = driver.page_source
        soup = BeautifulSoup(wb_data, 'lxml')
        # tbody = soup.find_all('tbody')
        pagebar = soup.find('p', id='pagebar').find_all('a')
        page = pagebar[-2].get_text()
        concept_number = values[-15:-6]
        for i in range(1, int(page)+1):
            url_back = '?q=cn|s|bk{}&c=m&n=hqa&o=pl,d&p={}020'.format(concept_number, i)
            driver.get(values+url_back)
            sleep_time = random.randint(3, 20)
            time.sleep(sleep_time)
            print('已停留%s秒后开始正在请求：%s' % (sleep_time, values+url_back))
            wb_data2 = driver.page_source
            soup2 = BeautifulSoup(wb_data2, 'lxml')
            tbody2 = soup2.find_all('tbody')
            a = tbody2[2].find_all('a')
            for j in range(1, len(a), 4):
                init_list.append(a[j].text)
            concept_list.append(init_list)
        init_list = []
        print(concept_list)
        total_list.append(concept_list)
        concept_list = []
        with open('concept.txt', 'a+', encoding='utf-8') as f:
            f.write(str(concept_list))
            f.write('\n')
get_page_source()

