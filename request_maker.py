import socket
from pythonping import ping
import datetime
import whois

##WTF PING DOES NOT ; ADMIN NEED PERMISSION
##print(ping('8.8.8.8').__dict__)
##print(ping('8.8.8.8', count=1).__dict__['_responses'])

##domain = whois.query('google.com')


##AS WELL AS WHOIS
##print(domain.__dict__)
##import os
##hostname = "google.com" #example
##response = os.system("ping -c 1 " + hostname)
##


class One_request:
    def __init__(self, host, ports):
        self.host = host
        self.ports = ports
        self.requests = []
        self.group_requester()

    def make_single_request(self, port):
        obj = Single_port_request(self.host, port)
        self.requests.append(obj)

    def group_requester(self):
        for i in self.ports:
            self.make_single_request(i)
    
class Single_port_request:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.time_of_request = None
        self.ip_adress = None
        self.rtt_max_ms = '2000 ms'
        self.state = False
        self.packets = 1.0
        self.make_request()
        
    def make_request(self):
        self.time_of_request = datetime.datetime.now()
        try:
            pg = str(ping('8.8.8.8', count=1).__dict__['_responses'][0]).split()[-1]
            print(pg)
            self.packets = 1.0
            self.rtt_max_ms = pg
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn.connect((self.host, int(self.port)))
            conn_for_ip = str(conn).split('=')
            flag1 = False
            for i in conn_for_ip:
                if flag1:
                    self.ip_adress = i.split(', ')[0].strip('<>').strip('()').strip("'")
                    break
                if 'raddr' in i:
                    flag1 = True

            print()
            self.state = True
############ MAKE WHOIS AND PYTHONPING REQUESTS
        except Exception as ex:
            print(type(ex), ex)
            print()



