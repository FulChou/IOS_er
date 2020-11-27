import requests
from bs4 import BeautifulSoup
import re 
import json
import os
import copy
from random import choice
username = 'xx'
password = 'xx'

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
session = requests.session() # 使用session对象
# 获取登录的 token：
def get_login_id():
    url = 'http://ca.its.csu.edu.cn/Home/Login/69'
    post_data = {
    'userName': username,
    'passWord': password,
    'enter': 'true'
    }
    headers = {
        "Referer": "http://ca.its.csu.edu.cn/Home/Login/69",
        'User-Agent': userAgent,
    }
    req = session.post(url,post_data,headers)
    html = req.text
    bf = BeautifulSoup(html,'lxml')
    tokenId_input_list = bf.find_all('input',attrs={'name':'tokenId'}) # name 是函数签名，所以不能用name = "tokenId"
    tokenId = tokenId_input_list[0].get('value')
    print(tokenId)
    return tokenId

##登录到用户的界面：
def login(tokenId) ->str:
    p_data = {
    "tokenId": tokenId,
    "account": username,
    "Thirdsys": "xsgzx" # xsgzxt
    }
    new_headers = {
        'Referer': 'http://ca.its.csu.edu.cn/',
        'User-Agent': userAgent
    }
    # print(req.cookies)
    # print('1111')
    # temcookie = requests.utils.dict_from_cookiejar(req.cookies)
    # print(type(req.cookies))
    # print(requests.utils.dict_from_cookiejar(req.cookies)) # 成功登录到 用户界面： nice！！
    req = session.post('http://202.197.71.125/loginsso.jsp',p_data,new_headers) # 改用session会话
    # print(req.text)
    # print(req.cookies) # cookies 里面没有真的东西。。。 只有一个sessionID，后端不发过来（只存在前端浏览器中）

level = ['A', 'B'] # 评价登记
##进入填报界面： 可以在这里选择填哪一个同学：获取填报信息：
def get_stu_information():
    # if os.path.exists('stu_data.json'): # exists information
    #     with open('stu_data.json','r') as fl:
    #         data_list = json.loads(fl.read())
    #     return data_list
    
    req = session.get('http://202.197.71.125/a/physicalhealth/gxxl07/gXXL0704/form?type=add')
    ## 拿出同学的数据：
    bstext = BeautifulSoup(req.text,'lxml')
    taglist = bstext.find_all('td',id=True)
    data_list = []
    params_data = {
    'gxxl0703Id': '',
    'gxxl0705Id': '',
    'type': 'edit'
    }
    for td in taglist: 
        td_name = td.find_next_sibling('td')
        td_address = td_name.find_next_sibling('td')
        stu_name = td_name.string
        stu_address = td_address.string
        stu_id = td.string
        # 找link id：
        tds = td.find_parent('tr').find('a')
        id_string = tds.get('onclick') #得到包含id 的字符串，解析得到两个id
        url_id_list = re.findall(r"'\w{32}'|''",id_string) # 这个正则会包含’ ‘ 号
        # data参数模板
        data = {    
        'xsid': '',
        'xh': '',
        'xm': 'stu_name',
        'qs': 'stu_address',
        'lxfs': '13690098765',
        'xyqk': choice(level),
        'qgzk': choice(level),
        'rjgx': choice(level),
        'shqk': choice(level),
        'xldj': '1级',
        'zjywtfsj': '无',
        'tj': '1' ,
        'gxxl0703Id':'', 
        'gxxl0705Id':''
        }
        data['xsid'] = stu_id
        data['xh'] = stu_id
        data['xm'] = stu_name
        data['qs'] = stu_address
        data['gxxl0703Id'] = url_id_list[0].strip("'")  
        data['gxxl0705Id'] = url_id_list[1].strip("'")       
        params_data['gxxl0703Id'] = data['gxxl0703Id']
        params_data['gxxl0705Id'] = data['gxxl0705Id']
        phone_num = get_phone_num(params_data)
        data['lxfs'] = phone_num
        data_list.append(data)
    json_data = json.dumps(data_list)
    with open('stu_data.json','w') as fl:
        fl.write(json_data)
    print('succecc for data')
    return data_list

def get_phone_num(params_data):
    sub_req = session.get('http://202.197.71.125/a/physicalhealth/gxxl07/gXXL0705/toAddDetail?\
    gxxl0703Id='+params_data['gxxl0703Id']+'&\
    gxxl0705Id='+params_data['gxxl0705Id']+'&\
    type=edit',params=params_data)
    ### 解析：
    bf = BeautifulSoup(sub_req.text,'lxml')
    phone_num = bf.find('input',attrs={'name':'lxfs'}).get('value')
    return phone_num

def upload_data(data_list=None,flag=True):
    if flag:
        for data in data_list:
            req = session.post('http://202.197.71.125/a/physicalhealth/gxxl07/gXXL0704/saveMain',
            data=data) 
        print(req.status_code)
        print("Well-done")



if __name__ == "__main__":
    tokenId = get_login_id()
    login(tokenId)
    data_list = get_stu_information()
    upload_data(data_list)