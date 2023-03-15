"""1^365
   1.1^365"""
import requests
from lxml import etree
import csv
import xlwt
#url = 'https://cd.zu.ke.com/zufang'
city = str('绵阳')#['cd','sh','san','mianyang']
citys = {'成都':'cd','上海':'sh','绵阳':'mianyang'}
in_page = int(1)#range(1,3)
pages = range(1,in_page+1)
print(city)
list_box = []
#for city in citys:
for page in pages:
    url = f'https://{citys[city]}.zu.ke.com/zufang/pg{page}/#contentList'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
               'Cookie': 'select_city=510100; lianjia_uuid=db980944-7c31-4bcc-8aae-78cdd9ba138d; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22181a93da768e3e-047b67455463da-26021a51-1327104-181a93da769efd%22%2C%22%24device_id%22%3A%22181a93da768e3e-047b67455463da-26021a51-1327104-181a93da769efd%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E8%B4%9D%E5%A3%B3%E6%89%BE%E6%88%BF%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wychengdu%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; GUARANTEE_BANNER_SHOW=true; login_ucid=2000000245569411; lianjia_ssid=712b2a49-fc10-4962-8fea-379234735b80; lianjia_token=2.0013a6ea83788090ec020bc3b2663bffe3; lianjia_token_secure=2.0013a6ea83788090ec020bc3b2663bffe3; security_ticket=R2sd09nxk8Sm81pfJkvABUssf/StkYIdArkOZN0QqdFQvHLLFF7LBqExRYZbcQYf29gNoQKxH9O7MpAHGu2v73TQnJFksR9KIw/NJ+itit98LyB2Ncs/DgCZmgm3w0ypGjqFK49ik+KFpzJtvr4ukZOE94RSX5+eLymj/Vb+D18=; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYTRkYjMxYmRhYTM3YTU1ZWI3NDg5OGFiNTVhNTk3ZGQxY2ZhMDkyNTg2YWYwM2NiZDlhMWMwNzM3YmQ2ZmI1ZmZiODA4YmQ4ZTVkMWU4NDNjMjU2M2FhMGZhMzlkM2U4MjkzYTE4Y2U4NjVkNGU3Nzc5NTM5ZmFkNzlmMTE3ZGVkZmFlZDdkNmQxNjc4ZTA0ZDhiOTNiNzhhMDEyM2Q1Y2M0N2QzMDRlYjhkYjliOGM4MGQ2ZTdiMjc0N2UxMzViNjRkYjcwNjA5ZmVkMmIyMjhjMzc2NDQyN2E5YTkzNTY0MjkwYjU2NGE1OGZmYjcxNjMzZDAwZjMxNDBkY2YwNlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJjODFiYmNhYVwifSIsInIiOiJodHRwczovL2NkLnp1LmtlLmNvbS96dWZhbmciLCJvcyI6IndlYiIsInYiOiIwLjEifQ=='}
    resp = requests.get(url=url,headers=headers)
    #print(resp.text)
    #xpath解析
    parser = etree.HTMLParser(encoding='utf-8')
    #转换树对象
    tree = etree.XML(resp.text,parser=parser)
    #print(tree)
    # price = tree.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div/span/em/text()')
    price = tree.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div/span/em/text()')
    #print(price)
    addres = tree.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div/p[2]/a[1]/text()')
    #print(addres)
    access = tree.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div/p[2]/a[2]/text()')
    #print(access)
    area = tree.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div/p[2]/a[3]/text()')
    #print(area)
    #拿到一整列的房源标题
    titles = tree.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[1]/a/text()')
    #print(titles)
    prices = tree.xpath('//*[@id="content"]/div[1]/div[1]/div/div/span/em/text()\n')
    #print(prices)
    #获取你需要的信息的所有板块
    all_list = tree.xpath('//*[@id="content"]/div[1]/div[1]/div')
    #print(all)
    #遍历子板块信息

    # for all in all_list:
    #     title = all.xpath('./div/p[1]/a/text()')
    #     price = all.xpath('./div/span/em/text()')
    #     path = all.xpath('./div/p[2]/a[1]/text()')
    #     sub =  all.xpath('./div/p[2]/a[2]/text()')
    #     home = all.xpath('./div/p[2]/a[3]/text()')
    #     all_1 = all.xpath('./div/p[2]/text()')
    #     all_1.pop(0)
    #     all_1.pop(0)
    #     all_1.pop(0)
    #     all_1.pop(0)
    #     if '\n        ' in all_1 :
    #         all_1.pop(0)
    #         all_1.remove('\n      ')
    #     else:
    #         x=1
    #     # if "精选" in all_1:
    #     #     all_1.pop[0]
    #     # else:
    #     #     x=1
    #     list_box.append([title,price,path,sub,home,all_1])

    for all in all_list:
        title = all.xpath('./div/p[1]/a/text()')
        price = all.xpath('./div/span/em/text()')
        path = all.xpath('./div/p[2]/a[1]/text()')
        sub =  all.xpath('./div/p[2]/a[2]/text()')
        home = all.xpath('./div/p[2]/a[3]/text()')
        jx = all.xpath('./div/p[2]/text()[1]')[0]
        if '精选' in jx:
            area = all.xpath('./div/p[2]/text()[6]')
            toward = all.xpath('./div/p[2]/text()[7]')
            house_type = all.xpath('./div/p[2]/text()[8]')
        else:
            area = all.xpath('./div/p[2]/text()[5]')
            toward = all.xpath('./div/p[2]/text()[6]')
            house_type = all.xpath('./div/p[2]/text()[7]')
        list_box.append([title, price, path, sub, home,area,toward,house_type])


    for i in list_box:
        i[0][0] = i[0][0].strip()
        i[1][0] = i[1][0].strip()
        i[2][0] = i[2][0].strip()
        # if i[3][0] is None:
        #     i[3][0] = i[3][0]
        # else:
        #     i[3][0] = i[3][0].strip()
        i[4][0] = i[4][0].strip()
        i[5][0] = i[5][0].strip()
        i[6][0] = i[6][0].strip()
        i[7][0] = i[7][0].strip()

    for i in list_box:
        print(i)
#设置页 加到表头
'''pages = range(1,3)
for page in pages:
    url = f'https://cd.zu.ke.com/zufang/pg{page}/#contentList'''
#存数字方式之一
#存到csv文件，逗号分隔符文件
# writer = csv.writer(open('data1.csv','w',encoding='utf-8'))#打开，未创建文件
# writer.writerow(['title', 'price', 'path', 'sub', 'home','area','toward','house_type'])
# writer.writerows(list_box)
# 存储数据方式二
# 写入excel文件
wb = xlwt.Workbook()#建立工作布
sheet = wb.add_sheet(('data'))#建立表
titles = ('title', 'price', 'path', 'sub', 'home','area','toward','house_type')
for index,title in enumerate(titles):# enumerate 输出两个维度的数据 1、数据系列的索引值，2、数据本身
    sheet.write(0,index,title)# 参数-：行索引 参数二：列索引 参数三：数据本身
for i , item in enumerate(list_box):# i:行索引 item：一行数据
    for j ,data in enumerate(item):# j：列索引 data：一个数据
        sheet.write(i+1,j,data)
wb.save('house.xls')