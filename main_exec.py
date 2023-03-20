from csv_analizer import csv_to_list
from request_maker import One_request, Single_port_request
import urllib
from urllib import request


def execution():
# gitting a table
	try:
		list_servers = csv_to_list()
	except Exception:
		print("IT SEEMS THAT EITHER THE CSV TABLE DOES NOT EXIST OR ITS NAME OR/AND DIRECTORY HAS BEEN CHANGED")
		return
	domains = []
	final_results = []
# checking connection
	try:
	    urllib.request.urlopen("http://google.com")
	except IOError:
	    "OOOPS!!! Internet seems to be absent example your device!"
	    return
# checking the table
	for i in list_servers:
		if len(i) != 2:
			print('WRONG INPUT GIVEN')
			return
		elif i[0] == '':
			print('NULL SPACE IN STEAD OF IP_ADRESS/DOMAIN GIVEN')
			return
# working with classes
	for i in list_servers:
	    try:
	        example = One_request(i[0], i[1])
	    except Exception:
	        if i[0].split('.') in [1, 3]:
	            example = One_request(i[0], None)
	        else:
	            example = One_request(None, i[1])
	    domains.append(example)
# turning the info into normal format
	for i in domains:
		main_info = [i.host if i.host.count('.') < 2 else '???', i.ip_adresses, i.ports]
		big_lines = []
		for j in i.requests:
			stdout = []
			stdout.append(str(j.time_of_request))
			stdout.append(i.host if i.host.count('.') < 2 else '???')
			stdout.append(str(j.ip_adress))
			stdout.append(str(j.packets_loss))
			stdout.append(str(j.rtt_max_ms)) 
			stdout.append(str(j.port) if str(j.port).isdigit() else '-1')
			stdout.append(str(j.state) )
			big_lines.append('\t' + ' ||| '.join(stdout))
		final_results.append([main_info, big_lines, i.message])
# printing
	for i in final_results:
		print(i[0])
		for j in i[1]:
			print(j)
		print(i[2])
		print('\n' + '-' * 20 + '\n')
	print()
