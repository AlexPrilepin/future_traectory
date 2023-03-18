from csv_analizer import csv_to_list
from request_maker import One_request, Single_port_request


list_servers = csv_to_list()


for i in list_servers:
    try:
        on = One_request(i[0], i[1])
    except Exception:
        if i[0].split('.') in [1, 3]:
            on = One_request(i[0], None)
        else:
            on = One_request(None, i[1])
