No 'Access-Control-Allow-Origin' header is present on the requested resource

### 在使用浏览器xmlHttpRequest去访问自己flask搭建的网站后端的时候，出现报错：

经过一番查找知道是资源跨域访问问题，以前使用java spring 自动帮忙解决了这个问题，都有些忘记有这个事情要做了。

flask 解决资源跨域的方法很简单：
但是更加重要的是其中蕴含了什么原理，这样不管是别人问我们，还是去面试。我们都能够比较清楚的答出来：


### 浏览器的 same origin policy：
如果网站访问的api的网站和自己不同源，浏览器一样会帮你发送request，但是会去检测response 的头部，如果api网站后端返回的respnse 的头部信息，没有允许跨域访问，那么你就不能够得到返回的信息

- 不同源的标准：
- 	domain 域名不一样
- http还是https
- 端口号不一样


### Cross-Origin Resource Sharing，
跨來源資源共享。是指当浏览器收到 异步访问的Response 之後，返回的头部信息里面Access-Control-Allow-Origin裡面的內容，如果裡面有包含現在這個發起 Request 的 Origin 的話，就會允許通過，请求者順利接收到 Response。

### python-flask的解决办法：
#### 使用flask_cors包
安装
`pip install flask_cors`
初始化的时候加载配置，这样就可以支持跨域访问了
```python
from flask_cors import CORS`

app = Flask(__name__)
CORS(app, supports_credentials=True)

if __name__ == "__main__":
    app.run()
```
对请求的Response header中加入header
```python
@app.after_request
def af_request(resp):     
    """
    #请求钩子，在所有的请求发生后执行，加入headers。
    :param resp:
    :return:
    """
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp
```

![加载图片](https://gitee.com/csu_vincent/images/raw/master/20200518222705.bmp)