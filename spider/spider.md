# 爬虫
什么是url：


## 访问url

## 解析url

beautifulsoup4

lxml


## 保存信息


### 爬取图片：

审查元素找图片地址，你会发现，这个页面不能右键！
- F12
- view-source:https://www.dmzj.com/view/yaoshenji/41917.html
- 更简单的办法是，将鼠标焦点放在浏览器地址栏，然后按下F12依然可以调出调试窗口。

遇到动态加载不要慌，使用JavaScript动态加载，无外乎两种方式：

- 外部加载
- 内部加载

外部加载就是在html页面中，以引用的形式，加载一个js，例如这样：
`<script type="text/javascript" src="https://cuijiahua.com/call.js"></script>`

内部加载就是Javascript脚本内容写在html内(在html内部写的JavaScript)

图像资源：在浏览器中打开，可能直接无法打开，或者能打开，但是一刷新就又不能打开了！

记住，这就是一种典型的通过Referer的反扒爬虫手段！
- Referer可以理解为来路，先打开章节URL链接，再打开图片链接。打开图片的时候，Referer的信息里保存的是章节URL。

