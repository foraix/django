import requests
from lxml import etree
import pymysql


def get_html():
    url = 'https://search.51job.com/list/090300%252C090200,000000,0000,00,9,99,Python%2B%25E5%25BC%2580%25E5%258F%2591,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    body = requests.get(url)
    body.encoding = 'gbk'
    html = body.text
    return html


# 获取title标签中的值
def get_body():
    body = get_html()
    html = etree.HTML(body)
    print(html)


def get_company_name():
    body = get_html()
    html = etree.HTML(body)
    a_text = html.xpath('//span[@class="t2"]/a/@title')
    del a_text[0]
    return a_text


def get_money():
    body = get_html()
    html = etree.HTML(body)
    a_text = html.xpath('//span[@class="t4"]/text()')
    del a_text[0]
    del a_text[0]
    return a_text


def get_location():
    body = get_html()
    html = etree.HTML(body)
    a_text = html.xpath('//span[@class="t3"]/text()')
    del a_text[0]
    del a_text[0]
    return a_text


def get_job_name():
    body = get_html()
    html = etree.HTML(body)
    a_text = html.xpath('//div[@class="el"]/p/span/a/@title')
    return a_text


# 新增
def insert(tup):
    # 创建数据库连接
    db = pymysql.connect("localhost", "root", "test", "testpy")

    # 获取游标对象
    cur = db.cursor()
    sql = "INSERT INTO company (name, job, salary, location) " \
          "VALUES (%s,%s,%s,%s)"
    cur.executemany(sql, tup)
    # 获取响应行数
    num = cur.rowcount
    # 提交
    db.commit()
    if num > 0:
        print("insert success")
    else:
        print("insert error")


context = list(zip(get_company_name(), get_job_name(), get_money(), get_location()))

# c = []
# for i in range(len(context)):
#     c.append((context[i])[1])
# print(c)
c = get_job_name()
dict = {}
for key in c:
    dict[key] = dict.get(key, 0) + 1
# insert(context)
lst_keys, lst_values = dict.keys(), dict.values()


def get_keys():
    return list(dict.keys())


def get_values():
    return list(dict.values())
