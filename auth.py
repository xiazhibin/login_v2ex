#coding=utf-8

import requests, cookielib
try:
    from bs4 import BeautifulSoup
except:
    import BeautifulSoup

session = requests.session()
requests.cookies = cookielib.LWPCookieJar('cookies')

try:
    requests.cookies.load(ignore_discard=True)
except:
    pass

url = 'https://www.v2ex.com/signin'
get_headers = {
        'authority': "www.v2ex.com",
        'method': "GET",
        'path': '/signin',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': "http://www.zhihu.com/",
        'content-type': "application/x-www-form-urlencoded",
        'origin': 'https://www.v2ex.com',
        'referer': 'https://www.v2ex.com/signin',
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
    }
r = requests.get(url, headers=get_headers, verify=False)
soup = BeautifulSoup(r.content, "html.parser")
once = soup.find('input', attrs={'name': "once"}).attrs.get('value')
print once
user_name = soup.find('input', attrs={'placeholder': u'用户名或电子邮箱地址'}).attrs.get('name')
print user_name
pwd_name = soup.find('input', attrs={'type': 'password'}).attrs.get('name')
print pwd_name

post__headers = {
        'authority': "www.v2ex.com",
        'method': "POST",
        'path': '/signin',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': "http://www.zhihu.com/",
        'content-type': "application/x-www-form-urlencoded",
        'origin': 'https://www.v2ex.com',
        'referer': 'https://www.v2ex.com/signin',
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
    }

user_name_value = 'bin381'
pwd_value = 'bin123456'
form = dict()
form['once'] = once
form[user_name] = user_name_value
form[pwd_name] = pwd_value
form['next'] = '/'

print form

r = requests.post(url, data=form, headers=post__headers, verify=False)
print r.content
requests.cookies.save()
