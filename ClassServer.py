#!/usr/bin/env python3
# -*- coding:utf-8 -*-
class Server:
    start_ip = 1
    
    def __init__(self):
        self.ip = Server.start_ip
        self.buffer = []
        Server.start_ip+=1
        self.router = None
        
    def get_ip(self):
        return self.ip
    
    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)
            
    def get_data(self):
        res = self.buffer[:]
        self.buffer = []
        return res

class Router:
    def __init__(self):
        self.data_base = {}
        self.buffer = []
        
    def link(self, server):
        if server not in self.data_base.keys():
            self.data_base[server.ip] = server
            server.router = self
        
    def unlink(self, server):
        server.router = None
        serv = self.data_base.pop(server.ip, False)
        if serv:
            serv.router = None
        
    def send_data(self):
        for data in self.buffer:
            if data.ip in self.data_base:
                self.data_base[data.ip].buffer.append(data)
        self.buffer.clear()            

class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

router = Router()
sv1 = Server()
sv2 = Server()
router.link(sv1)
router.link(sv2)
router.link(Server())
router.link(Server())
sv5 = Server()
router.link(sv5)

sv1.send_data(Data("Hello", sv5.get_ip()))
sv5.send_data(Data("Hello", sv2.get_ip()))

for data in router.__dict__['buffer']:
    print(data.data, '-->', data.ip)

router.send_data()

for server in router.data_base.keys():
    print(server, end='\t')
    if router.data_base[server].buffer:
        for el in router.data_base[server].buffer:
            print(el.ip, '--->>>', el.data)
    else:
        print('Nothing in the buffer')
        
print('END')