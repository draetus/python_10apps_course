import os
import csv
import data_types


def main():
    print_header()
    filename = get_data_file()
    print(filename)
    data = load_file(filename)
    query_data(data)


def print_header():
    print('-----------------------------')
    print(' REAL ESTATE DATA MINING APP')
    print('-----------------------------')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder,'data',
        'Sacramento-RealEstate-Transactions.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        
        reader = csv.DictReader(fin)
        purchases = []

        for row in reader:
            p = data_types.Purchase.create_from_dict(row)
            purchases.append(p)

        print(purchases[0].__dict__)


#LOADING WITHOUT THE CSV MODULE
#def load_file(filename):
#    with open(filename,'r',encoding = 'utf-8') as fin:
#        header = fin.readline().strip()
#        print('Found header: ' + header)
#
#        lines = []
#        for line in fin:
#            line_data = line.strip().split(',')
#            bed_count = line_data[4]
#            lines.append(line_data)
#
#        print(lines[:5])



def query_data(data):
    pass


if __name__ == '__main__':
    main()
