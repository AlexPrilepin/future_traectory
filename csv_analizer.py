import csv


def csv_to_list():
    with open('hosts.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        my_list = []
        for row in reader:
            beg = row[0].split(';')
            beg[-1] = beg[-1].split(',')
            my_list.append(beg)
        return my_list

