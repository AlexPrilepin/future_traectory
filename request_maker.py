import socket
from pythonping import ping
import datetime

# we put each element from the table into this class
class One_request:
    def __init__(self, host, ports):
        self.host = host
        self.ports = ports
#   here is a list of all the examples of Single_port_request, which are relevant to our example
        self.requests = []
        self.message = ''
# list of ip_adresses for the domain given
        try:
            self.ip_adresses = socket.gethostbyname_ex(self.host)[2] if host != None else []
        except Exception:
            self.ip_adresses = []
            self.message = '\t\nDUE TO THE SYSTEM ANSWER, POSSIBLY THIS WEBSITE DOES NOT EXIST'
        self.group_requester()
# checking incorrect ports
        for i in self.ports:
            if i.isdigit() is False:
                del self.ports[self.ports.index(i)]
# this function is here to make all possible requests with all permutations of ports and ip_adresses
    def group_requester(self):
        if not self.ip_adresses:
            for i in self.ports:
                self.make_single_request(i)
        else:
            for i in self.ports:
                for j in self.ip_adresses:
                    self.make_single_request(i, j)
# and this one just creates an example of Single_port_request class, adds it to requests list 
    def make_single_request(self, port, ip=None):
        obj = Single_port_request(self.host, port) if self.ip_adresses == [] else  Single_port_request(self.host, port, ip)
        self.requests.append(obj)
 
# this class is aimed to collect all the data for a particular ip and port combination
class Single_port_request:
    def __init__(self, host, port, ip=None):
# just all the data to collect
        self.host = ip if ip!= None else host 
        self.port = port if port.isdigit() else '???'
        self.time_of_request = None
        self.ip_adress = None
        self.rtt_max_ms = '2000 ms'
        self.state = False
        self.packets_loss = 0.0
        self.make_request()
# turning data into a good condition :)
        if self.ip_adress == None:
            if self.host.count('.') == 3:
                self.ip_adress = self.host
        if self.ip_adress == None:
            self.ip_adress = '???'
        
    def make_request(self):
# time of request
        self.time_of_request = datetime.datetime.now()
# pinging
        try:
            zzz = ping(self.host, count=1, timeout=2)
            if str(zzz).split()[0].lower() == 'reply':
                pg = str(zzz.__dict__['_responses'][0]).split()[-1]
                self.rtt_max_ms = pg 
            else:
                self.packets_loss = 1.0
        except Exception:
            pass
# using socket            
        if self.port != '???':
            try:
                conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                conn.settimeout(8)
                conn.connect((self.host, int(self.port)))
                conn_for_ip = str(conn).split('=')
                flag1 = False
                for i in conn_for_ip:
                    if flag1:
                        self.ip_adress = i.split(', ')[0].strip('<>').strip('()').strip("'")
                        break
                    if 'raddr' in i:
                        flag1 = True
                self.state = True
            except Exception as ex:
                if str(type(ex)) == "<class 'socket.timeout'>":
                    self.packets_loss = 1.0
        else:
            self.port = -1
            self.state = '???'
        if self.state == False:
            self.state = 'Not Opened'
        elif self.state == True:
            self.state = 'Opened'