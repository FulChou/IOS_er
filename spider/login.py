
import requests
from bs4 import BeautifulSoup
import re 
import json
import os



userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'



Cookie = 'JSESSIONID=AC3553C42B2CD42F8BFC6AE41C8252F5'

session = requests.session() # 使用session对象
# 获取登录的 token：
def get_login_id():
    url = 'http://ca.its.csu.edu.cn/Home/Login/69'
    post_data = {
    'userName': '0304170106',
    'passWord': '312578',
    'enter': 'true'
    }
    headers = {
        "Referer": "http://ca.its.csu.edu.cn/Home/Login/69",
        'User-Agent': userAgent,
    }
    req = requests.post(url,post_data,headers)
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
    "account": "0304170106",
    "Thirdsys": "xsgzx"
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

##进入填报界面： 可以在这里选择填哪一个同学：获取填报信息：
def get_stu_information():
    if os.path.exists('stu_data.json'): # exists information
        with open('stu_data.json','r') as fl:
            data_list = json.loads(fl.read())
            print('1111',data_list)
        return data_list
    req = session.get('http://202.197.71.125/a/physicalhealth/gxxl07/gXXL0704/form?type=add')
    # print(req.text)
    ## 拿出同学的数据：
    bstext = BeautifulSoup(req.text,'lxml')
    taglist = bstext.find_all('td',id=True)
    data_list = []
    params_data = {
    'gxxl0703Id': '',
    'gxxl0705Id': '',
    'type': 'edit'
    }
    # get_data = {
    # 'gxxl0703Id': '553c2189e7e845af9e636d287e7ee00c',
    # 'gxxl0705Id': '97a061b4758c48b2ba0b43f59ea1fb9d',
    # 'type': 'edit'
    # }

    for td in taglist: ## 还差一个联系方式：get from jquery
        td_name = td.find_next_sibling('td')
        td_address = td_name.find_next_sibling('td')
        stu_name = td_name.string
        stu_address = td_address.string
        stu_id = td.string
        # 找link id：
        tds = td.find_parent('tr').find('a')
        id_string = tds.get('onclick') #得到包含id 的字符串，解析得到两个id
        # print(id_string)
        url_id_list = re.findall(r"'\w{32}'|''",id_string) # 这个正则会包含’ ‘ 号
        data = {    
        'xsid': stu_id,
        'xh': stu_id,
        'xm': stu_name,
        'qs': stu_address,
        'lxfs': '13690098765',
        'xyqk': 'A',
        'qgzk': 'A',
        'rjgx': 'A',
        'shqk': 'A',
        'xldj': '1级',
        'zjywtfsj': '无',
        'tj': '1' ,
        'gxxl0703Id':url_id_list[0].strip("'"), #根本不需要煞费苦心去读取re id
        'gxxl0705Id':url_id_list[1].strip("'")
        }
        params_data['gxxl0703Id'] = data['gxxl0703Id']
        params_data['gxxl0705Id'] = data['gxxl0705Id']

        phone_num = get_phone_num(params_data)
        data['lxfs'] = phone_num
        # print(params_data['gxxl0703Id'],params_data['gxxl0705Id'],'http://202.197.71.125/a/physicalhealth/gxxl07/gXXL0705/toAddDetail?\
        # gxxl0703Id='+params_data['gxxl0703Id']+'&\
        # gxxl0705Id='+params_data['gxxl0705Id']+'&\
        # type=edit',params_data)
        data_list.append(data)
        # print(url_id_list)
        # print(tds)
    # print(data_list)
    json_data = json.dumps(data_list)
    with open('stu_data.json','w') as fl:
        fl.write(json_data)
    return data_list

def get_phone_num(params_data):
    # print(params_data)
    sub_req = session.get('http://202.197.71.125/a/physicalhealth/gxxl07/gXXL0705/toAddDetail?\
    gxxl0703Id='+params_data['gxxl0703Id']+'&\
    gxxl0705Id='+params_data['gxxl0705Id']+'&\
    type=edit',params=params_data)

    # print('11111111',sub_req.text)
    ### 解析：
    bf = BeautifulSoup(sub_req.text,'lxml')
    phone_num = bf.find('input',attrs={'name':'lxfs'}).get('value')
    return phone_num

