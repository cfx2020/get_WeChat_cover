# coding:utf-8

from bs4 import BeautifulSoup
import requests
import re
import os

# 网页爬取

def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态码不是200会引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


# 网页解析

def parse_page(html):
    try:
        image = re.search(r'var msg_cdn_url \= \".*\"', html)
        img_url = eval(image.group(0).split('=', maxsplit=1)[1])
        title = re.search(r'var msg_title \= \'.*\'', html)
        name = eval(title.group(0).split('=', maxsplit=1)[1])
        return img_url, name
    except:
        print("解析失败")


# 图片爬取

def get_wx_msg(img_url, name):
    root = "C://Users//shinelon//Downloads//"
    path = root+name+".png"
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(img_url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")


def main():
    url = input("请输入公众号链接")
    html = get_html_text(url)
    img_url = parse_page(html)[0]
    name = parse_page(html)[1]
    get_wx_msg(img_url, name)


main()
