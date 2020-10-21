# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup
"""
发起请求，解析数据，保存数据
"""

def get_content(target):
    req = requests.get(url = target)
    req.encoding = 'gb2312'
    html = req.text 
    bs = BeautifulSoup(html,'lxml')
    texts = bs.find('div',id='contentbox')
    result = " "
    contents = texts.text.strip().split('\xa0'*4)
    print(contents)
    for content in contents:
        result = result + content+'\n'
    return result



if __name__ == '__main__':
    target = "https://www.uukanshu.com/b/102656/"
    server = 'https://www.uukanshu.com'
    book_name = '我真没想重生啊.txt'
    req = requests.get(url = target)
    req.encoding = 'gb2312'
    html = req.text
    bs = BeautifulSoup(html,'lxml')
    chapterList = bs.find('ul',id='chapterList')
    links = chapterList.find_all('a')
    index = 0
    for link in links:
        if index >=2: break #下载两章玩一玩：
        index += 1
        chapter_name = link.string
        url = server + link.get('href')
        content = get_content(url)
        with open(book_name,'a',encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n\n')
            f.write(content)
            f.write('\n')