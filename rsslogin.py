# coding: utf8



import requests
from bs4 import BeautifulSoup
import json
import re;

homeurl = 'http://kindle4rss.com'
loginurl = 'http://kindle4rss.com/login/'
sendUnreadUrl = 'http://kindle4rss.com/send_now/'

session = requests.Session()


def init():
    """
    initialization
    :return:
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Host": 'kindle4rss.com',
        'Referer': 'http://kindle4rss.com/',
        "Upgrade-Insecure-Requests": "1"
    }
    payload = {
        'email_address':  input('请输入账号'),
        'password':   input('请输入密码')
        'persistent': True
    }
    session.headers = headers
    get = session.get(loginurl)
    print(get)
    response = session.post(url=loginurl, headers=headers, data=payload)
    print("服务器端返回状态码：", response.status_code)

def sendUnread():
    """
    send unread news
    :return:
    """
    sendRss = session.post(url=sendUnreadUrl)
    print('Send success status:', sendRss.status_code)


def sendOneSubscription(subscriptionId):
    """
    send one specific channel to kindle
    :param subscriptionId: subscripted channel id
    :return:
    """
    subscriptionUrl = 'http://kindle4rss.com/subscriptions/{}/'.format(subscriptionId)
    sendUrl = 'http://kindle4rss.com/feed/send/'
    get = session.get(subscriptionUrl)
    post = session.post(sendUrl, data={'subscription_id': subscriptionId})
    print('sendOneSubscription status code:',post.status_code)



def getAllSubscriptionId(homepage):
    subscriptionList = re.findall('/subscriptions/\d*/', homepage.content.decode('utf8'))
    list_ = [s[15:21] for s in subscriptionList]




init()
# print(response.text)
homepage = session.get(homeurl)
getAllSubscriptionId(homepage)
print('主页状态:',homepage.status_code)
sendUnread()
# sendOneSubscription('980576')

