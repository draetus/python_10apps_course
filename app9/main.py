import os
import statistics
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
    with open(filename,'r',encoding='utf-8') as fin:
        
        reader = csv.DictReader(fin)
        purchases = []

        for row in reader:
            p = data_types.Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases

def get_price(p):
    return p.price

def query_data(data):
    data.sort(key=lambda p: p.price)

    high_purchase = data[-1]
    print('The most expensive house is {:,}$ with {} beds and {} baths'.format(
        high_purchase.price, high_purchase.beds,high_purchase.baths))

    low_purchase = data[0]
    print('The least expensive house is {:,}$ with {} beds and {} baths'.format(
        low_purchase.price,low_purchase.beds,low_purchase.baths))

    prices = [
            p.price
            for p in data]

    ave_price = statistics.mean(prices)

    print('The average home price is {:,}$'.format(int(ave_price)))

    two_bed_homes = (
            p
            for p in data
            if announce(p,'2-bedrooms, found {}'.format(p.beds)) and p.beds == 2)

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    ave_price = statistics.mean((announce(p.price, 'price') for p in homes))
    ave_baths = statistics.mean((p.baths for p in homes))
    ave_sqft  = statistics.mean((p.sqft for p in homes))
    print('The average 2 bedroom home is {:,}$, baths={}, sq ft={:,}'.format(
        int(ave_price), round(ave_baths,1), round(ave_sqft,1)))


def announce(item,msg):
    print('Pulling item {} for {}'.format(item,msg))
    return item


if __name__ == '__main__':
    main()
