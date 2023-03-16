# Bk-source-acquisition
贝壳房源爬取
1.需求分析
打开贝壳租房首页：(https://cd.zu.ke.com/zufang)

我们将要提取的信息有房名，价格、区域、地址、面积、朝向、房型。

# Xpath分析
整个程序的核心在与Xpath分析。进入检查页面，我们发现所有信息都在ul标签下的div下，我们可以通过复制xpath路径来获取代码路径。
有了路径在python中分析就容易多了

1）房名

//*[@id="content"]/div[1]/div[1]/div/div/p[1]/a/text()

2）价格

//*[@id="content"]/div[1]/div[1]/div/div/span/em/text()

3）区域

//*[@id="content"]/div[1]/div[1]/div[1]/div/p[3]/a[1]/text()

4）地址

//*[@id="content"]/div[1]/div[1]/div[1]/div/p[2]/a[1]/text()

5）面积

//*[@id="content"]/div[1]/div[1]/div[3]/div/p[2]//text()[5]
Xpath的使用方式
1) 导入模块

如果你下载的是4.5或4.5以上的版本，导入模块方式为：from lxml import html

否则为：from lxml import etree

2）构建Xpath

首先我们要获取一个html的响应文件，我使用的requests模块拿到的
解析Xpath
转换树对象

3）
获取匹配内容
