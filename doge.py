#!/usr/bin/env python
import sys
import requests
import json

class MarketData(object):
    
    def __init__(self, raw_json=None):
        self.raw_json = raw_json

    def get_data(self):
        resp = requests.get('http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132')
        resp.raise_for_status()
        self.raw_json = json.loads(resp.content)
        if not self.raw_json['success']:
            raise Exception('Something went wrong')
        self.raw_json = self.raw_json['return']['markets']['DOGE']

    def get_last_trade_price(self):
        return self.raw_json['lasttradeprice']

    def get_stats(self):
        price_sum = 0.0
        for trade in self.raw_json['recenttrades']:
            price_sum += float(trade['price'])
        avg = price_sum / len(self.raw_json['recenttrades'])
        s = sorted(self.raw_json['recenttrades'], key=lambda trade: trade['price'])
        length = len(s)
        if not len(s) % 2:
            median = (float((s[length / 2]['price'])) + float(s[length / 2 - 1]['price'])) / 2.0
        median = float(s[length / 2]['price'])
        return avg, median, length

def main(btc):
    btc = float(btc)
    market_data = MarketData()
    market_data.get_data()
    last_price = float(market_data.get_last_trade_price())
    can_purchase = btc / last_price
    avg, median, length = market_data.get_stats()
    print 'You can purchase {} DOGE with {} BTC at price {}'.format(can_purchase, btc, last_price)
    print 'Average price over last {} recent trades is {}'.format(length, avg)
    print 'Median price over last {} recent trades is {}'.format(length, median)

if __name__ == '__main__':
    main(*sys.argv[1:])
