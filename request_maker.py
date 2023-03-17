import socket
from csv_analizer import csv_to_list
##from pythonping import ping

##WTF PING DOES NOT ; ADMIN NEED PERMISSION

list_servers = csv_to_list()


class One_request:
    def __init__(self, host, ports):
        self.host = host
        self.port = ports.split(',')
        self.requests = []

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
        self.state = None
        
    def check_host_and_port(self):
        pass

    def make_request(self):
        pass

    def log_yourself_into_upclass(self):
        pass


for i in list_servers:
    try:
        on = One_request(i[0], i[1])
    except Exception:
        if i[0].split('.') in [1, 3]:
            on = One_request(i[0], None)
        else:
            on = One_request(None, i[1])
##        try:
##            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##            host = i[0]
##            port = int(j)
##            conn.connect((host, port))
##            print(conn)
##            print()
##        except Exception as ex:
##            print(type(ex))
##            print()

