import shodan

class shodan_api:
    def __init__(self,query,start,end):
        self.API_KEY = "Your Key"
        self.query = query
        self.pagestart = start
        self.pageend = end
        self.api = shodan.Shodan(self.API_KEY)
        
    def run(self):
        data = []
        
        rsttotal = self.api.count(self.query)
        maxpage = (rsttotal['total']+99)/100

        if self.pageend > maxpage:
            self.pageend = maxpage
        for page in range(int(self.pagestart),int(self.pageend+1)):
            print ("Page:",page)
            try:
                result = self.api.search(self.query,page)
                for res in result['matches']:
                    #print res["port"]
                    #print res["ip_str"]
                    data.append(res["ip_str"] + ":" + str(res["port"]))
            except Exception as e:
                print (e)
        return data

