import requests
import re
from contextlib import closing
from urllib.request import urlretrieve


from bs4 import BeautifulSoup
if __name__ == "__main__":
    url = 'https://www.dmzj.com/info/yaoshenji.html'
    req = requests.get(url = url)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html,'lxml')
    links = bf.find('ul','list_con_li autoHeight').find_all('a')
    chapter_name = []
    chapter_url = []
    for link in links:
        href = link.get('href')
        name = link.string
        chapter_name.insert(0,name)
        chapter_url.insert(0,href)
    # 访问 第一章节：
    url2 = 'https://www.dmzj.com/view/yaoshenji/41917.html'
    r = requests.get(url=url2)
    html = BeautifulSoup(r.text, 'lxml')
    script_info = html.script
    # print(r.text)
    # print('\n\n\n\n')
    # print(html)
    # print(script_info)
    pics = re.findall('\d{13,14}', str(script_info))#拿到图片的resouce
    for inx,pic in enumerate(pics):
        if len(pic) == 13:
            pics[inx] = pic + '0'
    pics = sorted(pics,key=lambda x:int(x)) #
    chapterpic_hou = re.findall('\|\|(\d{5})', str(script_info))[0]
    chapterpic_qian = re.findall('\|jpg\|(\d{4})', str(script_info))[0]
    for pic in pics:
        if pic[-1] == '0':
            url = 'https://images.dmzj.com/img/chapterpic/' + chapterpic_qian + '/' + chapterpic_hou + '/' + pic[:-1] + '.jpg'
        else:
            url = 'https://images.dmzj.com/img/chapterpic/' + chapterpic_qian + '/' + chapterpic_hou + '/' + pic + '.jpg'
        # print(url)
    download_header = {
    'Referer': 'https://www.dmzj.com/view/yaoshenji/41917.html'}
    dn_url = 'https://images.dmzj.com/img/chapterpic/3059/14237/14395217739069.jpg'
    #urlretrieve(dn_url,'1.jpg')
    ### 下载：
    with closing(requests.get(dn_url, headers=download_header, stream=True)) as response:
        chunk_size = 1024  
        content_size = int(response.headers['content-length'])  
        if response.status_code == 200:
            print('文件大小:%0.2f KB' % (content_size / chunk_size))
            with open('1.jpg', "wb") as file:  
                for data in response.iter_content(chunk_size=chunk_size):  
                    file.write(data)  
        else:
            print('链接异常')
    print('下载完成！')

    # 只差把所有的章节下面的所有图片下载下来了
    