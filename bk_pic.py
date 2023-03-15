"""1^365
   1.1^365"""
import requests
from lxml import etree
url = 'https://cd.zu.ke.com/zufang'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Cookie': 'select_city=510100; lianjia_uuid=db980944-7c31-4bcc-8aae-78cdd9ba138d; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22181a93da768e3e-047b67455463da-26021a51-1327104-181a93da769efd%22%2C%22%24device_id%22%3A%22181a93da768e3e-047b67455463da-26021a51-1327104-181a93da769efd%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E8%B4%9D%E5%A3%B3%E6%89%BE%E6%88%BF%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wychengdu%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; GUARANTEE_BANNER_SHOW=true; login_ucid=2000000245569411; lianjia_ssid=712b2a49-fc10-4962-8fea-379234735b80; lianjia_token=2.0013a6ea83788090ec020bc3b2663bffe3; lianjia_token_secure=2.0013a6ea83788090ec020bc3b2663bffe3; security_ticket=R2sd09nxk8Sm81pfJkvABUssf/StkYIdArkOZN0QqdFQvHLLFF7LBqExRYZbcQYf29gNoQKxH9O7MpAHGu2v73TQnJFksR9KIw/NJ+itit98LyB2Ncs/DgCZmgm3w0ypGjqFK49ik+KFpzJtvr4ukZOE94RSX5+eLymj/Vb+D18=; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYTRkYjMxYmRhYTM3YTU1ZWI3NDg5OGFiNTVhNTk3ZGQxY2ZhMDkyNTg2YWYwM2NiZDlhMWMwNzM3YmQ2ZmI1ZmZiODA4YmQ4ZTVkMWU4NDNjMjU2M2FhMGZhMzlkM2U4MjkzYTE4Y2U4NjVkNGU3Nzc5NTM5ZmFkNzlmMTE3ZGVkZmFlZDdkNmQxNjc4ZTA0ZDhiOTNiNzhhMDEyM2Q1Y2M0N2QzMDRlYjhkYjliOGM4MGQ2ZTdiMjc0N2UxMzViNjRkYjcwNjA5ZmVkMmIyMjhjMzc2NDQyN2E5YTkzNTY0MjkwYjU2NGE1OGZmYjcxNjMzZDAwZjMxNDBkY2YwNlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJjODFiYmNhYVwifSIsInIiOiJodHRwczovL2NkLnp1LmtlLmNvbS96dWZhbmciLCJvcyI6IndlYiIsInYiOiIwLjEifQ=='}
resp = requests.get(url=url, headers=headers)
# print(resp.text)
# xpath解析
parser = etree.HTMLParser(encoding='utf-8')
# 转换树对象
tree = etree.XML(resp.text, parser=parser)
'''for i in range(1,int(input('输入需求图片数'))+1):
    img = tree.xpath(f'//*[@id="content"]/div[1]/div[1]/div[{i}]/a/img/@data-src')[0]
    print(img)
    img_data = requests.get(img)
    img_pic = img_data.content
    f = open(f'house{i}.jpg','wb')
    f.write(img_pic)
    f.close()'''
'''all_list = tree.xpath('//*[@id="content"]/div[1]/div[1]/text()')
for all in range(1,len(all_list)):
    img = tree.xpath(f'//*[@id="content"]/div[1]/div[1]/div[{all}]/a/img/@data-src')[0]
    #print(img)
    img_data = requests.get(img)
    img_pic = img_data.content
    f = open(f'house{all}.jpg','wb')
    f.write(img_pic)
    f.close()'''
img_list = tree.xpath('//*[@id="content"]/div[1]/div[1]/div/a/img/@data-src')
count = 0
for img in img_list:
    count += 1
    img_data = requests.get(img)
    img_pic = img_data.content
    f = open(f'house{count}.jpg','wb')
    f.write(img_pic)
    f.close()