def upload_data(data_list=None):

    req = session.post('http://202.197.71.125/a/physicalhealth/gxxl07/gXXL0704/saveMain',
    data=data_list[0]) # 找到捷径，根本不需要网页的跳转id
    print(req.status_code)

    # for data in data_list:
    #     del data[]

    # input_headers = {
    # 'Referer': 'http://202.197.71.125/a/physicalhealth/gxxl07/gXXL0705/toAddDetail?\
    #     gxxl0703Id=553c2189e7e845af9e636d287e7ee00c&\
    #     gxxl0705Id=97a061b4758c48b2ba0b43f59ea1fb9d&\
    #     type=edit',
    # 'User-Agent': userAgent,
    # 'Cookie': 'JSESSIONID=9955E69E6DBD8F4BBBDA4AFE202A75E9',
    # 'X-Requested-With': 'XMLHttpRequest'
    # }
    # input_res = requests.post('http://202.197.71.125/a/physicalhealth/gxxl07/gXXL0704/saveMain',data=input_data,headers=input_headers)
    # print(input_res.status_code)
    print("done")





if __name__ == "__main__":
    tokenId = get_login_id()
    login(tokenId)

    # upload_data(data_list)

    # header = {
    # 'Referer': 'http://202.197.71.125/a/physicalhealth/gxxl06/gXXLIndex/orderList',
    # 'User-Agent': userAgent,
    # 'Cookie': 'JSESSIONID=9955E69E6DBD8F4BBBDA4AFE202A75E9'
    # }
    # 获得填报的列表界面 选择哪一个填报的界面
    #res1 = se.get('http://202.197.71.125/a/physicalhealth/gxxl07/gXXL0704/list',headers=header)

    # res1 = session.get('http://202.197.71.125/a/physicalhealth/gxxl07/gXXL0704/list')
    # pyb_list = BeautifulSoup(res1.text,'lxml')
    # print(pyb_list)

    

    # header2 = {
    # 'Referer': 'http://202.197.71.125/a/physicalhealth/gxxl07/gXXL0704/list',
    # 'User-Agent': userAgent,
    # 'Cookie': Cookie
    # }
    # res2 = requests.get('http://202.197.71.125/a/physicalhealth/gxxl07/gXXL0704/form?type=add',headers = header2)
    # print(res2.text)


    # ## 进入选项界面： 进去了。可以看到手动的选项了，但是没必要了，直接模拟发送请求就行
    # header3 = {
    # 'Referer': 'http://202.197.71.125/a/physicalhealth/gxxl07/gXXL0704/form?\
    #     gxxl0704Id=6a80eb366ce94a85befed91bacdce315&type=edit',
    # 'User-Agent': userAgent,
    # 'Cookie': 'JSESSIONID=08D2D33B7F6B6E77C342BD25195F8A93'
    # }

    # get_data = {
    # 'gxxl0703Id': '553c2189e7e845af9e636d287e7ee00c',
    # 'gxxl0705Id': '97a061b4758c48b2ba0b43f59ea1fb9d',
    # 'type': 'edit'
    # }
    # res3 = session.get('http://202.197.71.125/a/physicalhealth/gxxl07/gXXL0705/toAddDetail?\
    #     gxxl0703Id='+get_data['gxxl0703Id']+'&\
    #     gxxl0705Id='+get_data['gxxl0705Id']+'&\
    #     type=edit',params=get_data)
    # print(res3.text) # 拿到了这个界面，但是cooike 要是对的：

    data_list = get_stu_information()

    
    
'''
<form name="myForm" method="post" action="http://202.197.71.125/loginsso.jsp" runat="Server"  >
<input name="tokenId" type="hidden" value="eb9d795813044fda876411ec0e7d207f" runat="Server">
<input name="account" type="hidden" value="0304170106" runat="Server">
<input name="Thirdsys" type="hidden" value="xsgzxt" runat="Server">


gxxl0703Id: cd64af5c26eb4929ab06870978aeb32c
gxxl0705Id: 
type: add

'''