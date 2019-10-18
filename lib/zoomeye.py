import requests
import json
import os

class zoomeye:
    def __init__(self, keyword, from_page,end_page):
        self.username = ""
        self.password = ""
        self.access_token = ''
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0", "Content-Type":"application/json"}
        self.keyword = keyword
        self.from_page = int(from_page)
        self.end_page = int(end_page) + 1
        self.targets = []

    def get_access_token(self):
        login_url = "https://api.zoomeye.org/user/login"
        data = '{"username": "%s", "password": "%s"\
        }' % (self.username, self.password)
        r = requests.post(login_url,data=data)
        self.access_token = r.text[18:-2]
        return self.access_token

    def get_info(self):
        if not self.access_token:
            self.get_access_token()
        info_url = "https://api.zoomeye.org/resources-info"
        self.headers["Authorization"] = "JWT " + self.access_token
        r = requests.get(info_url, headers=self.headers)
        return r.text

    def run(self):
        if not self.access_token:
            self.get_access_token()
        for n in range(self.from_page, self.end_page):
            print ("page:",n)
            search_url = "https://api.zoomeye.org/host/search?query=%s&page=%s\
            " % (self.keyword, str(n))
            self.headers["Authorization"] = "JWT " + self.access_token
            r = requests.get(search_url, headers=self.headers)
            result = json.loads(r.text)
            for i in result['matches']:
                target = i['ip'] + ":" + str(i['portinfo']['port'])
                
                self.targets.append(target)
        return self.targets

    def run_web(self):
        if not self.access_token:
            self.get_access_token()
        for n in range(self.from_page, self.end_page):
            search_url = "https://api.zoomeye.org/web/search?query=%s&page=%s\
            " % (self.keyword, str(n))
            self.headers["Authorization"] = "JWT " + self.access_token
            r = requests.get(search_url, headers=self.headers)
            result = r.text
            result = json.loads(result)
            try:
                for i in result['matches']:
                    target = i["site"]
                    self.targets.append(target)
            except:
                pass
        return self.targets

