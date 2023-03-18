import socket
from pythonping import ping
import datetime
import whois

##WTF PING DOES NOT ; ADMIN NEED PERMISSION
##ping('8.8.8.8')

##domain = whois.query('google.com')


##AS WELL AS WHOIS
##print(domain.__dict__)



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
        self.rtt_max_ms = None
        self.state = False
        self.packets = 0.0
        self.make_request()
        
    def make_request(self):
        self.time_of_request = datetime.datetime.now()
        try:
            
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn.connect((self.host, int(self.port)))
            print(conn)
            conn_for_ip = str(conn).split('=')
            flag1 = False
            for i in conn_for_ip:
                if flag1:
                    self.ip_adress = i.split(', ')[0].strip('<>').strip('()').strip("'")
                    break
                if 'raddr' in i:
                    flag1 = True

            print()
############ MAKE WHOIS AND PYTHONPING REQUESTS
        except Exception as ex:
            print(ex)
            print()



